# `Binomial Expansion CLI Tool`
This script expands upto `n = 18` of an expression using the binomial expansion formula.

## The Binomial Theorem
In essence, any valid expression of the form $\(a + b\)^n$ can be expanded using the formula: $\sum\limits_{k=0}^{n} \binom{n}{k} \(a)^{n-k} \(b)^{k}\$

## Usage
```bash
python main.py --exp (a + b)^k
```
--exp, is a flag telling the CLI the expression to expand
