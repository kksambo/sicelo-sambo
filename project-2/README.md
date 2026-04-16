## Weighted Average Signal Filter

## Description

This project is a simple Python program that smooths a signal using a weighted average.

It keeps track of the last **n values** and applies weights to calculate a filtered (smoothed) output.

---

## How it works

* Takes a list of weights
* Stores the last n input values using a buffer
* Multiplies each value by its corresponding weight
* Computes the weighted average
* Returns a smoother version of the signal

---

## How to run

### 1. Clone the repository

```bash
git clone https://github.com/kksambo/sicelo-sambo.git
cd project-2
```

### 2. Run the program

```bash
python weighted_average.py
```

---

## Example

Output:

```
Input: 0.000 -> Filtered: 0.000
Input: 0.199 -> Filtered: 0.000
Input: 0.389 -> Filtered: 0.000
...
Input: 0.717 -> Filtered: 0.456
```

Explanation:

* First few outputs are `0.0` because the buffer is not full yet
* Once enough values are collected, the weighted average is applied

---

## Files

```
weighted_average.py
README.md
```

---

## Branch name

```
sicelo-2026/weighted-sum-average
```
