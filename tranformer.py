# Author: Malek Azadegan

from enum import Enum

# Color enum class. Has black, white, and any attributes.
class Color(Enum):
    BLACK = 1
    WHITE = 2
    ANY = 3

# Shape enum class. Has triangle, square, circle and any attributes.
class Shape(Enum):
    TRIANGLE = 1
    SQUARE = 2
    CIRCLE = 3
    ANY = 4

# Direction enum class. Has left and right.
class Direction(Enum):
    LEFT = 1
    RIGHT = 2

# class Symbol. Has color and shape attributes.
class Symbol:
    def __init__(self, color: Color, shape: Shape):
        self.color = color
        self.shape = shape
    
    # returns true if the given color matches the color of the symbol.
    def is_color(self, color: Color):
        return self.color == color

    # returns true if the given shape matches the shape of the symbol.
    def is_shape(self, shape: Shape):
        return self.shape == shape

    # changes the shape of the symbol to the given shape.
    def change_shape(self, shape: Shape):
        self.shape = shape
    
    # changes the color of the symbol to the given color.
    def change_color(self, color: Color):
        self.color = color

    # returns true if the given shape and color matches the shape and color of the symbol.
    def is_color_shape(self, color: Color, shape: Shape):
        return self.is_color(color) and self.is_shape(shape)

    # to string method.
    def __str__(self):
        return f"<Symbol(color={self.color}, shape={self.shape})>"
    
    # equality method.
    def __eq__(self, other):
        if not isinstance(other, Symbol):
            return False
        return self.color == other.color and self.shape == other.shape

# class Word. Has list of symbols.
class Word:
    def __init__(self, symbols: list[Symbol]):
        self.symbols = symbols
    
    # to string method.
    def __str__(self):
        return f"<Word(symbols={[s.__str__() for s in self.symbols]})>"

    # equality method.
    def __eq__(self, other):
        if not isinstance(other, Word):
            return False
        if len(self.symbols) != len(other.symbols):
            return False
        for i in range(len(self.symbols)):
            if self.symbols[i] != other.symbols[i]:
                return False
        return True
    
    # pretty print method. Extracts the color and shape of each symbol and prints them in a nice format.
    def pretty_print(self):
        for s in self.symbols:
            print(f"Color: {s.color.name}, Shape: {s.shape.name}")

    # finds the indices of all symbols that match the given color and shape.
    def find(self, color: Color, shape: Shape):
        indices = []
        # if the color is any and shape is not any, add all indices of symbols that match the shape.
        if color == Color.ANY and shape != Shape.ANY:
            for i in range(len(self.symbols)):
                if self.symbols[i].is_shape(shape):
                    indices.append(i)
        # if the shape is any and color is not any, add all indices of symbols that match the color.
        elif shape == Shape.ANY and color != Color.ANY:
            for i in range(len(self.symbols)):
                if self.symbols[i].is_color(color):
                    indices.append(i)
        # if the color and shape are not any, add all indices of symbols that match the color and shape.
        else:
            for i in range(len(self.symbols)):
                if self.symbols[i].is_color_shape(color, shape):
                    indices.append(i)
        return indices
            

    # transforms the word according to the given initiator, terminator, direction, and condition.
    def transform(self, initiator: Symbol, terminator_predicate: callable, direction: Direction, output: callable, condition_predicate: callable = lambda _: True):
        # find the indices of all symbols that match the initiator.
        initiator_indices = self.find(initiator.color, initiator.shape)
        # holds the indices of all affected symbols.
        affected_indices = []
        
        # if the direction is right...
        if direction == Direction.RIGHT:
            # look to the right of each initiator index.
            for i in initiator_indices:
                for j in range(i + 1, len(self.symbols)):
                    # if the symbol at index j matches the terminator...
                    if terminator_predicate(self.symbols[j]):
                        # if the condition is true for the symbol at index j...
                        if condition_predicate(self.symbols[j]):
                            # add i to the affected indices
                            affected_indices.append(i)
                        break
        
        # transforms all affected symbols.
        for i in affected_indices:
            output(self.symbols[i])