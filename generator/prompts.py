def create_prompt(feature,count,test_case_type):
        prompt = f"""
        You are a Senior QA Engineer.

    Generate exactly {count} unique {test_case_type} manual test cases for the following feature: {feature} 

    Requirements:

    - Include positive scenarios
    - Include negative scenarios
    - Include boundary conditions
    - Include validation checks
    - Avoid duplicate scenarios
    - Use concise but meaningful descriptions

    Return ONLY valid JSON as an array.

Example format:

[
  {{
    "Test Case ID": "TC001",
    "Title": "Verify successful login",
    "Scenario": "Login with valid credentials",
    "Preconditions": "User account exists",
    "Test Steps": [
      "Open login page",
      "Enter valid username",
      "Enter valid password",
      "Click Login"
    ],
    "Expected Result": "User is logged in successfully",
    "Priority": "High",
    "Test Type": "Positive"
  }}
]

Generate exactly {count} UNIQUE test cases.
Do not repeat the example.
Replace all values with appropriate test case data.
Return ONLY JSON.
    ]

    Do not include markdown or explainations.
    """
        return prompt