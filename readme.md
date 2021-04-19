1. Requirements

You will need Python3 in order to run this program

2. Setup

Ensure all required packages are installed, using pip. For most python installations this will be done through the command:

pip3 (or pip) install -r requirements.txt

3. First Run

Once the dependencies are installed, use your command line tool (cmd for windows, terminal for Mac and Linux) and move
to the directory that you unzipped the program into. Run the command:

/path/to/program/main.py

This will open a window which allows registration of a new account or logging in. 
Since you will not have an account yet, please create a new account. 
Once successful (a box will confirm), log in using this information. 
This will take you to a page where you can choose an existing list of magic cards (which you will not have yet).
Instead, create a new list by typing a name you want your list to be called in the box titled “Make New List” and hitting the button.
For example, type “List 1” or “Bob’s List” in the bottom box and hit “Make New List”. 
Once done, this will open the “card search” window, in which you can input the name of a magic card (examples to try: Cancel, Putrefy, Weaponize the Monsters).
This will also return an error if no card with the name was found (try typing “Cancell” instead of Cancel). 
This will create a series of buttons in the bottom frame.
These buttons, when clicked, dynamically add this card to an excel document (with the name you entered previously). 
When you close this card search window, the list is saved in /lists/username/listname. 
This excel document can then be opened to see a list of cards in your collection and their qualities (price, etc). 