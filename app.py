from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import warnings 
warnings.filterwarnings("ignore")

# Load all the environment variables
load_dotenv()

# Configure genAI key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Create a function to load the Gemini model and get a response
def get_gemini_response(query, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], query])
    print(response.text)
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.commit()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        # st.error(f"An error occurred: {e}")
        rows = []
    finally:
        connection.close()
    return rows

# Define the prompt
prompt = ["""
    You are an expert in converting English questions to SQL code!
    The SQL database is named STUDENT and has the following columns: Name, Class, Section.
    For example,
    Example 1: How many entries of records are present?
    The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    Ensure that the SQL code in the response does not have ''' at the beginning or end of the response and does not contain the word 'sql' in the output.
"""]

# Streamlit app configuration
st.set_page_config(page_title="Data Retrieval from SQL Database Using gemini-pro")
st.header("Data Retrieval from SQL Database Using gemini-pro")

question = st.text_input("Input your question:", key='input')
submit = st.button("Submit")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    if response:
        results = read_sql_query(response, "Student.db")
        st.subheader("Output:")
        if results:
            for row in results:
                st.write(row)
        else:
            st.write("No results found or an error occurred.")
