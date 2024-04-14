# 0x00-pascal_triangle


# Pascal's Triangle
<img src=https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif>

Pascal's Triangle is a triangular array of binomial coefficients. It's named after Blaise Pascal, a famous French Mathematician and Philosopher. 

Each number in the triangle is the sum of the two numbers directly above it. The triangle starts with a single '1' at the top, then two '1's in the next row, and subsequent rows are constructed by adding the number above and to the left with the number above and to the right, treating blank entries as 0.

## Properties

1. **Symmetry**: Each row of Pascal's Triangle is symmetric - the elements on the left mirror the elements on the right.

2. **Binomial Coefficients**: The `n`th row and `k`th column of Pascal's Triangle represent the coefficients in the binomial expansion of `(x+y)^n`.

3. **Fibonacci Sequence**: The sum of the numbers diagonally in Pascal's Triangle gives the Fibonacci sequence.

## Applications

1. **Combinatorics**: Pascal's Triangle is used in algebra for binomial expansions. Each row represents the coefficients in the expansion of a binomial equation.

2. **Probability**: In statistics, the rows of Pascal's Triangle are used to calculate combinations for probability problems.

3. **Computer Science**: In computer graphics, Pascal's Triangle is used to determine coefficients of Bezier curves.

4. **Number Theory**: Pascal's Triangle has several properties and contains many patterns of numbers, so it's used in various number theory problems.
# Pascal's Triangle Python Implementation

This Python function generates Pascal's Triangle up to `n` rows.

```python
def pascal_triangle(n: int) -> List[List[int]]:
```

## Parameters

- `n` (int): The number of rows of Pascal's Triangle to generate.

## Returns

- `List[List[int]]`: A list of lists representing Pascal's Triangle up to `n` rows.

## Description

The function first checks if `n` is an integer. If not, it raises a `TypeError`. If `n` is less than or equal to 0, it returns an empty list.

The function then initializes an empty list `pascal` to store the rows of the triangle.

It then starts a loop that runs `n` times. For each iteration:

- It initializes a list `row` with a single element 1.
- If `pascal` is not empty, it gets the last row of `pascal` and assigns it to `last_row`. It then extends `row` by adding the sum of each pair of consecutive elements in `last_row`, and appends 1 to `row`.
- It appends `row` to `pascal`.

Finally, it returns `pascal`, which represents Pascal's Triangle up to `n` rows.

## Example

```python
print(pascal_triangle(5))
```

Output:

```python
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```
```
This code block generates Pascal's Triangle for `n` rows, where `n` is a user-provided integer. The triangle is represented as a list of lists, where each inner list is a row of the triangle.
