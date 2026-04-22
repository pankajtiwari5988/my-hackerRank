"""Basic hello world example."""


# pylint: disable=too-few-public-methods
class HelloWorld:
    """A simple class to print hello world."""

    def say_hello(self):
        """Prints hello world message."""
        print("Hello, World!")


if __name__ == "__main__":
    obj = HelloWorld()
    obj.say_hello()