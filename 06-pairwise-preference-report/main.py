"""Summarize human A/B preferences, ties, and invalid votes. Synthetic educational demo; see README for limits."""
from collections import Counter

def evaluate(data):
    counts = Counter(data['votes'])
    a,b,t = (counts[k] for k in ('A','B','tie'))
    invalid = len(data['votes'])-a-b-t
    return {'A':a,'B':b,'ties':t,'invalid':invalid,'A_win_rate_excluding_ties':round(a/(a+b),4) if a+b else None}


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
