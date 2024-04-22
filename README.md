FastAPI Project
Overview

This repository contains a FastAPI project with CRUD operations for managing users. It includes endpoints for creating, reading, updating, and deleting user data. The project utilizes SQLAlchemy for database operations and Pydantic for data validation.
Files

    README.md: This file provides an overview of the project and instructions on how to set it up and run it.
    logs.log: This file contains logs of requests processed by the FastAPI application.
    models.py: This file defines the SQLAlchemy models used for database operations.
    routes.py: This file contains the FastAPI route definitions for handling HTTP requests.
    schemas.py: This file defines Pydantic schemas for data validation and serialization.
    tech.db: This is the SQLite database file used by the project to store user data.
    tests.py: This file contains unit tests for testing the endpoints defined in routes.py.

Setup

    Clone the repository to your local machine.
    Make sure you have Python installed (preferably version 3.7 or later).
    Install the required dependencies by running pip install -r requirements.txt.
    Ensure that the database is initialized by running python models.py.
    Start the FastAPI server by running uvicorn routes:app.

Usage

Once the FastAPI server is running, you can access the API documentation by navigating to http://localhost:8000/docs in your web browser. From there, you can test the various endpoints and perform CRUD operations on user data.
Tests

To run the unit tests, execute the command pytest tests.py. This will run the tests defined in tests.py and provide the results in the terminal.
