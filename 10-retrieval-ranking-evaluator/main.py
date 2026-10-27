"""Measure precision, recall, and reciprocal rank for retrieved document IDs. Synthetic educational demo; see README for limits."""
def evaluate(data):
    k = data['k']
    if not isinstance(k,int) or isinstance(k,bool) or k < 1:
        raise ValueError('k must be a positive integer')
    ranking = list(dict.fromkeys(data['retrieved']))[:k]
    relevant = set(data['relevant'])
    hits = sum(doc in relevant for doc in ranking)
    reciprocal = next((1/i for i,doc in enumerate(ranking,1) if doc in relevant),0)
    return {'precision_at_k':round(hits/k,4),'recall_at_k':round(hits/len(relevant),4) if relevant else None,'reciprocal_rank_at_k':round(reciprocal,4)}


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
