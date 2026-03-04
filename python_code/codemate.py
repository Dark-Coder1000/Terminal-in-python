import curses
from curses import wrapper
import os

def codeMate():
    fileToEdit = input("What file would you like to edit?: ").strip()
    
    # --- LOAD FILE CONTENT ---
    lines = [""]
    if os.path.exists(fileToEdit):
        with open(fileToEdit, "r") as f:
            # Read lines and strip trailing newlines so they don't double up
            content = [line.rstrip('\n') for line in f.readlines()]
            if content: lines = content

    def main(stdscr):
        curses.noecho()
        
        # Use the 'lines' list from the outer scope
        nonlocal lines 
        
        while True:
            stdscr.clear()
            max_h, max_w = stdscr.getmaxyx()
            
            stdscr.addstr(0, 0, f"Editing: {fileToEdit} (Ctrl+A to Save & Exit):", curses.A_REVERSE)

            # Display all lines (with basic scrolling protection)
            display_limit = min(len(lines), max_h - 4)
            for idx in range(display_limit):
                stdscr.addstr(idx + 2, 2, lines[idx])
            
            stdscr.addstr(display_limit + 2, 0, "-" * 20)

            # Position cursor at the end of the last line
            stdscr.move(display_limit + 1, len(lines[-1]) + 2)
            
            ch = stdscr.getch()

            if ch == 1: # Ctrl+A
                break
                
            elif ch == 10: # Enter
                if len(lines) < max_h - 5:
                    lines.append("")
                
            elif ch in (curses.KEY_BACKSPACE, 127, 8): # Backspace
                if len(lines[-1]) > 0:
                    lines[-1] = lines[-1][:-1]
                elif len(lines) > 1:
                    lines.pop()
            
            elif 32 <= ch <= 126: # Printable
                if len(lines[-1]) < max_w - 5:
                    lines[-1] += chr(ch)

        # --- SAVE TO FILE ---
        with open(fileToEdit, "w") as f:
            for line in lines:
                f.write(line + "\n")

    wrapper(main)
    print(f"File saved to {fileToEdit}")

