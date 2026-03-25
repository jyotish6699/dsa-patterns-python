# ⚡ Longest Consecutive Sequence — Version 2 (Better Approach)

## 🎯 Goal

Improve brute force by:

* Reducing lookup time
* Keeping logic simple

---

## 🔧 Improvements Over v1

### 1. ⚡ Faster Lookup Using Set

* Convert list → set
* Lookup becomes O(1) instead of O(n)

---

### 2. 🔁 Same Sequence Logic

Still:

* Start from each number
* Move forward step-by-step
* Count sequence length

---

## ⚠️ What is STILL wrong?

### ❌ Repeated Work Exists

Example:

```id="f3tt8m"
[1,2,3,4]
```

* Start from 1 → full sequence
* Start from 2 → repeat
* Start from 3 → repeat again

👉 Same sequence calculated multiple times

---

## ⏱️ Complexity

### Time Complexity: **O(n²)**

* Outer loop → O(n)
* Inner sequence expansion → up to O(n)

---

### Space Complexity: **O(n)**

* Set used for lookup

---

## 🧠 What You Learn in v2

* Importance of **data structures (set)**
* Trade-off:

  * memory ↑ → time ↓
* Step toward optimization

---

## 🚀 Why This Version Matters

This version teaches:

> “How to reduce cost of operations without changing logic”

---

## 🔥 Word: **Optimization Step**

**Meaning:** improving one part of system without redesigning everything
