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
    st.markdown("""
<script>
let moonboard = document.createElement('div');
moonboard.classList.add('.moonboard')

// let moonboard = document.querySelector('.moonboard');

let selected_holds = [];

/* * * * * * * * * * * * * * * * * * * * * * 

                DOM CREATION 

* * * * * * * * * * * * * * * * * * * * * */

for (let i = 0; i < 20; i++) {
    let row = document.createElement('div');
    row.classList.add(`row-${i}`);
    for(let j = 0; j < 10; j++) {
        let btn = document.createElement('button');
        btn.classList.add(`hold`);
        btn.classList.add(`btn-${i}-${j}`);

        // let buttonLabel = buttonMapping[i][j];
        // let buttonLabel = `button-${i}-${j}`;
        let buttonLabel = 'hold';

        btn.textContent = buttonLabel;
        // if (Array.from('1234567890+-*/').includes(buttonLabel)) { // numbers and operations
        //     btn.addEventListener('click', () => appendDisplayValue(buttonLabel));
        // }

        row.appendChild(btn);
    }
    moonboard.appendChild(row);
}
</script>
                """, unsafe_allow_html=True)
    # st.markdown(f'<div class="moonboard">', unsafe_allow_html=True)
    # for i in range(n):
    #     for j in range(m):
    #         st.markdown(f'<input type="checkbox"> {i},{j} </input>', unsafe_allow_html=True)
    
    # st.markdown("""
    #              <style>
    #              input {
    #                 padding: 100px; 
    #              }
    #              </style>
    #              """, unsafe_allow_html=True)   
    # st.markdown(f'</div>', unsafe_allow_html=True)

st.title("Route Grader")

# buttonGrid(20, 10)
buttonGrid2(2,2)