# 📘 Longest Consecutive Sequence — Brute Force Approach

## 🧠 Problem Understanding

Given an unsorted array of integers, find the **length of the longest consecutive sequence**.

* Consecutive means: `x, x+1, x+2, ...`
* Order in array does not matter
* Only length is required, not the sequence itself

---

## ⚙️ Approach (Brute Force)

For each number in the array:

1. Start from that number
2. Keep checking if next number exists (`current + 1`)
3. Continue until next number is missing
4. Count the length of this sequence
5. Track the maximum length

---

## 🔁 Logic Flow

```
For each number:
    start fresh
    move forward step-by-step
    stop when next number not found
    track length
```

---

## ⏱️ Complexity Analysis

### Time Complexity: **O(n²)**

* Outer loop → O(n)
* Inner lookup (`in nums`) → O(n)
* Total → O(n × n) = O(n²)

---

### Space Complexity: **O(n)**

* Using a set/list to store results or intermediate values

---

## ⚠️ Limitations

* Repeated work:

  * Same sequence is recalculated multiple times
* Slow lookup:

  * `in nums` takes O(n)
* No optimization for skipping unnecessary starts

---

## 🧠 Key Learning

* Learned how to:

  * Expand sequences step-by-step
  * Use stopping conditions
  * Track sequence length
* Understood difference between:

  * Pair checking ❌
  * Sequence building ✅

---

## 🚀 Status

✅ Brute force logic understood
⚠️ Needs optimization for performance

---

## 🔥 Word: **Foundation**

**Meaning:** the basic structure on which stronger systems are built

👉 This solution is your foundation. Optimization comes next.
