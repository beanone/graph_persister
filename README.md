# Graph Persister

A Python project for persisting hierarchical Stochastic Block Model (hSBM) graphs using the `graph_builder` API. This tool allows you to serialize NetworkX graphs (with node and edge properties) to disk, supporting downstream analysis, visualization, and integration with Large Language Models (LLMs) as a knowledge source.

## Features
- Converts NetworkX hSBM graphs to a persistent format
- Stores node and edge properties, including hierarchical levels
- Uses SQLite for efficient indexing
- Modular and extensible architecture
- Enables use of graph data as structured knowledge for LLMs and AI applications

## Project Structure
```
├── src/                # Main source code (if applicable)
├── graph_persister/    # Core logic for graph persistence
│   └── persister.py    # Main entry point for persisting graphs
├── tests/              # Unit and integration tests
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
```

## Requirements
- Python 3.12+
- [NetworkX](https://networkx.org/)

## Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo>
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

## Usage
1. **Prepare your NetworkX graph** (e.g., `topic_graph.gpickle`).
2. **Run the persister:**
   ```bash
   python -m graph_persister.persister
   ```
   This will load the graph and persist it to the `.graph/graphdb` directory.

## License
MIT License

## Acknowledgments
- [NetworkX](https://networkx.org/)

---

For more details, see the code and docstrings in each module.