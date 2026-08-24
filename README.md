# AI-Powered Test Case Generator

An AI-powered QA utility that generates structured test cases from feature
requirements using the OpenAI API.

## Features

- Generate test cases dynamically using OpenAI API
- Prompt engineering for structured test-case generation
- JSON-based response processing
- Export generated test cases to Excel
- Streamlit UI for feature selection and generation

## Tech Stack

- Python
- OpenAI API
- Streamlit
- OpenPyXL
- python-dotenv

## How It Works

1. Select a feature requirement.
2. The application sends the requirement to the OpenAI API.
3. The configured prompt generates structured test cases.
4. The response is processed and displayed.
5. Test cases can be exported to Excel.

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

   pip install -r requirements.txt

4. Create a `.env` file and add your OpenAI API key:

   OPENAI_API_KEY=your_api_key_here

5. Run the application:

   streamlit run app.py

## Project Structure

ai-test-case-generator/
├── app.py
├── generator
├── output
├── requirements.txt
├── .venv
├── .gitignore
└── README.md
