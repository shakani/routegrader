import streamlit as st

button_col, other_col= st.columns([1,3])

st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

with button_col:
    "*Modified gap:*"
    st.checkbox("text")
    st.checkbox("text1")
    st.checkbox("text2")

with other_col:
    "*Unmodified gap:*"
    st.checkbox("text4")
    st.checkbox("text5")
    st.checkbox("text6")

st.markdown("## A header")
st.markdown("🪄 This is a repeated sentence"*100)