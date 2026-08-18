#!/usr/bin/env python3
"""Regression tests for check_slop.py.

Run from anywhere: python3 tests/run_tests.py
Asserts the slop sample trips every pattern family it contains and the
clean sample exits 0. Uses required-substring checks rather than exact
FAIL counts so adding banned words doesn't break the suite.
"""
import subprocess
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
script = here.parent / "scripts" / "check_slop.py"

def run(sample, doc_type):
    r = subprocess.run(
        [sys.executable, str(script), str(here / sample), "--type", doc_type],
        capture_output=True, text=True)
    return r.returncode, r.stdout

failures = []

code, out = run("slop-sample.md", "social")
if code != 1:
    failures.append(f"slop-sample expected exit 1, got {code}")
required = [
    "em dash",
    "banned phrase: Let's dive in",
    "banned phrase: Let that sink in",
    "banned phrase: Read that again",
    "banned phrase: What's your take?",
    "contrast-punch",
    "count-teaser",
    "negative listing",
    "two-beat kicker",
    "bold-label bullet",
    "relative-clause fragment",
    "elided predicate",
    "spaced hyphen",
    "Title Case header",
    "social: no markdown headers",
]
for r in required:
    if r not in out:
        failures.append(f"slop-sample missing expected finding: {r}")

code, out = run("clean-sample.md", "docs")
if code != 0:
    failures.append(f"clean-sample expected exit 0, got {code}:\n{out}")

if failures:
    print("REGRESSION FAILURES:")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("all regression checks passed")
