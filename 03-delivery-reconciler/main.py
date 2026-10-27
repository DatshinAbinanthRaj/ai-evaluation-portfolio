"""Compare ordered and delivered mass by zone and bar diameter. Synthetic educational demo; see README for limits."""
from collections import defaultdict
from decimal import Decimal

def evaluate(data):
    order, delivered = defaultdict(Decimal), defaultdict(Decimal)
    seen = set()
    for row in data['orders']:
        order[(row['zone'],row['diameter_mm'])] += Decimal(str(row['kg']))
    for row in data['tickets']:
        if row['id'] in seen:
            raise ValueError('Duplicate ticket ID')
        seen.add(row['id'])
        delivered[(row['zone'],row['diameter_mm'])] += Decimal(str(row['kg']))
    return [{'zone':z,'diameter_mm':d,'ordered_kg':float(order[(z,d)]),'delivered_kg':float(delivered[(z,d)]),'variance_kg':float(delivered[(z,d)]-order[(z,d)])} for z,d in sorted(order.keys() | delivered.keys())]


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
