"""Check whether a cited quotation exists in the cited source. Synthetic educational demo; see README for limits."""
def evaluate(data):
    normalize = lambda text: ' '.join(text.split())
    results = []
    for claim in data['claims']:
        source = data['sources'].get(claim['source_id'])
        quote = normalize(claim['quote'])
        status = 'missing_source' if source is None else ('quote_present' if quote and quote in normalize(source) else 'quote_missing')
        results.append({'id': claim['id'], 'status': status})
    return results


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
