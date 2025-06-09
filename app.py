import streamlit as st
import json
import random
from interview_logic import evaluate_answer

# Load categorized questions
with open("questions.json", "r") as f:
    questions_by_category = json.load(f)

st.title("🎤 AI Interview Coach")
st.write("Practice behavioral questions and get instant feedback!")

# Initialize session state defaults
if "category" not in st.session_state:
    st.session_state.category = list(questions_by_category.keys())[0]  # default to first category

if "question" not in st.session_state:
    st.session_state.question = None

if "custom_question" not in st.session_state:
    st.session_state.custom_question = ""

if "history" not in st.session_state:
    st.session_state.history = []

# Category selector (moved to main page as you requested)
selected_category = st.selectbox(
    "Select Question Category",
    options=list(questions_by_category.keys()),
    index=list(questions_by_category.keys()).index(st.session_state.category),
    key="category_selector",
)

# If category changed, update and reset question & custom question
if selected_category != st.session_state.category:
    st.session_state.category = selected_category
    st.session_state.question = random.choice(questions_by_category[selected_category])
    st.session_state.custom_question = ""  # clear custom question when category changes

st.write(f"**Current Category:** {st.session_state.category}")

# Button to get new random question (resets custom question too)
if st.button("🎲 Get New Question"):
    st.session_state.question = random.choice(questions_by_category[st.session_state.category])
    st.session_state.custom_question = ""

# Custom question input (controlled via session_state)
custom_q = st.text_input(
    "📝 Or enter your own custom question:",
    value=st.session_state.custom_question,
    key="custom_question",
)

# Determine question to display (custom overrides random)
current_question = custom_q.strip() if custom_q.strip() else st.session_state.question

if current_question:
    st.subheader("🧠 Question:")
    if custom_q.strip():
        st.write(f"**Custom Question Input**")
    st.write(current_question)

    user_answer = st.text_area("💬 Your Answer:", height=150)

    feedback_styles = {
        "Detailed": "Provide a thorough and detailed analysis.",
        "Concise": "Give a brief and concise evaluation.",
        "Friendly": "Offer feedback in a friendly and encouraging tone."
    }

    selected_style = st.selectbox(
        "Choose Feedback Style",
        options=list(feedback_styles.keys()),
        index=0,  # default Detailed
        key="feedback_style_selector"
    )

    if st.button("🔍 Evaluate My Answer"):
        if not user_answer.strip():
            st.warning("Please enter your answer before evaluating.")
        else:
            with st.spinner("Analyzing..."):
                style_instruction = feedback_styles[selected_style]
                feedback = evaluate_answer(user_answer, style_instruction)
            st.session_state.history.append({
                "category": "Custom" if custom_q.strip() else st.session_state.category,
                "question": current_question,
                "answer": user_answer,
                "feedback": feedback,
                "feedback_style": selected_style
            })
            st.markdown("### 📊 Feedback:")
            st.markdown(feedback)

# Answer Archive with category filter
with st.sidebar.expander("📜 Answer Archive", expanded=False):
    categories = ["All"] + list(questions_by_category.keys()) + ["Custom"]
    filter_cat = st.selectbox("Filter by Category", categories, key="archive_filter")

    filtered_history = st.session_state.history
    if filter_cat != "All":
        filtered_history = [h for h in st.session_state.history if h["category"] == filter_cat]

    if filtered_history:
        for idx, record in enumerate(reversed(filtered_history)):
            style_info = f" ({record['feedback_style']})" if "feedback_style" in record else ""
            st.markdown(f"**Q{len(filtered_history) - idx} [{record['category']}] {style_info}: {record['question']}**")
            st.markdown(f"- **Your Answer:** {record['answer']}")
            st.markdown(f"- **AI Feedback:** {record['feedback']}")
            st.markdown("---")
    else:
        st.info("Your past answers will appear here after evaluation.")

def format_history_as_text(history):
    lines = []
    for i, record in enumerate(history, 1):
        style_info = f" ({record['feedback_style']})" if "feedback_style" in record else ""
        lines.append(f"**Q{len(filtered_history) - idx} [{record['category']}] {style_info}: {record['question']}**")
        lines.append(f"Your Answer:\n{record['answer']}")
        lines.append(f"AI Feedback:\n{record['feedback']}")
        lines.append("-" * 40)
    return "\n\n".join(lines)

# In your sidebar export button section
if st.sidebar.button("📥 Export All Answers as TXT"):
    full_text = format_history_as_text(st.session_state.history)
    st.sidebar.download_button(
        label="Download Answers as TXT",
        data=full_text,
        file_name="interview_answers.txt",
        mime="text/plain"
    )