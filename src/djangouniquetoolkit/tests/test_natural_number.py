import pytest
from djangouniquetoolkit.models import NaturalNumberModel
from djangouniquetoolkit.services.get_unique_natural_number import get_unique_natural_number


@pytest.mark.django_db
def test_generate_unique_natural_number():
    """
    Tests generation of unique natural numbers.

    - Ensures that the generated number is saved in the database.
    - Verifies that consecutive calls produce different unique numbers.
    """
    number = get_unique_natural_number()

    # Check that the generated number exists in the database
    assert NaturalNumberModel.objects.filter(id=number).exists()

    # Generate a second unique number and verify it is different
    number2 = get_unique_natural_number()
    assert number != number2
