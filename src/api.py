from fastapi import FastAPI,Query
from pathlib import Path

from src.search import  load_runbooks
from src.search import search_runbooks, rank_runbooks

app = FastAPI(
    title ="Run book search api",
    version="1.0.0"

)

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "runbooks.json"

@app.get("/health")
def health_check():
    return {"status":"healthy"}

@app.get("/runbooks")
def get_runbooks():
    return load_runbooks(FILE_PATH)

@app.get("/runbooks/search")
def search(keyword:str =Query(min_length=1)):
    runbooks = load_runbooks(FILE_PATH)
    results = search_runbooks(runbooks, keyword)
    return {
        "keyword":keyword,
        "count":len(results),
        "results":results
    }


@app.get("/runbooks/rank")
def rank(keyword:str =Query(min_length=1)):
    runbooks = load_runbooks(FILE_PATH)
    results = rank_runbooks(runbooks, keyword)

    return {
        "keyword":keyword,
        "count":len(results),
        "results":results
    }
