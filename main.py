import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]
st.title("The Rizzler")
st.write("Welcome to The Rizzler, a pickup line generator using OpenAI's API")

name = st.text_input("What's their name?:")
fact = st.text_input("What's a fact about them?:")
gender = st.selectbox("What's their gender:", ["Male", "Female"])
option = st.selectbox("What kind of pickup line are you looking for?:", ["Clever", "Humorous", "Forward", "Cheesy", "Cute"])

prompt = (f"generate a {option} pickup line for someone named {name} who is {gender}. a fact about them is  {fact}.")
completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
pickup_line = completions.choices[0].text

st.write("Here is your pickup line:")
st.write(pickup_line)