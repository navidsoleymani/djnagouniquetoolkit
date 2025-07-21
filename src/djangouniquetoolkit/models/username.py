from django.db import models
from django.utils.translation import gettext_lazy as _


class Username(models.Model):
    """
    Represents a unique username string used for identification purposes.

    This model is used to store and ensure the uniqueness of usernames generated
    dynamically by the system. It can be applied to systems where programmatic
    username assignment is required (e.g., onboarding flows, anonymized identities,
    pseudonyms, etc.).

    Attributes:
        id (str): A unique username string. This field serves as the primary key.
    """

    id = models.CharField(
        verbose_name=_('ID'),
        primary_key=True,       # Treats 'id' as the primary key in the database table
        blank=False,            # Value must be provided on creation (not optional)
        null=False,             # Disallows NULL values at the database level
        unique=True,            # Ensures that all usernames are globally unique
        editable=False,         # Prevents this field from being edited in admin or forms
        db_index=True,          # Adds an index to optimize lookups
        max_length=255,         # Optional: consider specifying this for future safety
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the model instance.

        Returns:
            str: The unique username.
        """
        return str(self.id)

    class Meta:
        verbose_name = _('Username')           # Human-readable singular name (used in admin)
        verbose_name_plural = _('Usernames')   # Human-readable plural name (used in admin)
