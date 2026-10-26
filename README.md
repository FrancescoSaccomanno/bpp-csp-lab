# bpp-csp-lab

Research on one-dimensional bin packing (BPP) and cutting stock (CSP)
problems: solutions for benchmark instances, verification tools and, in
future releases, solver code.

Instances come from [BPPLIB](https://github.com/mdelorme2/BPPLIB).

## Contents

```
solutions/    solutions for benchmark instances, one folder per class
tools/        verification and utility scripts
```

| Folder | Instances | Result |
|---|---|---|
| [`solutions/SSTriples/`](solutions/SSTriples/) | 150 SSTriples (BPP and CSP) | All 150 solved with LB bins, including the 58 listed as open in BPPLIB |

## Verification

`tools/verify.py` uses only the Python standard library and shares no
code with the solvers used to find the solutions. For each instance it
checks that:
1. the solution uses exactly LB = ⌈Σw / W⌉ bins;
2. every bin has total weight exactly W;
3. the multiset of weights is identical to the instance file.

```
python tools/verify.py --instances path/to/instances --solutions solutions/SSTriples --list solutions/SSTriples/instances.csv
```

## Solution format

One file per instance, named `<instance>.sol`. One bin per line, with the
weights of its items separated by spaces. Lines starting with `#` are
comments.

## Citation

Please cite this repository through its Zenodo DOI (see `CITATION.cff`)
and the original sources of the instances, listed in each folder.

## License

Solutions and tables: CC BY 4.0. Code in `tools/`: MIT.
