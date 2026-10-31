
runbooks =[
    {
        "id":"1",
        "title":"Database Connection Error",
        "description":"Check Database Credentials"
    },
    {
        "id":"2",
        "title":"Application Memory Error",
        "description":"Increase Jvm Heap Size"
    },
    {
      "id":"3",
      "title":"Api Timeout",
      "description":"Check Network Connectivity"
    }
]

for runbook in runbooks:
    print(runbook["title"])


print("Total Run books",len(runbooks))


from search import search_runbooks

matches = search_runbooks(runbooks,"database")

for match in matches:
    print("title",match["title"])
    print("description",match["description"])