# Lab 04 — Python Data Structures & Clean Code

## Concepts Practiced
- Lists
- Tuples
- Dictionaries
- Sets
- Comprehensions
- `enumerate()`
- `zip()`
- Sorting and counting records
- Data structure selection
- Clean code
- File organization

## Tasks Completed
1. Lists
2. Aliasing vs Copying (including shallow vs deep copy)
3. Tuples (including tuples as dictionary keys)
4. Dictionaries
5. Sets
6. Comprehensions
7. `enumerate()` and `zip()`
8. Data Structure Selection
9. Prediction Analysis — Part A and Part B

## Data Structure Decisions
- Scenario A: List — order matters for evaluation sequence
- Scenario B: Tuple — image size is fixed and never changes
- Scenario C: Dictionary — named fields make config readable
- Scenario D: Set — unique labels only, no duplicates needed
- Scenario E: List of Dictionaries — many records with same fields
- Scenario F: Set — fast membership check and set difference

## Aliasing vs Copying
- Part A: both variables pointed to same list in memory
- Part B: .copy() created new list — original was safe
- Part C: .copy() only copied the outer list — inner dictionaries were still shared
- deepcopy() copied everything — raw data was fully protected

## Hashability
- Tuple can be a dictionary key because it is immutable and hashable
- List cannot be a key because it is mutable — its hash would change

## Sets vs Lists for Validation
- Sets express intent directly with union, intersection, difference
- Set membership checks are O(1) — much faster than list O(n)
- For 1,000,000 IDs, set lookup is nearly instant vs list is slow

## Clean-Code Refactoring
- Original code used x, y, z, d — unreadable names
- Refactored with meaningful names and constants
- Confirmed behavior by comparing Part A output with original
- Refactored version is easier to test and maintain

## Handling Incomplete Records
- Records missing required fields are skipped and their IDs reported
- Labels are normalized (stripped and lowercased) without mutating raw data

## Edge Cases Tested
- filter_by_confidence([]) → []
- average_confidence([]) → None
- confidence exactly 0.80 → included
- normalize_labels → raw data unchanged

## What I Found Difficult
- Understanding shallow vs deep copy difference

## What I Learned
- How to choose right data structure for each problem
- How to handle incomplete records
- How to normalize data without mutating originals

## AI Engineering Relevance
- Data structures organize preprocessing pipelines
- Clean code makes model configs readable
- Sets validate model output labels efficiently
- Dictionaries store model metadata and results

## AI Usage Log
### Tool Used
Claude & ChatGPT

### What I Asked
- Help writing and understanding each task

### What I Used
- Code structure and logic guidance

### What I Verified or Changed Myself
- Ran and tested every program myself