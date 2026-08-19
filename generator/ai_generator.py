import json
from openai import OpenAI
import os
from dotenv import load_dotenv
from generator.prompts import create_prompt

def generate_test_cases(feature,count,test_case_type):
    load_dotenv()

    client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
    try:
        response = client.responses.create(
        model="gpt-5.5",
        input=create_prompt(feature, count, test_case_type)
    )
    except Exception as e:
        print(f"Error calling OpenAI api: {e}")
        exit()
    output = response.output_text
    print(output)

    # Convert String to JSON
    try:
        test_cases = json.loads(output)
    except json.JSONDecodeError:
        print("Invalid JSON received from AI")
        print(output)
        exit()
    return test_cases
