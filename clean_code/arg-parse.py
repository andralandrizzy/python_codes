import argparse

def fib_number(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        return a
def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("v", "--verbose", action = "store_true")
    group.add_argument("q", "--quit", action = "store_true")
    parser.add_argument("num", help = "The fibonacci number you wish to calculate.", type = int)
    parser.add_argument("o", "--output", help = "Output result to a file.", action = "store_true")

    args = parser.parse_args()
    
    result = fib_number(args.num)
    if args.verbose:
        print("The " + str(args.num) + "the fibonacci number is " + str(result))
    elif args.quit:
        print(result)
    else:
        print("Fib(" + str(args.num) + ") = " + str(result) )

if __name__ == "__Main__":
    Main()