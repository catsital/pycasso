#!/usr/bin/env python

import argparse
import logging

from pycasso.unscramble import Canvas

log = logging.getLogger("pycasso.cli")

def main():
    parser = construct_parser()
    args = parser.parse_args()
    if not args.mode:
        log.error(
            "No mode specified: you need to specify the "
            "mode to scramble or unscramble an image."
        )
        raise SystemExit
    if not args.seed:
        log.warning(
            "No seed specified: this will automatically use "
            "the current system time."
        )
    if not args.output:
        log.warning(
            "No output found: appending base file name to current "
            "working directory."
        )
    if args.output.endswith('/'):
        log.warning(
            "No file name found: appending base file name to "
            "specified directory."
        )
    img = Canvas(
        args.image,
        slice_size=args.num,
        seed=args.seed,
    )
    img.export(
        mode=args.mode,
        path=args.output
    )

def construct_parser():
    parser = argparse.ArgumentParser(
        prog="pycasso",
        description="Split image into tiles and scramble/unscramble it with seed",
        epilog="Report bugs and make feature requests at "
               "https://github.com/catsital/pycasso/issues",
        add_help=False,
    )

    required = parser.add_argument_group("Required")
    required.add_argument("image", help="Path to image file.")
    required.add_argument("mode", help="Modes available: scramble, unscramble")

    optional = parser.add_argument_group("Optional")
    optional.add_argument(
        "-n",
        "--num",
        type=int,
        default=5,
        help="Size of tiles to slice an image."
    )
    optional.add_argument(
        "-s",
        "--seed",
        type=str,
        default=None,
        help="Seed to use to scramble or unscramble an image."
    )
    optional.add_argument(
        "-o", "--output",
        default="",
        help="Output file name and format."
    )

    info = parser.add_argument_group("Info")
    info.add_argument("-h", "--help", action="help", help="Display this screen."),
    info.add_argument("-v", "--version", action="version", help="Show program version.", version="%(prog)s 1.1.2")

    return parser

if __name__ == "__main__":
    main()
