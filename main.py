from generator.excel_writer import save_to_excel
from generator.ai_generator import generate_test_cases
from generator.input_handler import *

# Inputs
feature = get_feature_name()
count = get_test_case_count()
test_case_type = get_test_case_type()   

# Generating the test case
test_cases = generate_test_cases(feature, count,test_case_type)

# Create a Excel workbook
save_to_excel(test_cases, feature)