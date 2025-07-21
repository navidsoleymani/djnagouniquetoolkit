import pytest
from djangouniquetoolkit.models import UsernameModel
from djangouniquetoolkit.services.get_unique_username import get_unique_username


@pytest.mark.django_db
def test_username_generation_creates_unique_value():
    """
    Test the unique username generation functionality.

    Steps:
    1. Generate a username and verify it is stored in the database.
    2. Confirm that the generated username is a non-empty string.
    3. Generate another username and assert it differs from the first,
       ensuring uniqueness of consecutive generations.
    """
    username = get_unique_username()

    # Verify the username is saved in the database
    assert UsernameModel.objects.filter(id=username).exists()

    # Check that the username is a non-empty string
    assert isinstance(username, str)
    assert len(username) > 0

    # Generate a second username and ensure it is unique
    another = get_unique_username()
    assert username != another
