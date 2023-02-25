import argparse
from api import update, fibonacci

d = """
API test application using a combination
of pure Python functions and additional
helper modules written in Rust.
This application uses several Python libraries to
create a colorful commandline app with example
functionality implemented in Rust
"""

def main():
    parser = argparse.ArgumentParser(
        description=d
    )

    parser.add_argument(
        "-n", "--app-name",
        action="store",
        required=False,
        help="App name to use for update download simulation"
    )

    parser.add_argument(
        "-r", "--rust-arg",
        action="store",
        required=False,
        help="""
        Tell us your name! This `string` value gets passed
        to the `say_hello` function implemeted in Rust.
        """
    )

    parser.add_argument(
        "-f", "--fibonacci",
        action="store",
        required=False,
        help="""
        Calculation time comparison among python, numba,
        cython and rust(pyo3).
        """
    )

    args = parser.parse_args()

    if args:
        if args.app_name:
            update.checkVersion(args.app_name)
        if args.rust_arg:
            rp.say_hello(args.rust_arg)
        if args.fibonacci:
            fibonacci.fib_calc(int(args.fibonacci))
    else:
        parser.print_usage()

if __name__ == '__main__':
    main()
