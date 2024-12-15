// JavaScript functions for Sudoku Solver

function clearGrid() {
    // Clear all cells
    const cells = document.querySelectorAll(".cell");
    cells.forEach(cell => cell.value = "");
}

function solveSudoku() {
    // Collect grid data
    const grid = [];
    for (let i = 0; i < 9; i++) {
        const row = [];
        for (let j = 0; j < 9; j++) {
            const cell = document.getElementById(`cell-${i}-${j}`);
            row.push(cell.value ? parseInt(cell.value) : 0);
        }
        grid.push(row);
    }

    // Send grid data to the backend for solving
    fetch("/solve", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ grid })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Populate the grid with the solved puzzle
            const solvedGrid = data.grid;
            for (let i = 0; i < 9; i++) {
                for (let j = 0; j < 9; j++) {
                    const cell = document.getElementById(`cell-${i}-${j}`);
                    cell.value = solvedGrid[i][j] || "";
                }
            }
        } else {
            alert("No solution found for the given Sudoku!");
        }
    })
    .catch(err => {
        console.error("Error solving Sudoku:", err);
        alert("An error occurred while solving the Sudoku. Please try again.");
    });
}
