# Simple order testing project

## Overview

This is a demo project for learning and practicing testing with **Flask, API, and Selenium**.  
The project contains a simple order form built with Flask, stores data in a local SQLite database, and includes automated tests for both API endpoints and browser interactions.  
The purpose of this project is to showcase my skills in automated testing, Flask development, and CI pipelines.

## Tests Included

- Pure API test with **pytest** (`GET` and `POST` requests)
- Combined Selenium + API test: Selenium sends form data, API checks that it is saved in the database
- API test with parametrize for different input values

## Important

- Uses fixtures for database cleanup
- CI pipeline with GitHub Actions:
  - Installs dependencies
  - Runs linting with flake8
  - Starts Flask server and runs tests automatically on push, pull request, or scheduled time
- Runs API and Selenium tests with pytest

## How to Run Tests

To run tests, follow these steps:

1. Clone this repository:  
   `git clone https://github.com/michalbelicka/simple_order.git`

2. Change into the project directory:  
   `cd simple_order`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Create your own database:  
   `python create_db.py`

5. Start the Flask server:  
   `python app.py`

6. Run the tests:  
   `pytest -v`
