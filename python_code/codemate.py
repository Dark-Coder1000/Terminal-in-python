import curses
from curses import wrapper
import os

def codeMate():
    fileToEdit = input("What file would you like to edit?: ").strip()
    
    # --- INITIAL STATE ---
    lines = [""]
    top_line = 0   # Camera offset
    cursor_y = 0   # Y position in the file
    cursor_x = 0   # X position on the current line

    if os.path.exists(fileToEdit):
        with open(fileToEdit, "r") as f:
            content = [line.rstrip('\n') for line in f.readlines()]
            if content: lines = content

    def main(stdscr):
        nonlocal lines, top_line, cursor_y, cursor_x
        curses.use_default_colors()
        stdscr.keypad(True) # Enable arrow keys

        while True:
            stdscr.clear()
            max_h, max_w = stdscr.getmaxyx()
            
            # 1. HEADER (Takes 1 row)
            stdscr.addstr(0, 0, f"Editing: {fileToEdit} (Ctrl+A to Save & Exit)", curses.A_REVERSE)

            # 2. RENDER VISIBLE LINES
            # We use max_h - 2 to leave room for header and potential status bar
            display_height = max_h - 2
            for i in range(display_height):
                line_idx = top_line + i
                if line_idx < len(lines):
                    # Draw line relative to top_line
                    stdscr.addstr(i + 1, 0, lines[line_idx][:max_w-1])

            # 3. SCROLLING LOGIC (Adjust top_line based on cursor_y)
            if cursor_y < top_line:
                top_line = cursor_y
            elif cursor_y >= top_line + display_height:
                top_line = cursor_y - display_height + 1

            # 4. POSITION PHYSICAL CURSOR
            # (File Y - Scroll Offset) = Screen Y
            stdscr.move((cursor_y - top_line) + 1, cursor_x)
            
            ch = stdscr.getch()

            if ch == 1: # Ctrl+A to save
                break

            elif ch == curses.KEY_UP:
                if cursor_y > 0:
                    cursor_y -= 1
                    cursor_x = min(cursor_x, len(lines[cursor_y]))

            elif ch == curses.KEY_DOWN:
                if cursor_y < len(lines) - 1:
                    cursor_y += 1
                    cursor_x = min(cursor_x, len(lines[cursor_y]))

            elif ch == 10: # Enter
                # Split line at cursor
                current_line = lines[cursor_y]
                lines[cursor_y] = current_line[:cursor_x]
                lines.insert(cursor_y + 1, current_line[cursor_x:])
                cursor_y += 1
                cursor_x = 0

            elif ch in (curses.KEY_BACKSPACE, 127, 8):
                if cursor_x > 0:
                    lines[cursor_y] = lines[cursor_y][:cursor_x-1] + lines[cursor_y][cursor_x:]
                    cursor_x -= 1
                elif cursor_y > 0:
                    # Move current line to end of previous line
                    old_len = len(lines[cursor_y-1])
                    lines[cursor_y-1] += lines.pop(cursor_y)
                    cursor_y -= 1
                    cursor_x = old_len

            elif 32 <= ch <= 126: # Typing
                lines[cursor_y] = lines[cursor_y][:cursor_x] + chr(ch) + lines[cursor_y][cursor_x:]
                cursor_x += 1

        # --- SAVE TO FILE ---
        with open(fileToEdit, "w") as f:
            f.write("\n".join(lines))

    wrapper(main)
    print(f"File saved to {fileToEdit}")

if __name__ == "__main__":
    codeMate()
