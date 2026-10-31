from src.search import search_runbooks



def test_search_database():
    runbooks = [
        {
            "id": 1,
            "title": "Database Connection Error",
            "resolution": "Check database credentials"
        },
        {
            "id": 2,
            "title": "Application Memory Error",
            "resolution": "Increase JVM heap size"
        }
    ]

    results = search_runbooks(runbooks, "database")

    assert len(results) == 1
    assert results[0]["title"] == "Database Connection Error"


def test_search_jvm() :
    runbook =[{
        "id":"1",
        "title":"Application Memory Error",

    }]

def test_search_empty_keyword():
    runbooks =[{
        "id":1,
        "title":"Database Connection Error",
        "resolution" :"check database credentials"

    }]
    results = search_runbooks(runbooks,"")
    assert results==[]