import abc


class UBase:
    """
    Abstract base class for generating and storing unique values.

    Subclasses must implement the `generator` method to define the logic for generating a value.
    The `execute` method handles checking if the value already exists in the database,
    and retries until a unique one is found and stored.

    Attributes:
        model (models.Model): A Django model class with a unique 'id' field.
    """

    model = None  # Must be set in subclasses to a Django model with a unique 'id' field

    def in_storage(self, x):
        """
        Checks whether the given value already exists in the database.
        If it doesn't exist, creates and stores it.

        Args:
            x: The candidate value to check.

        Returns:
            bool: True if the value already existed, False if it was newly stored.
        """
        exists = self.model.objects.filter(id=x).exists()
        if not exists:
            self.model.objects.create(id=x)
        return exists

    @abc.abstractmethod
    def generator(self, x=None, **kwargs):
        """
        Abstract generator method to produce the next candidate value.

        This method must be implemented in each subclass and should
        return a unique candidate value (not yet verified).

        Args:
            x: (Optional) Previous value to build upon.
            **kwargs: Additional context-specific parameters.

        Returns:
            Any: A candidate unique value.
        """
        pass

    def execute(self, **kwargs):
        """
        Main execution loop for generating a guaranteed unique value.

        It repeatedly generates candidate values and checks the database
        until a new, unused value is found and stored.

        Args:
            **kwargs: Arguments to be passed to the `generator` method.

        Returns:
            Any: A unique value that has been stored in the database.
        """
        x = self.generator(**kwargs)
        while self.in_storage(x):
            x = self.generator(x, **kwargs)
        return x
