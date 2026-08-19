import streamlit as st
from generator.ai_generator import generate_test_cases
from generator.excel_writer import save_to_excel

# Title name
st.title("🤖 AI Test Case Generator")

# Enter the feature
feature = st.text_input("Enter feature name:")
st.write(feature)

# Select the test case type
test_case_type = st.selectbox("Select test case type:",
                            [ "Functional", 
                              "Regression", 
                              "Smoke", 
                              "Sanity",
                              "API",
                              "UI",
                              "Security",
                              "Perfomance",
                              "Database"
                              ],
                              index=None,
                              placeholder="Choose a test case type"
                              )

st.write(test_case_type)

# Enter the count of test cases
count = st.number_input("Enter the number of test cases:",
                        min_value=1,
                        max_value=100,
                        value=10
                        )

st.write(count)

# Button to generate test cases(calling the function)
generate = st.button("🚀 Generate Test Cases")
if generate:
    with st.spinner("Generating AI test cases"):
        test_cases = generate_test_cases(
            feature, count, test_case_type)
        st.success("✅ Test cases generated successfully!")
        st.dataframe(test_cases)

        # Saving the test cases to file(calling the function)
        filename = save_to_excel(test_cases, feature)
        with open(filename, "rb") as file:

            #download button
            st.download_button(
                label="📥 Download test cases",
                data=file,
                file_name=f"{feature}_Testcases.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )