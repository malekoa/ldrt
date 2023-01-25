from tranformer import Word, Symbol, Color, Shape, Direction

# initiator is a square with any color
initiator = Symbol(Color.ANY, Shape.SQUARE)
# terminator is a predicate function that returns true if the symbol is black
terminator = lambda symbol: symbol.is_color(Color.BLACK)
# direction is right
direction = Direction.RIGHT
# condition is a predicate function that returns true if the symbol is a circle
condition = lambda symbol: symbol.is_shape(Shape.CIRCLE)
# output is a function that turns the symbol into a triangle
output = lambda symbol: symbol.change_shape(Shape.TRIANGLE)

# w1 should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: black, white, black, white, black
w1 = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w1_expected should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: black, white, black, white, black
w1_expected = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w2 should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: black, white, white, white, black
w2 = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w2_expected should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: black, white, white, white, black
w2_expected = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w3 should follow the following pattern:
# shape: square, circle, square, circle, circle
# color: black, white, black, white, black
w3 = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# w3_expected should follow the following pattern:
# shape: square, circle, triangle, circle, circle
# color: black, white, black, white, black
w3_expected = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# w4 should follow the following pattern:
# shape: square, circle, square, circle, circle
# color: black, white, white, white, black
w4 = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# w4_expected should follow the following pattern:
# shape: triangle, circle, triangle, circle, circle
# color: black, white, white, white, black
w4_expected = Word([
    Symbol(Color.BLACK, Shape.TRIANGLE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.TRIANGLE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# w5 should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: white, white, black, white, black
w5 = Word([
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w5_expected should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: white, white, black, white, black
w5_expected = Word([
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w6 should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: white, white, white, white, black
w6 = Word([
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w6_expected should follow the following pattern:
# shape: square, circle, square, circle, triangle
# color: white, white, white, white, black
w6_expected = Word([
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# w7 should follow the following pattern:
# shape: square, circle, square, circle, circle
# color: white, white, black, white, black
w7 = Word([
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# w7_expected should follow the following pattern:
# shape: square, circle, triangle, circle, circle
# color: white, white, black, white, black
w7_expected = Word([
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# w8 should follow the following pattern:
# shape: square, circle, square, circle, circle
# color: white, white, white, white, black
w8 = Word([
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.SQUARE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# w8_expected should follow the following pattern:
# shape: triangle, circle, triangle, circle, circle
# color: white, white, white, white, black
w8_expected = Word([
    Symbol(Color.WHITE, Shape.TRIANGLE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.WHITE, Shape.TRIANGLE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.CIRCLE)
])

# Adjacency test:
# adj_word should follow the following pattern:
# shape: square, circle, triangle, square, triangle
# color: all black
adj_word = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.BLACK, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE),
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# adj_word_expected should follow the following pattern:
# shape: square, circle, triangle, circle, triangle
# color: black, black, black, white, black
adj_word_expected = Word([
    Symbol(Color.BLACK, Shape.SQUARE),
    Symbol(Color.BLACK, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE),
    Symbol(Color.WHITE, Shape.CIRCLE),
    Symbol(Color.BLACK, Shape.TRIANGLE)
])

# adjacency_initiator should be a black square
adjacency_initiator = Symbol(Color.BLACK, Shape.SQUARE)
# adjacency_terminator should be a predicate that returns true if the symbol is any color and any shape
adjacency_terminator = lambda symbol: True
# adjacency_direction should be Direction.RIGHT
adjacency_direction = Direction.RIGHT
# adjacency_output should be a function that turns the symbol into a white circle
def adjacency_output(symbol: Symbol):
    symbol.change_color(Color.WHITE)
    symbol.change_shape(Shape.CIRCLE)
# adjacency_condition should be a function that returns true if the symbol is a black triangle
adjacency_condition = lambda symbol: symbol.color == Color.BLACK and symbol.shape == Shape.TRIANGLE

# Test function that takes a word, initiator, terminator, direction, output,  condition, and expected word as parameters. The function should transform the word, and then check if the word is equal to the expected word. If the word is equal to the expected word, the function should print "Test passed". Otherwise, the function should print "Test failed".
def test(word: Word, initiator: Symbol, terminator: callable, direction: Direction, output: callable, condition: callable, expected_word: Word):
    # transform the word
    word.transform(initiator, terminator, direction, output, condition)
    # check if the word is equal to the expected word
    if word == expected_word:
        print("Test passed")
    else:
        print("Test failed")

# if name is main...
if __name__ == "__main__":
    # tests found on page 25 of the paper
    print("Tests found on page 25 of the paper:")
    # test w1
    test(w1, initiator, terminator, direction, output, condition, w1_expected)
    # test w2
    test(w2, initiator, terminator, direction, output, condition, w2_expected)
    # test w3
    test(w3, initiator, terminator, direction, output, condition, w3_expected)
    # test w4
    test(w4, initiator, terminator, direction, output, condition, w4_expected)
    # test w5
    test(w5, initiator, terminator, direction, output, condition, w5_expected)
    # test w6
    test(w6, initiator, terminator, direction, output, condition, w6_expected)
    # test w7
    test(w7, initiator, terminator, direction, output, condition, w7_expected)
    # test w8
    test(w8, initiator, terminator, direction, output, condition, w8_expected)

    # Adjacency test found on page 24 of the paper
    print("Adjacency test found on page 24 of the paper:")
    test(adj_word, adjacency_initiator, adjacency_terminator, adjacency_direction, adjacency_output, adjacency_condition, adj_word_expected)