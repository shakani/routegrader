import streamlit as st 
import streamlit.components.v1 as components
import pandas as pd
from df_parser import parse
import pickle
import linear_model
from linear_model import DictEncoder
from linear_model import LabelEncoder


st.title("Route Grader")

grade = st.button("Grade Route")

df = pd.DataFrame([{f"col-{col}" : False for col in range(11)} for row in range(18)])
edited_df = st.data_editor(df)

with open('linear_model.pickle', 'rb') as handle:
    linear_model = pickle.load(handle)
with open('label_pipeline.pickle', 'rb') as handle:
    label_pipeline = pickle.load(handle)

if grade:
    output = parse(edited_df)
    df_input = pd.DataFrame({'holds' : [output]})
    pred = linear_model.predict(df_input)
    n_pred = label_pipeline[]
    st.markdown(pred)