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
    markdown_str = ''
    for row in range(n):
        for col in range(m):
            markdown_str += '<input type="checkbox"></input>'
    markdown_str = f'<div class="moonboard">{markdown_str}</div>'
    st.markdown(markdown_str, unsafe_allow_html=True)
    st.markdown("""
                <style>
                .moonboard {
                    display: grid;
                    grid-gap: 10px;
                    grid-template-columns: repeat(10, 1fr);
                    grid-template-rows: repeat(20, 1fr);
                }
                
                input {
                    width: 50px;
                    height: 50px;
                }
                </style>
                """,unsafe_allow_html=True)

st.title("Route Grader")

# buttonGrid(20, 10)
buttonGrid2(20,10)