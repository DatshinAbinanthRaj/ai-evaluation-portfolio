"""Check flat JSON responses for required fields, field types, and unexpected keys. Synthetic educational demo; see README for limits."""
TYPES = {'string':str,'integer':int,'number':(int,float),'boolean':bool,'array':list}
def evaluate(data):
    schema, value = data['schema'],data['value']
    if not isinstance(value,dict):
        return {'valid':False,'errors':['root: expected object']}
    errors = []
    for key,kind in schema.items():
        if key not in value:
            errors.append(key+': missing')
        elif not isinstance(value[key],TYPES[kind]) or (kind in ('integer','number') and isinstance(value[key],bool)):
            errors.append(key+': wrong type')
    errors.extend(key+': unexpected' for key in sorted(value.keys()-schema.keys()))
    return {'valid':not errors,'errors':errors}


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
