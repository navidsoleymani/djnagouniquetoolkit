import pytest
from djangouniquetoolkit.models import AlphabetModel
from djangouniquetoolkit.services.get_unique_alphabet import get_unique_alphabet


@pytest.mark.django_db
def test_alphabet_generation():
    """
    Tests that the generated alphabet string:
    - Is stored in the database.
    - Is a string.
    - Contains only alphabetic characters.
    """
    val = get_unique_alphabet()

    assert AlphabetModel.objects.filter(id=val).exists()
    assert isinstance(val, str)
    assert val.isalpha()
