"""Calculate raw agreement and Cohen kappa for two annotators. Synthetic educational demo; see README for limits."""
from collections import Counter

def evaluate(data):
    a,b = data['a'],data['b']
    if len(a) != len(b):
        raise ValueError('Aligned arrays must have equal length')
    n = len(a)
    if not n:
        return {'n':0,'agreement':None,'kappa':None}
    ca,cb = Counter(a),Counter(b)
    observed = sum(x==y for x,y in zip(a,b))/n
    expected = sum(ca[k]*cb[k] for k in ca.keys() | cb.keys())/(n*n)
    return {'n':n,'agreement':round(observed,4),'kappa':round((observed-expected)/(1-expected),4) if expected < 1 else None}


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
