import streamlit as st 
import streamlit.components.v1 as components
        
def buttonGrid(n: int, m: int) -> None:
    markdown_str = ''
    for row in range(n):
        for col in range(m):
            markdown_str += f'<input type="checkbox" id="hold-{row}-{col}" class="hold"></input>'
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
                    width: 20px;
                    height: 20px;
                }
                </style>
                """,unsafe_allow_html=True)

st.title("Route Grader")

if st.button('Grade This Route'):
    components.html("""<script>
                    
    let moonboard = document.querySelectorAll("input.hold");
    let selected_holds = [];
    for (let i = 0; i < moonboard.length; i++) {
        if (moonboard[i].check) {
            alert(i);
        }
    }
    
    alert(selected_holds);
    
                    
                    </script>""")

buttonGrid(20,10)