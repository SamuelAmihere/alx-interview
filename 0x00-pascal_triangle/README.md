# 0x00-pascal_triangle

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
