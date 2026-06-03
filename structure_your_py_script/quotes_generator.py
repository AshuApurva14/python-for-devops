#!/usr/bin/env python3

import random

from rich import print
from rich.text import Text

from quote_utils import get_quotes


def main():

    TEXT_STYLE="bold magenta"

    print(
        Text(
            "Welcome to the Inspirational Quote of the Day! Today's quote is:\n",
            style=TEXT_STYLE,
        )
    )

    random_quote = random.choice(get_quotes())

    print(
        Text(f"{random_quote['quote']} -- {random_quote['author']}", style=TEXT_STYLE)
    )


if __name__ == "__main__":
    main()
