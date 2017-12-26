
# Moving
Vim provides many ways to move the cursor. Becoming familiar with them leads to more effective text editing.

- h   move one character left
- j   move one row down
- k   move one row up
- l   move one character right
- w   move to beginning of next word
- b   move to previous beginning of word
- e   move to end of word
- W   move to beginning of next word after a whitespace
- B   move to beginning of previous word before a whitespace
- E   move to end of word before a whitespace

All the above movements can be preceded by a count; e.g. 4j moves down 4 lines.

- 0   move to beginning of line
- $   move to end of line
- _   move to first non-blank character of the line
- g_  move to last non-blank character of the line

- gg  move to first line
- G   move to last line
- ngg move to n'th line of file (n is a number; 12gg moves to line 12)
- nG  move to n'th line of file (n is a number; 12G moves to line 12)
- H   move to top of screen
- M   move to middle of screen
- L   move to bottom of screen

- zz  scroll the line with the cursor to the center of the screen
- zt  scroll the line with the cursor to the top
- zb  scroll the line with the cursor to the bottom

- Ctrl-D  move half-page down
- Ctrl-U  move half-page up
- Ctrl-B  page up
- Ctrl-F  page down
- Ctrl-O  jump to last (older) cursor position
- Ctrl-I  jump to next cursor position (after Ctrl-O)
- Ctrl-Y  move view pane up
- Ctrl-E  move view pane down

- n   next matching search pattern
- N   previous matching search pattern
  next whole word under cursor
- \#   previous whole word under cursor
- g*  next matching search (not whole word) pattern under cursor
- g#  previous matching search (not whole word) pattern under cursor
- gd  go to definition/first occurrence of the word under cursor
- %   jump to matching bracket { } [ ] ( )

- fX  to next 'X' after cursor, in the same line (X is any character)
- FX  to previous 'X' before cursor (f and F put the cursor on X)
- tX  til next 'X' (similar to above, but cursor is before X)
- TX  til previous 'X'
- ;   repeat above, in same direction
- ,   repeat above, in reverse direction



# Insert mode - inserting/appending text
- i - insert before the cursor
- I - insert at the beginning of the line
- a - insert (append) after the cursor
- A - insert (append) at the end of the line
- o - append (open) a new line below the current line
- O - append (open) a new line above the current line
- ea - insert (append) at the end of the word
- Esc - exit insert mode
# Editing
- r - replace a single character
- J - join line below to the current one with one space in between
- gJ - join line below to the current one without space in between
- cc - change (replace) entire line
- cw - change (replace) to the end of the word
- c$ - change (replace) to the end of the line
- s - delete character and substitute text
- S - delete line and substitute text (same as cc)
- xp - transpose two letters (delete and paste)
- u - undo
- Ctrl + r - redo
- repeat last command
# Marking text (visual mode)
v - start visual mode, mark lines, then do a command (like y-yank)
V - start linewise visual mode
o - move to other end of marked area
Ctrl + v - start visual block mode
O - move to other corner of block
aw - mark a word
ab - a block with ()
aB - a block with {}
ib - inner block with ()
iB - inner block with {}
Esc - exit visual mode
# Visual commands
- > - shift text right
- < - shift text left
- y - yank (copy) marked text
- d - delete marked text
- ~ - switch case
# Registers
- :reg - show registers content
- "xy - yank into register x
- "xp - paste contents of register x
- Tip Registers are being stored in ~/.viminfo, and will be loaded again on next restart of vim.
- Tip Register 0 contains always the value of the last yank command.
# Marks
- :marks - list of marks
- ma - set current position for mark A
- `a - jump to position of mark A
- y`a - yank text to position of mark A
# Macros
- qa - record macro a
- q - stop recording macro
- @a - run macro a
- @@ - rerun last run macro
- Cut and paste
- yy - yank (copy) a line
- 2yy - yank (copy) 2 lines
- yw - yank (copy) the characters of the word from the cursor position to the start of the next word
- y$ - yank (copy) to end of line
- p - put (paste) the clipboard after cursor
- P - put (paste) before cursor
- dd - delete (cut) a line
- 2dd - delete (cut) 2 lines
- dw - delete (cut) the characters of the word from the cursor position to the start of the next word
- D - delete (cut) to the end of the line
- d$ - delete (cut) to the end of the line
- x - delete (cut) character
# Exiting
- :w - write (save) the file, but don't exit
- :w !sudo tee % - write out the current file using sudo
- :wq or :x or ZZ - write (save) and quit
- :q - quit (fails if there are unsaved changes)
- :q! or ZQ - quit and throw away unsaved changes
- :wqa - write (save) and quit on all tabs
# Search and replace
- /pattern - search for pattern
- ?pattern - search backward for pattern
- \vpattern - 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed)
- n - repeat search in same direction
- N - repeat search in opposite direction
- :%s/old/new/g - replace all old with new throughout file
- :%s/old/new/gc - replace all old with new throughout file with confirmations
- :noh - remove highlighting of search matches
# Search in multiple files
- :vimgrep /pattern/ {file} - search for pattern in multiple files
- e.g. :vimgrep /foo/ \**/*
- :cn - jump to the next match
- :cp - jump to the previous match
- :copen - open a window containing the list of matches
# Working with multiple files
- :e file - edit a file in a new buffer
- :bnext or :bn - go to the next buffer
- :bprev or :bp - go to the previous buffer
- :bd - delete a buffer (close a file)
- :ls - list all open buffers
- :sp file - open a file in a new buffer and split window
- :vsp file - open a file in a new buffer and vertically split window
- Ctrl + ws - split window
- Ctrl + ww - switch windows
- Ctrl + wq - quit a window
- Ctrl + wv - split window vertically
- Ctrl + wh - move cursor to the left window (vertical split)
- Ctrl + wl - move cursor to the right window (vertical split)
- Ctrl + wj - move cursor to the window below (horizontal split)
- Ctrl + wk - move cursor to the window above (horizontal split)
# Tabs
- :tabnew or :tabnew file - open a file in a new tab
- Ctrl + wT - move the current split window into its own tab
- gt or :tabnext or :tabn - move to the next tab
- gT or :tabprev or :tabp - move to the previous tab
- #gt - move to tab number #
- :tabmove # - move current tab to the #th position (indexed from 0)
- :tabclose or :tabc - close the current tab and all its windows
- :tabonly or :tabo - close all tabs except for the current one
- :tabdo command - run the command on all tabs (e.g. :tabdo q - closes all opened tabs)
