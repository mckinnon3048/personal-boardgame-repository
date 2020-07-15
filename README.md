# personal-boardgame-repository
Manage a collection of boardgames accounting for player counts and value of game using python 3.8 or newer
    Python 3.8 or newer is required due to type sugestion


Project is intended to mantain a cataloge of my boardgames for both informational and insurance purposes.
The project consits of 2 files initially:
  menuapp.py                            
  boardgames.py
  
 menuapp.py --- 
    handles the user interface
    
 boardgames.py ---
    handles all the Boardgame object data, is called upon by the UI to read and write to .json file storing dictionaries of
    boardgame information in a file "board_game_lib.json"
    
    
 Future updates:
  1. Allow .env and context managment to migrate to an SQL based database
  2. Add a subjective rating to Boardgame class - including a means to update the existing library if such exists
  3. Add a game description to Boardgame class - entered either at add-time or after the fact for ease of entry
  
Learning goals:
  1. Gui interface for menuapp.py
  2. Visual processing network to read exterior of game boxes to pull title text from the packaging.
