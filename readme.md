# Simple Order Testing Project

## Overview

This is a demo project created to learn and practice automated testing using Flask, HTML, API testing with pytest, and browser testing with Selenium.  
It contains a simple order form built with Flask and HTML, stores data in a local SQLite database, and includes automated tests for both API endpoints and browser interactions.

The main goal of this project is to demonstrate practical skills in automated testing, backend development, and CI pipelines, with a focus on quality assurance processes.

---

## Technologies Used

- Python
- Flask
- SQLite
- requests
- pytest
- Selenium
- GitHub Actions

---

## Tests Included

- **Standalone CRUD test**: covers full lifecycle of an order (POST → GET → PUT → PATCH → DELETE) using fixtures
- **Modular API tests**: independent tests for POST, GET, PUT, PATCH, and DELETE operations
- **Combined Selenium + API tests**: Selenium submits order form and API verifies data in the database
- **Parameterized API tests**: testing with multiple input values

---

## CI Pipeline

- Installs dependencies
- Runs linting with flake8
- Starts Flask server
- Executes automated tests on push, pull request, or scheduled time

---

## How to Run Tests

To run tests, follow these steps:

1. Clone the repository:  
   `git clone https://github.com/michalbelicka/simple_order.git`

2. Change into the project directory:  
   `cd simple_order`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Create the database:  
   `python create_db.py`

5. Start the Flask server:  
   `python app.py`

6. Run the tests:  
   `pytest -v`

---

## What I Learned

While working on this project, I followed a step-by-step approach to develop my skills:

- Learned **HTML basics** to create and structure the order form
- Learned the basics of **Flask** to create a simple backend application
- Created and integrated a **SQLite database** to store order data
- Implemented **pytest fixtures** for setup and cleanup between tests
- Developed **automated API tests** for POST, GET, PUT, PATCH, and DELETE methods
- Combined **Selenium and API testing** for end-to-end scenarios
- Set up a **CI pipeline with GitHub Actions** to automate testing

---

## Future Improvements

- Add **basic validation criteria** in the Flask backend (for example, checks for name format, valid email, positive quantity)
- Once validations are in place, add **edge case and negative tests** to verify how the system handles invalid or missing input
- Include **screenshots or logs** for Selenium tests for easier debugging
- Create **manual test cases** documenting expected behavior of the order form
- Improve the front-end design to make the order form more user-friendly and visually appealing
- Improve **README and documentation** with examples and test instructions
