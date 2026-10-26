# SSTriples

Optimal solutions for the 150 SSTriples instances of BPPLIB
(da Silva and Schouery, INFORMS Journal on Computing,
doi:10.1287/ijoc.2023.0399).

BPPLIB's `Solutions.xlsx` (snapshot of February 2026) lists 58 of these
instances as open, with best known upper bound LB + 1. The solutions in
this folder are the first reported solutions attaining the lower bound
for these 58 instances, which closes them: all 150 SSTriples instances are
now solved to optimality.

| Group       | Instances | Open in BPPLIB | Closed here |
|-------------|-----------|----------------|-------------|
| N216W10000  | 50        | 6              | 6           |
| N405W15000  | 50        | 15             | 15          |
| N648W20000  | 50        | 37             | 37          |
| **Total**   | **150**   | **58**         | **58**      |

`instances.csv` reports, for each instance, the LB and UB from BPPLIB, the
number of bins of the solution here, and whether the instance was open.

## BPP and CSP versions

The CSP files of SSTriples (`9_SSTriples_CSP.rar`) contain the same
multisets of weights as the BPP files, so each solution here is valid for
both versions. To obtain a CSP solution, group identical bins into
patterns with multiplicity.

## How to verify

1. Download `Instances/Benchmarks/9_SSTriples_BPP.rar` from BPPLIB and extract it.
2. From the repository root, run:

```
python tools/verify.py --instances path/to/SSTriples-BPP --solutions solutions/SSTriples --list solutions/SSTriples/instances.csv
```

Expected output: `150 verified, 0 failed, 150 checked`.

## Method

The solutions were found with a new approach. The method will be described in a forthcoming paper.

## References

- R. F. F. da Silva, R. C. S. Schouery. Solving cutting stock problems via
  an extended Ryan–Foster branching scheme and fast column generation.
  INFORMS Journal on Computing, 2023. doi:10.1287/ijoc.2023.0399
- M. Delorme, M. Iori, S. Martello. BPPLIB: a library for bin packing and
  cutting stock problems. Optimization Letters 12:235–250, 2018.
