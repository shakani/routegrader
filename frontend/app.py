import streamlit as st 
import streamlit.components.v1 as components
import pandas as pd
from df_parser import parse
        
st.title("Route Grader")

grade = st.button("Grade Route")

df = pd.DataFrame([{f"col-{col}" : False for col in range(11)} for row in range(18)])
edited_df = st.data_editor(df)

if grade:
    st.markdown(parse(edited_df))