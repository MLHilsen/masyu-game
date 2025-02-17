import random
import tkinter as tk

# Grid size
ROWS = 5
COLS = 5

# Create a grid
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

def place_circles(grid, num_black, num_white):
    """
    Randomly place black and white circles on the grid.
    """
    cells = [(r, c) for r in range(ROWS) for c in range(COLS)]
    random.shuffle(cells)

    for i in range(num_black):
        r, c = cells[i]
        grid[r][c] = 'black'

    for i in range(num_black, num_black + num_white):
        r, c = cells[i]
        grid[r][c] = 'white'

def draw_grid(canvas, grid):
    """
    Draw the grid and circles on the Tkinter canvas.
    """
    cell_size = 40
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c * cell_size, r * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")

            if grid[r][c] == 'black':
                canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="black")
            elif grid[r][c] == 'white':
                canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="white")

def on_click(event, canvas, grid):
    """
    Handle user clicks on the grid.
    """
    cell_size = 40
    col = event.x // cell_size
    row = event.y // cell_size
    print(f"Clicked on cell: ({row}, {col})")

def main():
    """
    Main function to set up the Tkinter GUI and run the application.
    """
    # Place circles on the grid
    place_circles(grid, num_black=3, num_white=3)

    # Set up Tkinter
    root = tk.Tk()
    root.title("Masyu Puzzle")
    canvas = tk.Canvas(root, width=COLS * 40, height=ROWS * 40)
    canvas.pack()

    # Draw the grid and circles
    draw_grid(canvas, grid)

    # Bind click event
    canvas.bind("<Button-1>", lambda event: on_click(event, canvas, grid))

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()