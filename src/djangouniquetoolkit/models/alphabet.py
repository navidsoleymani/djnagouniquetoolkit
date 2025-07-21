from django.db import models
from django.utils.translation import gettext_lazy as _


class Alphabet(models.Model):
    """
    Represents a unique alphabetic string used as an identifier.

    This model stores individual or composed alphabetic values, typically
    used in cases where a unique string-based identifier is needed (e.g., short tokens,
    character-based slugs, or symbolic representations).

    Attributes:
        id (str): A unique alphabetic string (up to 255 characters). This is the primary key.
    """

    id = models.CharField(
        verbose_name=_('ID'),
        primary_key=True,       # Ensures this field is the primary identifier in the database
        blank=False,            # Field must be provided (not blank)
        null=False,             # Field cannot be NULL in the database
        unique=True,            # Enforces uniqueness at the database level
        editable=False,         # Prevents editing this field in Django admin or forms
        db_index=True,          # Adds an index for faster lookup
        max_length=255,         # Limits the maximum length of the string
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the model instance.

        Returns:
            str: The alphabetic ID.
        """
        return str(self.id)

    class Meta:
        verbose_name = _('Alphabet')             # Human-readable singular name (used in admin)
        verbose_name_plural = _('Alphabets')     # Human-readable plural name (used in admin)
