# Long Distance Relationship Transformer

A python script that simultaneously applies a series of transformations to a sequence of symbols given a set of rules.

## `transformer.py`

### `class Symbol`

A `Symbol` is a single object that has two properties: `color` and `shape`. The `color` and `shape` properties are enums that can be accessed from the `Color` and `Shape` classes.

A `Symbol` is allowed to have an `Any` color or shape. This is represented by the `Color.Any` and `Shape.Any` enums.

### `class Word`

A `Word` is a sequence of `Symbol`s. It is represented as a list of `Symbol`s.

The `transform` method takes an initiator `Symbol`, a predicate function that takes a `Symbol` and returns a boolean, a direction `Direction`, a function that applies a transformation to a given `Symbol`, and an optional predicate function that takes a `Symbol` and returns a boolean. The `transform` method applies any valid transformations that it finds in place.

## Usage

```python
from transformer import *

# Create a Word
w = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# create an initiator symbol
initiator = Symbol(Color.ANY, Shape.SQUARE)
# create a terminator function that returns true if the symbol is black
terminator = lambda symbol: symbol.is_color(Color.BLACK)
# define a direction
direction = Direction.RIGHT
# create an output function that changes the shape of the symbol to a triangle
output = lambda symbol: symbol.change_shape(Shape.TRIANGLE)
# create a condition function that returns true if the symbol is a circle
condition = lambda symbol: symbol.is_shape(Shape.CIRCLE)

# apply the transformation
w.transform(initiator, terminator, direction, output, condition)

# word is now [BLACK_SQUARE, WHITE_CIRCLE, BLACK_TRIANGLE, WHITE_CIRCLE, BLACK_CIRCLE]
```