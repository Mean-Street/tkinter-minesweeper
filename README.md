Minesweeper Game - Python3
==========================

Widgets Structure
-----------------

- root window
	- menu
	- top frame
		- bombs counter
		- timer
	- game frame
		- squares of the game (= frame)
			- button


Handling events procedure
-------------------------
- Click on a button => calls left or right handler with his pos
Handler executes actions depending on the button's/state and the click :
- Right click :
	- add/remove flag
	- increase/decrease number of bombs
- Left click :
	- discover
	- if bomb, loose
	- else if 0, discover neighbours
	


TODO
----

- package for global variables ? Would save parameters
- end game properly (win and loose)
- count and print numbers of bombs
- add parameters for size / number of bombs
- cf incator of difficulty 3BV


Still a bug in dependencies !
<<<<<<< HEAD
-----------------------------
- main need classes to generate a grid of squares
- classes need to call an event handler, which have to access the grid of squares

In MVC model :
--------------
- *Model* = classes.py and gui.py
	- functions and data of the project
- *View* = gui.py 
	- display model to the user
- *Controller* = utils.py
	- handle user input

=======
main need classes to generate a grid of squares
classes need to call an event handler, which have to access the grid of squares
>>>>>>> bf4b0148c1cadcd0694b44f2636f8804df24c2a0
