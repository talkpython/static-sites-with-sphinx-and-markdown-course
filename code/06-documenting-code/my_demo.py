class MyDemo:
    """ A *great* demo """

    def __init__(self, name):
        self.name = name

    def hello(self, greeting: str) -> str:
        """ The canonical hello world example.

        A *longer* description with some **RST**.

        Args:
            name: The person to say hello to.
        Returns:
            str: The greeting
         """
        return f"{greeting} {self.name}"
