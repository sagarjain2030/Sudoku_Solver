from flask import request, jsonify, render_template
from .solver import solve_sudoku  # Import your Sudoku solving logic

def init_app(app):
    @app.route("/")
    def index():
        return render_template("sudoku.html")

    @app.route("/solve", methods=["POST"])
    def solve():
        data = request.json
        grid = data.get("grid", [])
        print("Grid:", grid)

        # Validate the grid
        if not grid or len(grid) != 9 or any(len(row) != 9 for row in grid):
            return jsonify({"success": False, "error": "Invalid Sudoku grid!"})

        # Solve the Sudoku
        solved_grid = solve_sudoku(grid)
        # if solved_grid:
        #     return jsonify({"success": True, "grid": solved_grid})
        # else:
        #     return jsonify({"success": False, "error": "No solution found!"})
