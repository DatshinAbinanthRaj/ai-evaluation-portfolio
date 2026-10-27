"""Compare a reported quantity against a reference after unit conversion. Synthetic educational demo; see README for limits."""
import math
UNITS = {'m':('length',1.0),'mm':('length',0.001),'kg':('mass',1.0),'g':('mass',0.001)}
def evaluate(data):
    ref, candidate, tolerance = (float(data[k]) for k in ('reference','candidate','tolerance'))
    if not all(map(math.isfinite,(ref,candidate,tolerance))) or tolerance < 0:
        raise ValueError('Finite numbers and non-negative tolerance required')
    rd, rf = UNITS[data['reference_unit']]
    cd, cf = UNITS[data['candidate_unit']]
    if rd != cd:
        return {'status':'incompatible_units'}
    error = abs(candidate*cf/rf-ref)
    return {'status':'pass' if error <= tolerance or math.isclose(error,tolerance,abs_tol=1e-12) else 'fail','absolute_error':round(error,9)}


if __name__ == "__main__":
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(Path(__file__).with_name("sample.json")))
    args = parser.parse_args()
    print(json.dumps(evaluate(json.loads(Path(args.input).read_text())), indent=2))
