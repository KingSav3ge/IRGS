"""Joined-checkout convenience entry for the App-owned reference attachment tool."""
from pathlib import Path
import runpy

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).resolve().parent.parent / 'IRGS_Web/register_historical_archive.py'), run_name='__main__')
