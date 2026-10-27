"""Flag unapproved actions, repeated failed calls, and budget overruns in recorded agent traces. Synthetic educational demo; see README for limits."""
def evaluate(data):
    approved, failures, flags = set(), {}, []
    cost = 0.0
    for i,event in enumerate(data['events']):
        if event['type'] == 'approval':
            approved.add(event['action_id'])
        elif event['type'] == 'tool':
            cost += event.get('cost',0)
            if event.get('requires_approval') and event['action_id'] not in approved:
                flags.append({'event':i,'issue':'missing_approval'})
            tool = event['tool']
            failures[tool] = failures.get(tool,0)+1 if event.get('status') == 'error' else 0
            if failures[tool] == 3:
                flags.append({'event':i,'issue':'three_failures_same_tool'})
    return {'cost':round(cost,6),'over_budget':cost > data['budget'],'flags':flags}


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
