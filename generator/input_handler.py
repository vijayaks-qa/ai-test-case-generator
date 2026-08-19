def get_feature_name(): 
    while True:
        feature = input("Enter the feature name:").strip()

        if feature:
            return feature
        
        print("Feature name can not be empty...")

def get_test_case_count():
    while True:
        try:
            count = int(input("Enter number of test cases:"))
            if count > 0:
                break
            else:
                print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    return count

def get_test_case_type():
    while True:
        test_case_type = input(
            "Enter test case type (Functional, Regression, Smoke, Sanity, API, UI, Security, Performance, Database): "
        ).strip()

        valid_types = ["Functional", "Regression", "Smoke", "Sanity","API","UI",
                       "Security", "Perfomance","Database"]

        if test_case_type.capitalize() in valid_types:
            return test_case_type.capitalize()

        print("Invalid test case type. Please choose from:")
        print(", ".join(valid_types))

    