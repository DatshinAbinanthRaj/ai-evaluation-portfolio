"""Find field changes between two structured document revisions. Synthetic educational demo; see README for limits."""
def index(rows):
    result = {}
    for row in rows:
        if row['id'] in result:
            raise ValueError('Duplicate record ID')
        result[row['id']] = row
    return result

def evaluate(data):
    old, new = index(data['old']), index(data['new'])
    changes = []
    for key in sorted(old.keys() | new.keys()):
        if key not in old or key not in new:
            changes.append({'id':key,'status':'added' if key in new else 'removed'})
            continue
        for field in sorted((old[key].keys() | new[key].keys()) - {'id'}):
            if field not in old[key] or field not in new[key] or old[key][field] != new[key][field]:
                changes.append({'id':key,'field':field,'old':old[key].get(field),'new':new[key].get(field),'old_present':field in old[key],'new_present':field in new[key]})
    return changes


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
