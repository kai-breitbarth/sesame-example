# Django Magic Link Authentication Example

This Django project demonstrates an implementation of passwordless authentication using "magic links" sent via email. Utilizing the django-sesame library, this example allows users to log in by clicking a unique link sent to their email, bypassing the need for traditional username/password authentication.

## Features

- Passwordless authentication using email-based "magic links."
- Custom user model with email as the primary identifier.
- Function-based view to handle the generation and sending of magic links.
- Admin customization to support user management without requiring a username or password.

## Requirements

This project requires Django and django-sesame. All dependencies can be installed via pip using the provided `requirements.txt` file.
