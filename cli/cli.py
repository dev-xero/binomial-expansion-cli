# Import modules
import argparse
from binomial.binomial import BinomialExpansion


# CLI Class
class CLI:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Binomial Expansion CLI Tool")
        print("Binomial Expansion CLI tool")

        parser.add_argument("--exp", type=str, required=True, help="The expression to expand")
        args = vars(parser.parse_args())  # transform args to dict

        binomial = BinomialExpansion(args)
        binomial.expand()  # expand the binomial
