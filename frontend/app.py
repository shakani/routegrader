import streamlit as st 
import streamlit.components.v1 as components
import pandas as pd
        
st.title("Route Grader")

grade = st.button("Grade Route")

df = pd.DataFrame([{f"col-{col}" : False for col in range(10)} for row in range(20)])
edited_df = st.data_editor(df)

if grade:
    st.markdown(edited_df.values)