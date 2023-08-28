This is a web application built using Flask.

## Getting Started

To run the application locally and perform testing, follow the steps below.

### Prerequisites

-   Python 3.x
-   pip (Python package manager)

### Installation

1. Clone this repository to your local machine:
   `git clone https://github.com/canhhs91/simple-flask-app.git`

2. Navigate to the project directory:

`cd simple-flask-app`

3. Setup the virtual environment
   `python -m venv venv`
   `source venv/bin/activate`

4. Install the required packages using pip:

`pip install -r requirements.txt`

### Running the Application

1. Start the Flask development server by running the following command in the project directory:

`flask run`

The application will be accessible at http://127.0.0.1:5000/.

### Running test

1. Running test using pytest

`python -m pytest`

### Project Structure

The project is structured as follows:

-   app.py: Entry point for this Flask application.
-   db.py: Database setup and configuration.
-   config.py: Configuration settings for the application.
-   modules/: This directory contains individual modules of your application.
    -   module_name/: Each subdirectory is a module.
        -   tests/: Test files and suites for this module.
        -   controllers.py: Module-specific controller logic.
        -   models.py: Module-specific database models.
        -   routers.py: Module-specific route definitions.
        -   schemas.py: Pydantic schemas for data validation.
