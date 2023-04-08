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

## Installation
- Clone the project
```shell
git clone https://github.com/po4apo/mathExpressionHandler.git
```
- Go into project
```shell
cd ./mathExpressionHandler
```
- Build image
```shell
docker build -t math_expression_handler ./
```
- Run Container
```shell
docker run --rm -p 8000:8000 --name meh math_expression_handler:latest
```

