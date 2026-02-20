import streamlit as st
import json
import os
import random
import time


TIME_PER_QUESTION = 30  # seconds

# LOAD QUESTIONS 
def load_questions():
    questions = []
    folder = "questions"

    for file in os.listdir(folder):
        if file.endswith(".json"):
            with open(os.path.join(folder, file), "r") as f:
                questions.extend(json.load(f))

    random.shuffle(questions)
    return questions

# GRADE FUNCTION 
def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"

# SESSION STATE INIT 
if "questions" not in st.session_state:
    st.session_state.questions = load_questions()
    st.session_state.q_no = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.selected = None

st.title("Quiz Application")

# QUIZ LOGIC 
if st.session_state.q_no < len(st.session_state.questions):

    q = st.session_state.questions[st.session_state.q_no]

    elapsed = time.time() - st.session_state.start_time
    remaining = TIME_PER_QUESTION - int(elapsed)

    st.write(f"### Question {st.session_state.q_no + 1}")
    st.write(q["question"])

    st.session_state.selected = st.radio(
        "Choose an option:",
        q["options"],
        key=st.session_state.q_no
    )

    st.warning(f"Time left: {remaining} seconds")

    if remaining <= 0:
        st.error("Time's up!")
        st.session_state.q_no += 1
        st.session_state.start_time = time.time()
        st.rerun()

    if st.button("Next"):
        if st.session_state.selected == q["answer"]:
            st.session_state.score += 1

        st.session_state.q_no += 1
        st.session_state.start_time = time.time()
        st.rerun()

else:
    
    total = len(st.session_state.questions)
    percentage = (st.session_state.score / total) * 100
    grade = get_grade(percentage)


    st.success(" Quiz Completed!")
    st.write(f"**Score:** {st.session_state.score} / {total}")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
