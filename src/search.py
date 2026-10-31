import json

def search_runbooks(runbooks, keyword):
    results = []

    keyword = keyword.strip().lower()

    if not keyword:
        return []

    for runbook in runbooks:
        title = runbook["title"].lower()
        resolution = runbook["resolution"].lower()

        if keyword in title or keyword in resolution:
            results.append(runbook)

    return results


def load_runbooks(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        runbooks = json.load(f)

        return runbooks


def rank_runbooks(runbooks, keyword):
    results = []
    keyword = keyword.lower().strip()

    if not keyword:
        return results

    for runbook in runbooks:
        title = runbook["title"].lower()
        resolution = runbook["resolution"].lower()

        score = 0

        if keyword in title:
            score += 10

        if keyword in resolution:
            score += 5

        if score > 0:
            results.append({
                "runbook": runbook,
                "score": score
            })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results
