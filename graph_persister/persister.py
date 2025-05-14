from graph_builder.storage_manager import GraphBuilder
from graph_builder.config import GraphBuilderConfig
import networkx as nx
import os
import pickle

def persist_hsbm_graph_to_graphbuilder(
    nx_graph: nx.Graph,
    output_dir: str
) -> None:
    """
    Persist a NetworkX hSBM graph (with node/edge properties, including hierarchical levels)
    to disk using the graph_builder API.

    Args:
        nx_graph (nx.Graph): The NetworkX graph with hSBM community and hierarchy properties.
        output_dir (str): Directory to store the graph_builder output.

    Returns:
        None

    Example:
        persist_hsbm_graph_to_graphbuilder(graph, "output/graphdb")
    """
    os.makedirs(output_dir, exist_ok=True)
    config = GraphBuilderConfig(output_dir=output_dir)
    builder = GraphBuilder(config)

    # Add nodes/entities
    node_to_entity_id = {}
    entity_id = 0
    for node, data in nx_graph.nodes(data=True):
        builder.add_entity(entity_id, {
            "name": node,
            "community": data["community"],
            "levels": data["levels"],
            "keywords": data["keywords"]})
        node_to_entity_id[node] = entity_id
        entity_id += 1

    # Add edges/relations using mapped entity IDs
    rel_id = 0
    for u, v, data in nx_graph.edges(data=True):
        builder.add_relation(
            rel_id,
            node_to_entity_id[u],
            node_to_entity_id[v],
            dict(data)
        )
        rel_id += 1

    builder.finalize()

if __name__ == "__main__":
    # Load the graph from the pickle file
    with open("resources/models/topic_graph.gpickle", "rb") as f:
        nx_graph = pickle.load(f)

    # Persist the graph to the graph_builder
    persist_hsbm_graph_to_graphbuilder(nx_graph, ".graph/graphdb")
