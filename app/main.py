import streamlit as st
import json
from app.ai_checker import evaluate
from utils.file_loader import load_all_mysteries

st.set_page_config(layout = "wide")

mysteries = load_all_mysteries("data/mysteries.json")
total_mysteries = len(mysteries)

if "mystery_index" not in st.session_state: 
    st.session_state.mystery_index = 0      

# Getting the current mystery now
mystery = mysteries[st.session_state.mystery_index]

st.title("🕵️ Murder Mystery AI Game")
col1, col2 = st.columns([1,1])

with col1:
    st.header("Case File")
    st.subheader(mystery['title'])
    st.markdown(f"**Description**\n{mystery['description']}")
    st.markdown(f"**Suspects:** {'. '.join(mystery['description'])}")
    st.markdown("**Clues**")
    for clue in mystery["clues"]:
        st.markdown(f"- {clue}")

with col2:
    st.header("Clue Video")
    st.video(mystery["video"])

st.markdown("----")
user_input = st.text_area("Enter your detective theory below:")

if st.button("Submit Theory"):
    with st.spinner("Evaluating your theory..."):
        response = evaluate(mystery, user_input)
        st.markdown("### AI Verdict")
        st.success(response)

if st.button("Next Mystery"):
    st.session_state.mystery_index = (st.session_state.mystery_index + 1) % total_mysteries
    st.experimental_rerun()