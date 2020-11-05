# Wheel Of Fortune
Implementation of a simplified version of [Wheel Of Fortune](https://www.wheeloffortune.com/) Game

In this version, there are computer players in addition to human players.
Computer players' difficulty level is set at the beginning of the game.

Screenshots from the game:

![1](https://user-images.githubusercontent.com/37106831/98155204-e9dfc600-1ee6-11eb-9e83-995662a724d6.jpg)
![2](https://user-images.githubusercontent.com/37106831/98155209-eba98980-1ee6-11eb-8d47-858f0e12ce03.jpg)
![3](https://user-images.githubusercontent.com/37106831/98155216-ed734d00-1ee6-11eb-8936-8f7b459cbd63.jpg)

The game continues...

## Technical Info

Categories and phrases are fetched from [phrases.json](https://github.com/kilicars/WheelOfFortune/blob/master/data/phrases.json) under `data` folder

Wheel data is fetched from [wheel.json](https://github.com/kilicars/WheelOfFortune/blob/master/data/wheel.json)  under `data` folder

Player related classes are found in `players` folder:

`player.py` is the base class for the players

`human_player.py` is inherited from `player` and represents the human player

`computer_player.py` is inherited from `player` and represents the computer player

`board.py` represents the board in the game where the category, phrase and guessed letters shown

`wheel.py` represents the wheel of the game which the player spins and get results like "cash", "bankrupt", "lose a turn"

`constants.py` includes the constants like "letters", "vowel_cost" etc.

`colorful.py` is a script that is used to color the text in the console

`wof.py` (short for wheel of fortune) includes the logic of the game organizing the above classes and interacts with the user using the standard output

## To Run the Application

```pip install colorama```

Run in the terminal as:

```python wof.py```
