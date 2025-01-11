import random
import string

from django.core.mail import send_mail
def generate_random_string(length=12):
    """
    Generates a random string of the given length.
    The string contains uppercase letters, lowercase letters, and digits.
    """
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits

    # Randomly select characters from the pool
    random_string = ''.join(random.choice(characters) for i in range(length))

    return random_string

# Example usage:

