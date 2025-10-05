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

- **Pure API tests** with pytest (GET and POST requests)
- **Combined Selenium + API test**: Selenium sends form data, and API verifies it in the database
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
- Developed **automated API tests** for GET and POST methods
- Combined **Selenium and API testing** for end-to-end scenarios
- Set up a **CI pipeline with GitHub Actions** to automate testing

---

## Future Improvements

- Extend the Flask backend with **PUT**, **PATCH**, and **DELETE** endpoints
- Add API tests for these methods using **requests** and **pytest**
- Create manual **test cases** for the order form (positive and negative scenarios)
- Add screenshots showing successful form submissions for documentation
