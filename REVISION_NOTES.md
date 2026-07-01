# Neetcode DSA Revision Notes

This file contains crisp revision notes, optimal approaches, key considerations, and collated doubts/mind maps for the problems solved on Neetcode.

---

## 🔗 Linked List Cycle Detection
  - Relative Speed (RS) is $2 - 1 = 1$. Distance $d$ decrements by exactly 1 each step, guaranteeing it hits 0:

---

## 🔗 Reorder Linked List
  - To find the middle use slow/fast pointers
  - Split into two halves
  - Reverse the second half.
  - Merge first and second halves alternately using a dummy node.
  - If `first` still has a node (odd-length list), append it.
- **Complexity**: Time: $O(N+M)$ while merging
