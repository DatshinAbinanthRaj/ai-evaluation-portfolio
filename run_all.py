"""Run every standalone demo and its tests. No external packages required."""
from pathlib import Path
import subprocess, sys
root = Path(__file__).resolve().parent
for folder in sorted(root.glob('[0-9][0-9]-*')):
    print('Testing ' + folder.name, flush=True)
    subprocess.run([sys.executable, '-m', 'unittest', '-v'], cwd=folder, check=True)
    result = subprocess.run([sys.executable, 'main.py'], cwd=folder, check=True, capture_output=True, text=True)
    (folder/'example_output.json').write_text(result.stdout)
print('All 12 projects passed tests and demo runs.')
