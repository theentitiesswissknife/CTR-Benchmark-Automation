# domain_utils.py
# Handles user input for domain URLs, ensuring they are correctly formatted with the required
# HTTP/HTTPS prefix and trailing slash. This module is crucial for initializing domain-specific operations within the
# application.

def format_domain(domain=None):
    """
    Formats the domain to include 'https://' and ends with '/'.
    Args:
        domain (str): Optional. Domain name input, if not provided, prompts user.
    Returns:
        str: Formatted domain.
    """
    if domain is None:
        domain = input("Enter Domain name (with http/https): ")
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain
    if not domain.endswith('/'):
        domain += '/'
    return domain
