"""Find normalized exact duplicates shared by train and evaluation sets. Synthetic educational demo; see README for limits."""
def evaluate(data):
    norm = lambda s: ' '.join(s.casefold().split())
    train = {}
    for i,text in enumerate(data['train']):
        if norm(text):
            train.setdefault(norm(text),[]).append(i)
    return [{'evaluation_index':i,'train_indices':train[norm(text)]} for i,text in enumerate(data['evaluation']) if norm(text) and norm(text) in train]


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
