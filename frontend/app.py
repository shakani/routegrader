import streamlit as st 
import streamlit.components.v1 as components
import pandas as pd
from df_parser import parse
import pickle
import linear_model
from linear_model import DictEncoder
from linear_model import LabelEncoder

from grader import convert_grade


st.title("Route Grader")
github_url = "https://github.com/shakani/"
repo_url = "https://github.com/shakani/routegrader"
st.markdown(f"\xa9 2024 [Sami Hakani]({github_url})")

grade = st.button("Grade Route")

with st.sidebar:
    st.title('Understanding Your Grade')
    st.markdown(f"""
    Click on the checkboxes to indicate the holds in your Moonboard route. \n
    Click on the "Grade Route" button to receive your grade. \n
    Routes are graded on the French (Fontainebleau) Grading Scale (e.g. 7A) plus an interpolation factor indicating how close it is to the next level up.
    For example, a grade of "7A plus 50%" indicates that the route is halfway between 7A and 7A+. \n
    Be sure to star [the repo]({repo_url}) on GitHub!
                """)


df = pd.DataFrame([{f"{chr(ord('A')+col)}" : False for col in range(11)} for row in range(18)])
edited_df = st.data_editor(df)

with open('linear_model.pickle', 'rb') as handle:
    linear_model = pickle.load(handle)
with open('label_pipeline.pickle', 'rb') as handle:
    label_pipeline = pickle.load(handle)

if grade:
    output = parse(edited_df)
    df_input = pd.DataFrame({'holds' : [output]})
    pred = linear_model.predict(df_input)
    n_pred = label_pipeline['scaler'].inverse_transform(pred)[0][0]
    n_pred = convert_grade(n_pred)
    st.info(n_pred)