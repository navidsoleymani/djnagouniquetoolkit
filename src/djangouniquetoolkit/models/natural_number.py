from django.db import models
from django.utils.translation import gettext_lazy as _


class NaturalNumber(models.Model):
    """
    Represents a unique natural number identifier.

    This model is designed to store a sequence of natural numbers (non-negative integers)
    where each value must be unique. Common use cases include generating user-friendly numeric IDs,
    invoice numbers, counters, or short codes that increment over time.

    Attributes:
        id (int): A unique positive big integer. This field is the primary key.
    """

    id = models.PositiveBigIntegerField(
        verbose_name=_('ID'),
        primary_key=True,       # Makes 'id' the primary key in the table
        blank=False,            # Field must be provided during creation
        null=False,             # Value cannot be NULL in the database
        unique=True,            # Ensures no duplicate values across records
        editable=False,         # Field is immutable via admin and forms
        db_index=True,          # Adds an index for efficient querying
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the model instance.

        Returns:
            str: The numeric ID as a string.
        """
        return str(self.id)

    class Meta:
        verbose_name = _('Natural Number')           # Singular name for admin UI
        verbose_name_plural = _('Natural Numbers')   # Plural name for admin UI
