from math import factorial as fact
from fractions import Fraction


# Binomial Expansion Class
class BinomialExpansion:
    def __init__(self, args: dict[str]):
        """Initialize class"""
        self.verify_arguments(args.get("exp"))          # verify arguments
        args_array = args.get("exp").split()            # split arguments
        self.args = self.extract_variables(args_array)  # extract variables

    def expand(self):
        """Expand expression"""
        n = self.args.get("n")
        if n > 18:
            print("Cannot expand expressions raised to more than 18")
            exit(1)  # terminate

        a = self.args.get("a")
        b = self.args.get("b")
        operand = self.args.get("operand")

        res = []
        for k in range(self.args.get("n")+1):
            term = []
            variables = []
            scaler = self.combination(n, k)
            resolved_a = self.resolve(a, n-k)
            resolved_b = self.resolve(b, k)

            # get the powers of x
            if len(resolved_a) > 1:
                variables.append(resolved_a[1])
            if len(resolved_b) > 1:
                variables.append(resolved_b[1])

            coefficient = scaler * resolved_a[0] * resolved_b[0]  # the coefficient

            # display as fraction
            if "." in str(coefficient):
                term.append(Fraction(coefficient))
            else:
                term.append(coefficient)

            # prevent displaying x^0 or x^1
            if n-k != 0:
                if sum(variables) == 1:
                    term.append(f"x")
                else:
                    term.append(f"x^{sum(variables)}")

            else:
                term.append("")

            res.append(f"{term[0]}{term[1]}")

            if operand == "-":
                if k % 2 == 0:
                    res.append("-")
                else:
                    res.append("+")
            else:
                res.append("+")

        res.pop()  # remove redundant operand
        print("\nExpansion:",  " ".join(res))

    @staticmethod
    def resolve(term: str, power: int):
        """Resolve the term into constant and variable parts"""
        res = []
        terms = term.split("x")
        res.append(pow(float(Fraction(terms[0])), power))
        if len(terms) == 2:
            res.append(power)

        return res

    @staticmethod
    def combination(n: int, r: int):
        """Return the combination of n in r"""
        return fact(n) / (fact(r) * fact(n - r))

    @staticmethod
    def verify_arguments(args: [str]):
        """Verify input arguments"""
        required_chars = {'(', ')', '^'}
        if len(args) < 3 or not all(char in args for char in required_chars):
            if '+' not in args or '-' not in args:
                print("[ERR]: invalid expression encountered")
                exit(1)  # terminate

    @staticmethod
    def extract_variables(args: [str]):
        """Extract variables from the args"""
        args_half = args[2].split(")")
        return {
            "operand": args[1],
            "a": args[0][1:],
            "b": args_half[0],
            "n": int(args_half[1][1:])
        }
