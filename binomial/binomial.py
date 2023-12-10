# Binomial Expansion Class
class BinomialExpansion:
    def __init__(self, args):
        self.verify_arguments(args.get("exp"))          # verify arguments
        args_array = args.get("exp").split()            # split arguments
        self.args = self.extract_variables(args_array)  # extract variables

    @staticmethod
    def verify_arguments(args):
        required_chars = {'(', ')', '^'}
        if len(args) < 3 or not all(char in args for char in required_chars):
            if '+' not in args or '-' not in args:
                print("[ERR]: invalid expression encountered")
                exit(1)  # terminate

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
