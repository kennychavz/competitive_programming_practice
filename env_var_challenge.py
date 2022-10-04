# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    # production mode
    if os.environ.get('FLASK_ENV') == 'production':
        return "Starting in production mode..."
    # development mode
    elif os.environ.get('FLASK_ENV') == 'development':
        return "Starting in development mode..."
    # empty mode
    else:
        return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
