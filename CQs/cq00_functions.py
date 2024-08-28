"""This is a challenge question about functions."""

__author__ = "730759640"


def mimic(message: str) -> str:
    """This function will return the string input into it."""
    return message


def main() -> None:
    """This is the main function of the module."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
