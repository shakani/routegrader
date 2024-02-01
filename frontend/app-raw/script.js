let moonboard = document.querySelector('.moonboard');

for (let i = 0; i < 20; i++) {
    let row = document.createElement('div');
    row.classList.add(`row-${i}`);
    for(let j = 0; j < 10; j++) {
        let btn = document.createElement('button');
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