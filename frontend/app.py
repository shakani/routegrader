import streamlit as st 

def buttonGrid(n: int, m: int) -> None:
    i = 0
    for col in st.columns([1] * m):
        with col:
            for j in range(n):
                # st.checkbox(f'button {i}, {j}')
                st.checkbox(label = 'button {i},{j}', key=(i,j), label_visibility="hidden")
        i += 1
        
def buttonGrid2(n: int, m: int) -> None:
    pass

st.title("Route Grader")

buttonGrid(20, 10)