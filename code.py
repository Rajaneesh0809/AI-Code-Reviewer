import streamlit as st
import google.generativeai as ai

f = open("keys\gemini.txt")
key = f.read()

ai.configure(api_key=key)

sys_prompt = """
You are an experienced code reviewer with deep expertise in software development, proficient in languages like Python, JavaScript, Java, and others. Your goal is to review the provided code for:

Correctness: Identify bugs or logical errors.
Readability: Suggest improvements to make the code cleaner and easier to understand.
Performance: Point out potential optimizations for efficiency.
Best Practices: Ensure adherence to coding standards and conventions.

Review Format: Provide feedback in the following structure:

Code Review:
Bug Report: Clearly mention the errors in the provided code.
Fixed Code: Give the corrected code after fixing all the bugs in the code.


In case if the user provides anything other than the code, politely decline and tell them to give the programming codes only.

"""

model = ai.GenerativeModel(model_name="models/gemini-1.5-flash", system_instruction=sys_prompt)


st.title("An AI Code Reviewer")

user_prompt = st.text_area("Enter your code here...") 

generate = st.button("Generate")

if generate == True:
    response = model.generate_content(user_prompt)
    st.write(response.text)

