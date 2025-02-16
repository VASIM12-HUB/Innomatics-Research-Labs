import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown

genai.configure(api_key="AIzaSyBRHQUx1rdAKL8MkOxgE1oyg-S1lvcp1WE")
sys_prompt="""You are a helpful AI coding tutor for AI Code Reviewer.
Students will ask you doubts related to various topics in Coding which have mistakes to correct it.
Starting with a side heading named as "Code Review"
next line with "Bug Report" which is telling the mistake that student has made.
Then, you have to give the corrected code under the name "Fixed Code".
You are expected to reply in as much detail as possible.
Make sure to take examples while explaining a concept and make a side heading as "Explanation".
In case if a student ask any quesiton outside the Code related scope,
politely decline and tell them to ask the question from Coding domain only.
"""

model=genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)
st.title("AI Code Reviewer")
#st.markdown("<h1 style='color: white;'>AI Code Reviewer</h1>", unsafe_allow_html=True)
img_path="C:/Users/hp/Downloads/Innomatics/Generative AI Sample Project/img.jpg"
#st.image(img_path,use_column_width=True)
st.markdown(
  """
  <style>
    
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/rear-view-programmer-working-all-night-long_1098-18697.jpg?t=st=1739689552~exp=1739693152~hmac=a758de580c3c067072f9da74a8582ed630893ebaeec0334a99f228d64bfc66c3&w=826");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
      }
        /* Set the text color */
    .stTextArea, .stButton {
        color: violet !important;
        size: 20px;
      }
  </style>
  """,
  unsafe_allow_html=True

)
user_prompt=st.text_area("Enter your query: ",placeholder="Type your query here...")
btn_click=st.button("Generate Answer")

if btn_click==True:
  response=model.generate_content(user_prompt)
  st.write(response.text)