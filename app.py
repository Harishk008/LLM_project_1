import streamlit as st
import subprocess

# Streamlit app
st.title("SRM Syllabus Retrieval System")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Add Data", "Query Syllabus"])

if selection == "Home":
    st.write("Welcome to the SRM Syllabus Retrieval System.")
    st.write("Use this tool to query syllabus data using a language model.")

elif selection == "Add Data":
    st.header("Add Data")
    
    # Button to trigger database population
    if st.button("Add Data"):
        # Run the populate_database script using subprocess
        result = subprocess.run(['python', '/mnt/data/populate_database.py'], capture_output=True, text=True)
        st.write(result.stdout)
        if result.stderr:
            st.error(result.stderr)
        else:
            st.success("Database added successfully!")

elif selection == "Query Syllabus":
    st.header("Query Syllabus Data")
    
    query = st.text_input("Enter your query:")
    
    if st.button("Search"):
        if query:
            # Run the query_data script with the input query
            result = subprocess.run(['python', 'query_data.py', query], capture_output=True, text=True)
            st.write("Results:")
            st.write(result.stdout)
            if result.stderr:
                st.error(result.stderr)
        else:
            st.error("Please enter a query.")
