import random
import string

from djangouniquetoolkit.models import AlphabetModel
from .base import UBase


class Alphabet(UBase):
    """
    Unique alphabet generator service.

    Generates unique alphabetic strings composed of random uppercase and lowercase letters.
    The service ensures that each generated value is stored only once using the underlying model.

    Attributes:
        model (AlphabetModel): Django model used to store and track generated alphabet strings.
    """

    model = AlphabetModel

    def _get_alphabet(self) -> str:
        """
        Returns a single random ASCII alphabet character (uppercase or lowercase).

        Returns:
            str: A randomly chosen character from A–Z or a–z.
        """
        return random.choice(string.ascii_letters)  # equivalent to ascii_lowercase + ascii_uppercase

    def generator(self, alphabet: str = None, **kwargs) -> str:
        """
        Generates a new alphabetic string by appending a random character to the input.

        Args:
            alphabet (str, optional): The current partial string to extend. If None, a new character starts the string.
            **kwargs: Additional arguments (currently unused).

        Returns:
            str: A new alphabetic string candidate.
        """
        if alphabet is None:
            alphabet = self._get_alphabet()
        else:
            alphabet += self._get_alphabet()
        return alphabet


# Callable for external use: generates and returns a guaranteed unique alphabet string
get_unique_alphabet = Alphabet().execute
