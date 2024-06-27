# -*- coding: utf-8 -*-

'''
    File name: server.py
    Purpose: Contains the server configuration to run our Dash application.
    Authors:
        - Yuashun Cui - 2404877
        - Samira Nazari - 2310647
        - Mohamad Hadi Ajami - 2227105
    Course: INF8808
    Python Version: 3.8

    This file provides the functionality to run a Flask server that serves the Dash application.
'''

from flask_failsafe import failsafe

# Define a failsafe decorator to create the Flask server
@failsafe
def create_app():
    """
    Gets the underlying Flask server from our Dash app.

    Returns:
        Flask app: The Flask server to be run.
    """
    # The import is inside the function to work with the failsafe mechanism
    from app import app  # pylint: disable=import-outside-toplevel
    return app.server


# Entry point to run the Flask server
if __name__ == "__main__":
    # Create and run the Flask app on port 8050 with debug mode enabled
    create_app().run(port="8050", debug=True)
