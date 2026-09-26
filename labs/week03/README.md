# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

## Concepts Practiced
- Functions
- Scope
- Modules and imports
- `__name__ == "__main__"`
- Exception handling
- Debugging
- Classes and objects
- Refactoring

## Tasks Completed
1. Function Design
2. Scope
3. Modules
4. Exception Handling
5. Debugging Challenge
6. ScoreAnalyzer Class
7. Refactoring Task

## Debugging Notes
- Bug 1: total = score replaced total each time instead of adding
- Located by tracing the loop manually
- Fixed by changing to total += score
- Bug 2: condition order in classify was wrong
- Fixed by moving >= 85 before >= 50

## Exception Handling Test Cases
| Case | Input | Expected Result | Actual Result |
|------|-------|----------------|---------------|
| Valid | 80, 100 | 80.00% | 80.00% |
| Negative | -5, 100 | Error | Error |
| Exceeds | 120, 100 | Error | Error |
| Zero total | 80, 0 | Error | Error |

## Design Decisions
- Functions used for simple reusable logic
- Class used in Task 6/7 because scores need state and behavior together
- main.py coordinates workflow only

## What I Found Difficult
- Understanding module imports

## What I Learned
- How to organize code into modules
- How to handle exceptions properly
- How to use classes with attributes and methods

## AI Engineering Relevance
Modularity, debugging, exceptions, and OOP help build larger AI systems
by making code reusable, testable, and maintainable.

## AI Usage Log
### Tool Used
Claude & ChatGPT

### What I Asked
- Help writing and understanding each task

### What I Used
- Code structure and logic guidance

### What I Verified or Changed Myself
- Ran and tested every program myself