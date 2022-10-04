# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys
import operator

# this file allows for a basic calculator to be used when calling the function,
# you can pass 2 numbers with a basic operator

# since the operator is given as a string, we want to convert this to a usable
# operator so we build a dict containing most of them
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}
def main():
    """Implement the calculator"""
    # we retrieve the arguments
    num1, num2, operator = int(sys.argv[1]), int(sys.argv[3]), str(sys.argv[2])
    # we retrieve the operator chosen using the dict of operators
    # and perform the expression
    return ops[operator](num1, num2)

if __name__ == "__main__":
    print(main())
