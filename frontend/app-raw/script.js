const gridContainer = document.querySelector('.grid-container');
const gridSizeInPixels = 580;
const nSizeMax = Math.round(Math.sqrt(gridSizeInPixels));

// grid resize
function gridGenerator(nSize) {
    let grid = [];

    for (let i = 0; i < nSize; i++) {
        grid[i] = [];
    }

    for (let i = 0; i < nSize; i++) {
        let row = document.createElement('div'); // row container
        row.classList.add('row')
        for (let j = 0; j < nSize; j++) {
            grid[i][j] = document.createElement('div');
            grid[i][j].classList.add('cell');
            // grid[i][j].addEventListener('click', () => grid[i][j].style.backgroundColor = 'blue');
            grid[i][j].addEventListener('click', () => grid[i][j].classList.toggle('cell-selected'));
            row.appendChild(grid[i][j]);
        }
        gridContainer.appendChild(row);
    }

    // const gridSizeInPixels = 540;
    const cellSizeInPixels = Math.round(gridSizeInPixels / nSize);
    let cells = document.querySelectorAll('.cell');
    cells.forEach((cell) => {
    cell.style.height = `${cellSizeInPixels}px`;
    cell.style.width = `${cellSizeInPixels}px`;
    });
}

function deleteGrid() {
    while (gridContainer.firstChild) {
        console.log('Deleting');
        gridContainer.removeChild(gridContainer.firstChild);
    }
}

function resizeGrid() {
    deleteGrid();
    let nSize = nSizeMax;
    while (nSize >= nSizeMax) { // get a reasonable grid size
        nSize = parseInt(prompt('Enter new grid size: '));
    }
    gridGenerator(nSize);
}

function eraseGrid() {
    let cells = document.querySelectorAll('.cell');
    cells.forEach((cell) => {
    cell.style.backgroundColor = 'white';
    });
}

// button listeners
const resizeButton = document.querySelector('#resize');
resizeButton.addEventListener('click', () => resizeGrid());

const eraseButton = document.querySelector('#erase');
eraseButton.addEventListener('click', () => eraseGrid());

// main
gridGenerator(16);