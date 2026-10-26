#!/usr/bin/env python3
"""
Independent verifier for SSTriples BPP solutions.

Instance format (BPPLIB): first line n, second line W, then n item weights.
Solution format: one bin per line, item weights separated by spaces.
Empty lines and lines starting with '#' are ignored.

A solution is accepted if and only if:
  1. it uses exactly LB = ceil(sum(w) / W) bins (hence it is optimal);
  2. every bin has total weight exactly W (no bin exceeds the capacity);
  3. the multiset of weights in the solution equals the multiset in the instance.

Usage:
  python verify.py --instances DIR --solutions DIR [--list instances.csv]

Only the Python standard library is used. MIT License.
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


def read_instance(path):
    vals = [int(t) for t in path.read_text().split()]
    n, W, w = vals[0], vals[1], vals[2:]
    if len(w) != n:
        raise ValueError(f"declares n={n} but contains {len(w)} weights")
    return W, w


def read_solution(path):
    bins = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            bins.append([int(t) for t in line.split()])
    return bins


def check(W, weights, bins):
    lb = -(-sum(weights) // W)
    errors = []
    if len(bins) != lb:
        errors.append(f"{len(bins)} bins, LB = {lb}")
    for i, b in enumerate(bins, 1):
        if sum(b) != W:
            errors.append(f"bin {i} sums to {sum(b)}, W = {W}")
    if Counter(x for b in bins for x in b) != Counter(weights):
        errors.append("multiset of weights differs from the instance")
    return lb, errors


def find(directory, name):
    hits = [p for p in directory.rglob("*") if p.is_file() and p.stem == name]
    return hits[0] if hits else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--instances", required=True, type=Path)
    ap.add_argument("--solutions", required=True, type=Path)
    ap.add_argument("--list", type=Path, help="CSV with an 'instance' column")
    a = ap.parse_args()

    if a.list:
        with a.list.open() as f:
            names = [r["instance"] for r in csv.DictReader(f)]
    else:
        names = sorted(p.stem for p in a.solutions.rglob("*") if p.is_file())

    ok = bad = 0
    for name in names:
        inst, sol = find(a.instances, name), find(a.solutions, name)
        if inst is None or sol is None:
            print(f"MISSING {name}: instance={inst} solution={sol}")
            bad += 1
            continue
        W, w = read_instance(inst)
        lb, errors = check(W, w, read_solution(sol))
        if errors:
            print(f"FAIL    {name}: " + "; ".join(errors))
            bad += 1
        else:
            print(f"OK      {name}: {lb} bins = LB (optimal)")
            ok += 1

    print(f"\n{ok} verified, {bad} failed, {ok + bad} checked")
    sys.exit(1 if bad or ok == 0 else 0)


if __name__ == "__main__":
    main()
