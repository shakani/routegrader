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

grade = st.button("Grade Route")

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