from datetime import date
import bcrypt

class User(object):
    """A user who will use the dashboard and web application.
    Args:
        first_name (str): The first name of the person, required
        last_name (str): The last or family name of the person, required
        email (str): Email address, required
        password (str): Password, required
        dob (date): Date of birth, optional with default None if value isn't provided.
    Attributes:
        first_name (str): The first name of the person
        last_name (str): The last or family name of the person
        email (str): Email address
        hashed_password (bytes): Hash value of the password string
        dob (date): Date of birth
        _is_logged_in(bool): Login status
    Methods:
        create_full_name: Creates the full names by concatenating the first names and last name
        calculate_age: Calculates the age from the date of birth
        hash_password: Create a hashed value of the string password
        is_correct_password: Checks if the string password matches the hashed password
        is_logged_in: Checks login status of users
    """

    def __init__(self, first_name: str, last_name: str, email: str, username: str, password: str, dob: date = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.hashed_password = self.hash_password(password)
        self.dob = dob
        self._is_logged_in = False

    def __repr__(self):
        """ String representation of a user object """
        return f" {self.first_name} {self.last_name} {self.email} {self.username} {self.dob} {self._is_logged_in}"

    @property
    def create_full_name(self):
        """Creates the full name by combining first_name and last_name
        Returns:
            Returns the full name
        """
        return f'{self.first_name} {self.last_name}'

    @property
    def calculate_age(self):
        """Calculates age based on the current date and the date of birth
        Returns:
            age (str): The age based on the dob and today's date, or a message if the date of birth has not been set
        """
        if self.dob is None:
            return "Age not calculated, date of birth unknown"
        else:
            today = date.today()
            age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
            return age

    def hash_password(self, password):
        """ Creates a hashed password from the string
        The bcrypt.hashpw() function takes a byte encoded arg, the password string therefore needs to be encoded.
        Args:
            password (str): Password in string format
        Returns:
            None
        """
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    def is_correct_password(self, password):
        """ Checks whether the provided password string matches the hashed password
        The bcrypt.checkpw() function takes byte encoded args, the password string needs to be encoded.
        Args:
            password (str): The string value of the password as input by the user
        Returns:
            bool : True if there is a match and False if not
        """
        if bcrypt.checkpw(password.encode('utf-8'), self.hashed_password):
            return True
        else:
            return False

    @property
    def is_logged_in(self):
        return self._is_logged_in

    @is_logged_in.setter
    def is_logged_in(self, status: bool):
        """
        If the user is not logged in, log them in, otherwise log them out
        Note: this is not how we will implement login functionality for Flask but will suffice for this example
        :param status: Boolean
        :return: sets _is_logged_in to either True or False depending on the value passed
        """
        self._is_logged_in = status

    def login(self, username, password):
        """
        Query the database and check if the username and password match, if they do then the status changes to logged in
        Note: This is not how to handle login for Flask! Added here just to provide code for the unit testing activity
        """
        # Database query logic here, for now assume the userid and password are valid
        self.is_logged_in = True

    def logout(self):
        """
        Logs out a user if they are logged in
        Note: This is not how to handle logout for Flask! Added here just to provide code for the unit testing activity
        """
        self.is_logged_in = False

