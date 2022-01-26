#!/usr/bin/env python

import argparse
import logging

from pycasso.unscramble import Canvas

log = logging.getLogger("pycasso.cli")


def main():
    try:
        parser = construct_parser()
        args = parser.parse_args()
        if not args.seed:
            log.warning(
                "No seed specified: this will automatically use "
                "the current system time."
            )
        if args.output.endswith('/'):
            log.warning(
                "No file name found: appending base file name to "
                "specified directory."
            )
        if args.n:
            width, height = args.n

        img = Canvas(
            args.input,
            slice_size=(width, height),
            seed=args.seed
        )
        img.export(
            mode=args.mode,
            path=args.output,
            format=args.format
        )

    except Exception as error:
        parser.error(error)


def construct_parser():
    parser = argparse.ArgumentParser(
        prog="pycasso",
        description="Split image into tiles and "
                    "scramble/unscramble them with seed.",
        epilog="Report bugs and make feature requests at "
               "https://github.com/catsital/pycasso/issues",
        add_help=False,
    )

    required = parser.add_argument_group("Required")
    required.add_argument("input", help="Path to image file.")
    required.add_argument("output", help="Output image file.")
    required.add_argument(
        "mode",
        choices=["scramble", "unscramble"],
        help="Modes available: scramble, unscramble"
    )

    optional = parser.add_argument_group("Optional")
    optional.add_argument(
        "-n",
        type=int,
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        default=(5, 5),
        help="Size (width, height) of tiles to slice an image."
    )
    optional.add_argument(
        "-s",
        "--seed",
        type=str,
        default=None,
        help="Seed to use to scramble or unscramble an image."
    )
    optional.add_argument(
        "-f",
        "--format",
        type=str,
        default="png",
        help="Image format."
    )

    info = parser.add_argument_group("Info")
    info.add_argument(
        "-h",
        "--help",
        action="help",
        help="Display this screen."
    ),
    info.add_argument(
        "-v",
        "--version",
        action="version",
        help="Show program version.",
        version="%(prog)s 2.1.1"
    )

    return parser


if __name__ == "__main__":
    main()
