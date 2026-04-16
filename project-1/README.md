# Word Frequency Tracker

## Description

This project is a simple Python program that counts words and shows the most frequent ones.

It reads a sentence, removes numbers and symbols, and then tracks how many times each word appears.

---

## How it works

* Takes a text input
* Uses regex to keep only words (letters only)
* Counts each word
* Shows the top N most used words
* Updates results step by step

---

## How to run

### 1. Clone the repository

```bash
git clone https://github.com/kksambo/sicelo-sambo.git
cd project-1
```

### 2. Run the program

```bash
python frequently_used_words.py
```

---

## Example

Input:

```
mine ngibona umfana, umfana weftukile uyafoma -> I see a boy, the boy is scared he is even sweating
```

Output:

```
[('mine', 1)]
[('mine', 1), ('ngibona', 1)]
[('umfana', 2), ('mine', 1)]
...
```

---

## Files

```
frequently_used_word.py
README.md
```

---

## Branch name

```
sicelo-2026/frequently-used-words
```


