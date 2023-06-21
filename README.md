# the-last-algorithms-course-you-need-primegean
Code from The Last Algorithms Course You'll Need

# 1. Basics

## Big O Time Complexity

### What is Big O
- categorize your algorithm based on how it responds to changes in the size of the input data set
- categorize your algorithm time or memory requirements based on input
- Not meant to be an exact measurement
  - Not tell you how many cpu cycles it takes
  - Generalize the growth of your algorithm
- describe the growth of the algorithm
- Example:
  - When someone says -> O(N) -> algorithm will grow linearly based on input
  - Why O(N) -> it will loop each element in the array

### Why do we use it?
- help use make decisions about what data structures and algorithms to use

### Important Concepts

- growth is with respect to the input
- constants are dropped. because big O describe the growth of the algorithm. 
  - constant becomes irrelevant as the input grows
  - because we're not trying to
    - get exact time
    - get how many units of CPU we need to use
  - it's how does it grow. know generally
- worst case is usually the way we measure
- Example:

| N     | O(10N) | O(N ^ 2)  | Description  |
|-------|--------|-----------|--------------|
| 1     | 10     | 1         |              |
| 5     | 50     | 25        |              |
| 100   | 1000   | 10000     | 10x bigger   |
| 1000  | 10000  | 1000000   | 100x bigger  |
| 10000 | 100000 | 100000000 | 1000x bigger |

### Practical vs theorical differences
- just because N is fater than N ^ 2, doesn't mean it's always faster for smaller input
- Remember, we drop constant 

### Big O consider worst case
- Example

```
function sum_char_codes(n: string): number {
    let sum = 0;
    for (let i = 0; i < n.length; ++i) {
        const charCode = n.charCodeAt(i);
        // Capital E
        if (charCode === 69) {
            return sum;
        }

        sum += charCode;
    }

    return sum;
}
```

- the worst case 
  - we don't find E
  - we find E, but at the end of the array

# 2. Search

## Linear Search & Kata Setup