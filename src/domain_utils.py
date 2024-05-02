# domain_utils.py
# Handles user input for domain URLs, ensuring they are correctly formatted with the required
# HTTP/HTTPS prefix and trailing slash. This module is crucial for initializing domain-specific operations within the
# application.

import re



import re

def is_valid_domain(domain):
    """
    Checks if the provided string is a valid domain name.
    Args:
        domain (str): The domain name to validate.
    Returns:
        bool: True if the domain is valid, False otherwise.
    """
    # Regular expression pattern to match domain name format
    pattern = r'^((https?:\/\/)?(www\.)?)[a-zA-Z0-9]+([-.][a-zA-Z0-9]+)*\.[a-zA-Z]{2,}(:[0-9]+)?([\/][\w-]+)*\/?$'
    return re.match(pattern, domain) is not None

def format_domain(domain=None):
    """
    Formats the domain to include 'https://' and ends with '/'.
    Args:
        domain (str): Optional. Domain name input, if not provided, prompts user.
    Returns:
        str: Formatted domain.
    """
    while True:
        if domain is None:
            domain = input("Enter Domain name (without http/https): ")

        # Format the domain
        if not domain.startswith(('http://', 'https://')):
            domain = 'https://' + domain
        if not domain.endswith('/'):
            domain += '/'

        # Validate the domain name
        if not is_valid_domain(domain):
            print("Invalid domain name. Please enter a valid domain.")
            domain = None
            continue

        return domain

