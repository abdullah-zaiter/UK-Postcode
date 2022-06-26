import argparse
from postcode.validator import validation_types, Validator
from postcode.formatter import Formatter

parser = argparse.ArgumentParser(usage="script.py [-h] [-v TYPE VALUE] [-f]",
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-v', '--validate', nargs=2, type=str,
                    help=f"""First value is which part of postcode you want to validate and Second value is the value.
First value can be anyone of the following values: {', '.join(map(str, validation_types))}
Second value can be any string you want to match against the selected type"""
                    )

parser.add_argument('-f', '--format',  type=str, help="The postcode string to format")

args = parser.parse_args()


def handle_validation(validation_type,  value):
    if validation_type in validation_types:
        validation_func = getattr(Validator, f"is_valid_{validation_type}")
        result = validation_func(value)
        if result:
            print(f"{value} is a valid {validation_type}")
        else:
            print(f"{value} is NOT a valid {validation_type}")
    elif not args.format:
        parser.error(f"Incorrect validation type, should be one of the following: {', '.join(map(str, validation_types))}")


def handle_formatting(string_to_format):
    try:
        postcode = Formatter.from_string(string_to_format)
        print(postcode)
    except ValueError:
        print(f"{string_to_format} is NOT a valid postcode to format")


if __name__ == "__main__":
    if not (args.validate or args.format):
        parser.error('No action requested, add --validate or --format')

    if args.validate:
        handle_validation(*args.validate)

    if args.format:
        handle_formatting(args.format)

