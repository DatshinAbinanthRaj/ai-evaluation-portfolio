"""Rank evaluation cases using explicit severity and confidence rules. Synthetic educational demo; see README for limits."""
SEVERITY = {'low':1,'medium':2,'high':3,'critical':4}
def evaluate(data):
    queue = []
    for item in data['cases']:
        confidence = item['confidence']
        if not 0 <= confidence <= 1:
            raise ValueError('confidence must be between 0 and 1')
        reasons = []
        if item['severity'] in ('high','critical'):
            reasons.append('high_severity')
        if confidence < 0.7:
            reasons.append('low_confidence')
        if item.get('disagreement'):
            reasons.append('annotator_disagreement')
        if reasons:
            priority = SEVERITY[item['severity']]*10 + (1-confidence)*5 + 3*bool(item.get('disagreement'))
            queue.append({'id':item['id'],'priority':round(priority,3),'reasons':reasons})
    return sorted(queue,key=lambda row:(-row['priority'],row['id']))


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
