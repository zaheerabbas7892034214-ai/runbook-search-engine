
# Runbook Search Engine

## Project Overview
A Python-based search engine that helps production
support engineers find troubleshooting runbooks.

## Features
- Search runbooks by keyword
- Case-insensitive matching
- Search titles and resolutions
- Load runbooks from JSON
- Automated unit testing with pytest

## Technology Stack
- Python
- JSON
- pytest

## Project Structure
- src/main.py - Application entry point
- src/search.py - Keyword search logic
- src/loader.py - JSON file loading
- data/runbooks.json - Troubleshooting runbooks
- tests/test_search.py - Unit tests

## How to Run

From the project root:

python -m src.main

## How to Test

python -m pytest tests/ -v

## Future Improvements
- Search ranking
- FastAPI REST endpoints
- Semantic search with embeddings
- RAG integration
