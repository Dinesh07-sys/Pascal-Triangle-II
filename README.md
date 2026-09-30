# Pascal Triangle II

A Python implementation for calculating a specific row of Pascal's Triangle using an iterative combination formula.

## Overview

Unlike generating the complete Pascal's Triangle, this approach targets one row directly.

The `getRow()` method starts with `1` and calculates subsequent values using the relationship between consecutive binomial coefficients:

```text
current = current × (rowIndex - col + 1) / col
```

The implementation performs the calculation using integer division (`//`).

## How It Works

The method begins with the first value of every Pascal row:

```python id="j4c7qy"
result: list[int] = [1]
current: int = 1
```

It then iterates through the requested row positions:

```python id="r8m2xp"
for col in range(1, rowIndex + 1):
```

For each position, the next value is calculated from the previous one:

```python id="q6n9vz"
current = current * (rowIndex - col + 1) // col
```

The calculated value is appended to the result:

```python id="w2f5ka"
result.append(current)
```

This recurrence avoids constructing all the rows before reaching the requested one.

## Example

The program requests:

```python id="s7d3mx"
rowIndex = 5
```

The fifth-indexed row of Pascal's Triangle would mathematically be:

```text
[1, 5, 10, 10, 5, 1]
```

However, the uploaded implementation currently contains:

```python id="p4r8cz"
return result
```

inside the `for` loop. As a result, the function returns after calculating only the first iteration rather than completing the entire row.

With the code exactly as uploaded, the returned result for `rowIndex = 5` is:

```text
[1, 5]
```

## Important Code Note

To generate the complete row, the `return result` statement would need to execute **after** the loop finishes.

Current structure:

```python id="a5v8qn"
for col in range(1, rowIndex + 1):
    current = current * (rowIndex - col + 1) // col
    result.append(current)
    return result
```

The early `return` prevents the remaining iterations from running.

## Algorithm

1. Start the result with `1`.
2. Set the current value to `1`.
3. Iterate through the positions of the requested row.
4. Calculate each next value from the previous value.
5. Append the calculated value.
6. Return the resulting row.

## Complexity

For a correctly completed row calculation:

| Metric | Complexity |
|---|---|
| Time | O(N) |
| Auxiliary Space | O(N) |

The method generates each value in the requested row directly rather than constructing previous rows.

## Running the Program

Run:

```bash
python "Pascal Triangle II.py"
```

The provided `main()` function uses `rowIndex = 5` and prints the result returned by `getRow()`.

## Key Concepts

- Pascal's Triangle
- Binomial coefficients
- Iterative recurrence
- Integer arithmetic
- Single-row generation
- Array/list construction
