import random

# Define your GuessingGame class here...
class GuessingGame:
    def __init__(self, hidden):
       self._hidden = hidden
       self._win = False
    
    def cheat(self):
       return self._hidden
    
    def solved(self):
       return self._win
    
    def guess(self, user_input):
       if user_input == self._hidden:
          self._win = True
       elif user_input > self._hidden:
          return 'Too high!'
       elif user_input < self._hidden:
          return 'Too low!'
       

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
    print(game.cheat())
    if last_guess != None: 
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess  = input("Enter your guess: ")
    last_result = game.guess(int(last_guess))


print(f"{last_guess} was correct!")