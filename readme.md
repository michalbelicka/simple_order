# Simple Order Testing Project

## Overview

**Live Application:** https://belicka-orders-api.onrender.com

This is a test automation project focused on API testing, UI testing, and backend behavior using Flask, pytest, and Selenium.

The project tests a simple order management system that exposes both an HTML form and a REST API.
Automated tests cover CRUD operations and verify core backend behavior and responses.

API tests are implemented using pytest and Flask test client. They verify API endpoints by validating responses for CRUD operations (create, read, update, delete) and basic input checks.
Tests use an in-memory SQLite database to ensure isolation and independent test runs.

Selenium tests the deployed application on Render through a real browser. The test simulates a user filling out the order form and verifies that an order is successfully created by checking the returned order ID.

The application uses a PostgreSQL database hosted on Render for persistent data storage.

The main goal of this project is to demonstrate practical skills in automated testing, API testing, backend development, and CI/CD workflows.

---

## Technologies Used

- Python
- Flask
- HTML
- SQLAlchemy (ORM)
- PostgreSQL (Render)
- pytest
- Selenium
- GitHub Actions (CI/CD)

---

## Tests Included

- CRUD API tests
- Individual API endpoint tests
- Database behavior tests
- Parameterized API tests
- Selenium UI test against the deployed Render application

---

## CI/CD Pipeline

- Installs project dependencies
- Runs code quality checks with flake8
- Executes automated tests on push, pull request, and scheduled runs
- Automatically deploys the application to Render after successful CI pipeline execution

---

## How to Run Tests

To run tests, follow these steps:

1. Clone the repository:  
   `git clone https://github.com/michalbelicka/simple_order.git`

2. Change into the project directory:  
   `cd simple_order`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Run the tests:  
   `pytest -v`

---

## What I Learned

While working on this project, I improved my skills in backend development and test automation through a step-by-step approach:

- Learned **HTML basics** to build a simple order form interface
- Learned the fundamentals of **Flask** for building REST APIs and backend logic
- Worked with **SQLAlchemy and PostgreSQL** for persistent data storage
- Implemented **pytest-based API testing** for CRUD operations (POST, GET, PUT, PATCH, DELETE)
- Used **Flask test client** for fast and isolated API testing without external HTTP calls
- Built **Selenium UI tests** to simulate real user interactions on a deployed application
- Set up a **CI/CD pipeline using GitHub Actions and Render** for automated testing and deployment

---

## Future Improvements

- Add more robust **input validation in the Flask backend** (e.g. name constraints, quantity rules)
- Extend test coverage with additional **edge case and negative scenarios** for invalid inputs
- Improve **Selenium testing output** by adding screenshots or logs for better debugging
- Add **formal manual test cases** describing expected behavior of the application
- Improve the front-end design to make the order form more user-friendly and visually appealing
- Add **Docker support** to containerize the application and simplify deployment
