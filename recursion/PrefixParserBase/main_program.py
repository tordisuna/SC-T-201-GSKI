import tokenizer
from tokenizer import Tokenizer

# throw/raise this exception if a
# division by zero occurs.
class DivisionByZero(Exception):
    pass

# IMPLEMENT HERE!!!! -----------------------------------------------------
def handle_expression(expression):
    pass
# This function is the actual recursive
# implementation of the prefix parser.
# The tokenizer is pass-by-object-reference
# so it will be the same instance of Tokenizer
# throughout the recursive run.
def prefix_parser_recursive(tokenizer, stack=list()):
    token = tokenizer.get_next_token()
    stack.append(token)
    symbols = {"*", "/", "+", "-"}
    if stack[-1] not in symbols:
        if stack[-2] not in symbols:
            return eval(stack[-2], stack[-3], stack[-1])
    if not token:
        return eval(a)
    total += handle_token(token)

    #print(token)  # debug line

# This function makes the tokenizer
# and then calls the recursive function.
# It is often necessary to make a separate
# recursive function that takes and returns
# particular values that don't match the
# proper functions parameters and return value.
def prefix_parser(str_statement):
    tokenizer = Tokenizer(str_statement)
    return prefix_parser_recursive(tokenizer)

# This is a tester function to test that
# the output and/or error message from the
# prefix_parser function are correct.
def test_prefix_parser(str_statement):
    str_print = str_statement.rstrip()
    try:
        str_print += " = " + str(prefix_parser(str_statement))
    except DivisionByZero:
        str_print += ": " + str("A division by zero occurred")
    print(str_print)

# A few hard coded tests
test_prefix_parser("+ 3 20")
test_prefix_parser("+ / 3 - 21 20 * 2 40")
test_prefix_parser("+ / 3 - 20 20 * 2 40")

# This must be a relative path from the folder that you have open
# in Visual Studio Code.  This particular path works if you open
# the folder PrefixParserBase directly
f = open("recursion/PrefixParserBase/prefix_statements.txt", "r")
for line in f:
    test_prefix_parser(line)
f.close()
