import random

from djangouniquetoolkit.models import NaturalNumberModel
from .base import UBase


class NaturalNumber(UBase):
    """
    Unique natural number generator service.

    This service generates unique non-negative integers by progressively appending
    random digits to the candidate number. It ensures uniqueness by checking against
    stored values in the associated model.

    Attributes:
        model (NaturalNumberModel): Django model used to persist and check uniqueness.
    """

    model = NaturalNumberModel

    def generator(self, nn: int = None, **kwargs) -> int:
        """
        Generates a new natural number candidate.

        If no input is given, it starts with a random digit between 0–9.
        If a previous number is passed, appends a new digit to the end.

        Args:
            nn (int, optional): Previous numeric value to build upon.
            **kwargs: Reserved for future use.

        Returns:
            int: A new natural number candidate.
        """
        if nn is None:
            nn = random.randint(0, 9)
        else:
            nn = int(f'{nn}{random.randint(0, 9)}')
        return nn


# Callable for external use: generates and stores a guaranteed unique natural number
get_unique_natural_number = NaturalNumber().execute
