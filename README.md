# Trends Fetcher

This Flask application fetches trending Twitter topics by country and classifies them into sectors using the OpenAI API.

## Prerequisites

- Git
- Python 3
- Pip

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hamza-dri/Trends-Fetcher.git
    ```

2. Navigate into the repository directory

3. Install `pipenv`:
    ```bash
    pip install pipenv
    ```

4. Install the dependencies using `pipenv`:
    ```bash
    pipenv install
    ```

### Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your OpenAI API key to the `.env` file:
    ```plaintext
    OPENAI_API_KEY='sk-ff14851qsfsfqsdfFDSQFDs26451fsfqsf' 
    ```

    (this is a template, use your actual key)

### Running the App

1. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

2. Start the Flask application:
    ```bash
    flask run
    ```

    or

    ```bash
    python app.py
    ```

