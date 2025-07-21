import random

from djangouniquetoolkit.models import UsernameModel
from .base import UBase


class Username(UBase):
    """
    Unique username generator service.

    This class generates unique usernames by selecting names from a predefined
    male/female name pool and appending digits when necessary. It ensures
    uniqueness by checking the database-backed `UsernameModel`.

    Attributes:
        model (UsernameModel): Django model for persisting and checking username uniqueness.
        MALE_NAMES (set): A set of common male first names.
        FEMALE_NAMES (set): A set of common female first names.
    """
    MALE_NAMES = {
        "James", "John", "Robert", "Michael", "William", "David", "Richard",
        "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew",
        "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua",
        "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward",
        "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric",
        "Stephen", "Jonathan", "Larry", "Justin", "Scott", "Brandon", "Benjamin",
        "Samuel", "Gregory", "Frank", "Alexander", "Raymond", "Patrick", "Jack",
        "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Henry", "Douglas",
        "Peter", "Nathan", "Zachary", "Walter", "Kyle", "Carl", "Arthur",
        "Gerald", "Jeremy", "Keith", "Roger", "Terry", "Lawrence", "Sean",
        "Christian", "Albert", "Joe", "Ethan", "Austin", "Jesse", "Willie",
        "Billy", "Bryan", "Bruce", "Jordan", "Ralph", "Roy", "Noah", "Dylan",
        "Alan", "Juan", "Wayne", "Billy", "Jordan", "Logan", "Alan", "Juan",
        "Gabriel", "Louis", "Russell", "Francis", "Billy", "Craig", "Tom",
        "Billy", "Harry", "Joe", "Adam", "Carl", "Marc", "Derek", "Carl",
        "Andre", "Jared", "Glenn", "Darren", "Brent", "Randy", "Luis",
        "Chad", "Jon", "Victor", "Melvin", "Glen", "Calvin", "Cody",
        "Nolan", "Lance", "Jorge", "Clifford", "Clinton", "Nathaniel",
        "Edwin", "Kurt", "Brady", "Grant", "Quentin", "Dustin", "Travis",
        "Philip", "Corey", "Lee", "Dean", "Bradley", "Ricky", "Ruben",
        "Marshall", "Trevor", "Julius", "Dale", "Tommy", "Trenton", "Billy",
        "Francisco", "Jared", "Kenny", "Clinton", "Brett", "Barry", "Caleb",
        "Derrick", "Corey", "Darryl", "Shawn", "Marc", "Randall", "Marvin",
        "Francisco", "Eddie", "Lionel", "Guillermo", "Alfred", "Sergio",
        "Erik", "Eduardo", "Dominic", "Oscar", "Ramon", "Gordon", "Ellis",
        "Troy", "Maurice", "Shane", "Jonathon", "Micheal", "Shaun", "Don",
        "Clayton", "Clint", "Cliff", "Abel", "Felix", "Lloyd", "Mitchell",
        "Spencer", "Oscar", "Clinton", "Marc", "Edgar", "Gavin", "Damon",
        "Brendan", "Dominick", "Noel", "Wesley", "Roland", "Dwayne", "Oliver",
        "Leonard", "Rodney", "Tomas", "Hector", "Mason", "Dean", "Eugene",
        "Russell", "Melvin", "Darren", "Calvin", "Cameron", "Allen", "Alvin",
        "Arnold", "Bernard", "Clayton", "Darryl", "Francisco", "Harrison",
        "Isaiah", "Jared", "Kelly", "Kirk", "Manuel", "Marc", "Marvin",
        "Nicolas", "Philip", "Quincy", "Roland", "Ronnie", "Shane", "Sterling",
        "Tracy", "Victor", "Wade", "Warren", "Wayne", "Zachary",
    }
    FEMALE_NAMES = {
        "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan",
        "Jessica", "Sarah", "Karen", "Nancy", "Lisa", "Margaret", "Betty",
        "Sandra", "Ashley", "Dorothy", "Kimberly", "Emily", "Donna", "Michelle",
        "Carol", "Amanda", "Melissa", "Deborah", "Stephanie", "Rebecca", "Sharon",
        "Laura", "Cynthia", "Kathleen", "Amy", "Shirley", "Angela", "Helen",
        "Anna", "Brenda", "Pamela", "Nicole", "Ruth", "Katherine", "Samantha",
        "Christine", "Emma", "Catherine", "Debra", "Virginia", "Rachel",
        "Janet", "Maria", "Heather", "Diane", "Julie", "Joyce", "Victoria",
        "Kelly", "Christina", "Lauren", "Joan", "Evelyn", "Olivia", "Judith",
        "Megan", "Cheryl", "Andrea", "Hannah", "Martha", "Jacqueline",
        "Molly", "Tiffany", "Teresa", "Rose", "Theresa", "Marilyn", "Beverly",
        "Denise", "Tammy", "Irene", "Jane", "Lori", "Kayla", "Marsha",
        "Annie", "Natalie", "Diana", "Abigail", "Julia", "Sophia", "Madison",
        "Isabella", "Mia", "Charlotte", "Amelia", "Evelyn", "Harper", "Luna",
        "Camila", "Gianna", "Elizabeth", "Eleanor", "Ella", "Avery", "Sofia",
        "Mila", "Aria", "Scarlett", "Penelope", "Layla", "Chloe", "Victoria",
        "Madeline", "Nora", "Addison", "Lucy", "Audrey", "Brooklyn", "Bella",
        "Claire", "Skylar", "Paisley", "Everly", "Anna", "Caroline", "Nova",
        "Genesis", "Emilia", "Kennedy", "Samantha", "Maya", "Willow", "Kinsley",
        "Naomi", "Aaliyah", "Elena", "Sarah", "Ariana", "Allison", "Gabriella",
        "Alice", "Madelyn", "Cora", "Ruby", "Eva", "Serenity", "Autumn", "Adeline",
        "Hailey", "Gianna", "Valentina", "Isla", "Eliana", "Quinn", "Nevaeh",
        "Ivy", "Sadie", "Piper", "Lydia", "Alexa", "Josephine", "Emery", "Julia",
        "Delilah", "Arianna", "Vivian", "Kaylee", "Sophie", "Brielle", "Clara",
        "Reagan", "Madeline", "Peyton", "Liliana", "Melanie", "Gianna", "Isabelle",
        "Eloise", "Sienna", "Natalia", "Rose", "Valeria", "Ellie", "Paislee",
        "Mackenzie", "Hazel", "Gabrielle", "Alexandra", "London", "Kylie",
        "Lilly", "Lauren", "Maria", "Morgan", "Melody", "Angelina", "Katherine",
        "Harmony", "Ada", "Lilith", "Vivienne", "Adalynn", "Anastasia", "Margot",
        "Piper", "Amaya", "Ximena", "Gia", "Norah", "Liliana", "Eliza",
        "Emerson", "Everleigh", "Melina", "Isabel", "June", "Valerie",
        "Callie", "Emilia", "Rachel", "Mya", "Daisy", "Arabella", "Gracie",
        "Ariella", "Remi", "Holly", "Adelyn", "Elliana", "Rowan", "Athena",
        "Sloane", "Jade", "Sage", "Alaia", "Genevieve", "Journey", "Kylee",
        "Esther", "Malia", "Zuri", "Tessa", "Blakely", "Amira", "Maggie",
        "Juliana", "Dakota", "Kira", "Lola", "Maisie", "Alina", "Mckenna",
        "Selena", "Rylee", "Cecilia", "Freya", "Adeline", "Brianna", "Elise",
        "Phoebe", "Lucia", "Remington", "Finley", "Hadley", "Jasmine",
        "Angel", "Rosemary", "Kelsey", "Paige", "Amari", "Noelle", "Cali",
        "Miriam", "Elena", "Jocelyn", "Adelaide", "Dakota", "Nina", "Elsie",
        "Luna", "Madilyn", "Emery", "Luna", "Saylor", "Serena", "Bridget",
        "Esme", "Aubree", "Kali", "Alana", "Zoe", "Talia", "Sienna", "Ember",
        "Sabrina", "Julianna", "Maya", "Makayla", "Nylah", "Catalina", "Alaina",
        "Teagan", "Kailani", "Camille", "Lena", "Ellie", "Arielle", "Mikayla",
        "Marley", "Amira", "Erin", "Alivia", "Sawyer", "Rosalie", "Ximena",
        "Kendall", "Lexi", "Maya", "Jade", "Nora", "Gia", "Brynlee", "Emerson",
        "Alayna", "Penny", "Hadley", "Ariel", "Cameron", "Camille", "Piper",
        "Payton", "Lilly", "Genevieve", "Kendra", "Camila", "Marina", "Reese",
        "Eden", "Dahlia", "Ada", "Anya", "Sierra", "June", "Lilly", "Maddison",
    }

    model = UsernameModel

    def _get_names(self, gender=None) -> set[str]:
        """
        Returns a set of names based on the specified gender.

        Args:
            gender (str, optional): Can be one of ['male', 'female', 'm', 'f', 0, 1, etc.]

        Returns:
            set[str]: A set of names matching the gender, or both if unspecified.
        """
        if gender and gender in [0, 'Female', 'F', 'female', 'f']:
            return self.FEMALE_NAMES
        elif gender and gender in [1, 'Male', 'M', 'male', 'm']:
            return self.MALE_NAMES
        return self.MALE_NAMES.union(self.FEMALE_NAMES)

    def generator(self, username: str = None, gender: str = None, **kwargs) -> str:
        """
        Generates a new username candidate.

        If no base username is provided, randomly selects a name from the
        appropriate gender pool. If a base name is given, appends a digit
        to create a new variation.

        Args:
            username (str, optional): Base username to build upon.
            gender (str, optional): Gender hint for name selection.
            **kwargs: Reserved for future use.

        Returns:
            str: A candidate username.
        """
        if username is None:
            names = self._get_names(gender)
            username = random.choice(list(names)).lower()
        else:
            username += str(random.randint(0, 9))
        return username


# Callable for external use: generates and stores a guaranteed unique username
get_unique_username = Username().execute
