# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 00:35:52 2025

@author: Hemal
"""
import streamlit as st
import random

# Function to generate a math question
def generate_question(operation):
    if operation == "Multiplication":
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        question = f"{num1} * {num2}"
        answer = num1 * num2
    elif operation == "Division":
        num2 = random.randint(1, 9)
        num1 = num2 * random.randint(1, 9)
        question = f"{num1} / {num2}"
        answer = num1 / num2
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        if operation == "Addition":
            question = f"{num1} + {num2}"
            answer = num1 + num2
        elif operation == "Subtraction":
            question = f"{num1} - {num2}"
            answer = num1 - num2
    return question, answer

# Streamlit app layout
st.title("Math Wizard")

# Sidebar for operation selection
operation = st.sidebar.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Generate question button
if st.sidebar.button("Generate Question"):
    question, correct_answer = generate_question(operation)
    st.session_state.question = question
    st.session_state.correct_answer = correct_answer

# Display the question
if 'question' in st.session_state:
    st.write(f"Solve this: {st.session_state.question}")
    user_answer = st.number_input("Your Answer", format="%.2f")

    # Check the answer
    if st.button("Submit"):
        if round(user_answer, 2) == round(st.session_state.correct_answer, 2):
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is {st.session_state.correct_answer:.2f}")
