# Math expression handler

## Description
This is an api for processing mathematical expressions.

## Limitations
The expression allows numbers, variable names, signs of arithmetic operations, exponentiation (including non-integer) ^, functions LG (decimal logarithm), then LN (natural logarithm), trigonometric functions sine, cosine, tan, ASIN, acos, Atan.

## Example request
```json
{
    "expression": "4-2*a/(5*x-3)",
    "variables": {
        "a": 2.5,
        "x": 0
    }
}
```

