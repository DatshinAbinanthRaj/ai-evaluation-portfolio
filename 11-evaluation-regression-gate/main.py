"""Compare baseline and candidate pass/fail results on the same test IDs. Synthetic educational demo; see README for limits."""
def evaluate(data):
    old,new = data['baseline'],data['candidate']
    if old.keys() != new.keys():
        raise ValueError('Case IDs must match')
    if any(type(v) is not bool for v in list(old.values())+list(new.values())):
        raise ValueError('Outcomes must be booleans')
    regressed = sorted(k for k in old if old[k] and not new[k])
    improved = sorted(k for k in old if not old[k] and new[k])
    return {'regressions':regressed,'improvements':improved,'gate':'no_data' if not old else ('fail' if regressed else 'pass')}


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
