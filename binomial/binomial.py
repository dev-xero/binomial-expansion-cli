# Binomial Expansion Class
class BinomialExpansion:
    def __init__(self, args):
        args = args.get("exp").split()            # remove whitespace
        self.args = self.extract_variables(args)  # extract variables

    @staticmethod
    def extract_variables(args):
        """Extract variables from the args"""
        args_half = args[2].split(")")
        return {
            "operand": args[1],
            "a": args[0][1:],
            "b": args_half[0],
            "n": args_half[1][1:]
        }

    def expand(self):
        print(self.args.get("b"))
