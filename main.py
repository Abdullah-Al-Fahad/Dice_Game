import sys
from dice import Dice
from game import Game

def main():
    if len(sys.argv) < 4:
        print("Error: At least 3 dice configurations are required")
        print("Example: python main.py 2,2,4,4,9,9 6,8,1,1,8,6 7,5,3,7,5,3")
        sys.exit(1)
        
    try:
        dice_list = []
        for dice_str in sys.argv[1:]:
            values = list(map(int, dice_str.split(',')))
            if any(value < 0 for value in values):
                raise ValueError("Dice values must be non-negative integers")
            dice_list.append(Dice(values))
        
        if any(len(dice.values) != 6 for dice in dice_list):
            raise ValueError("Each dice must have exactly 6 values")
        
        game = Game(dice_list)
        game.play()
    except ValueError as e:
        print(f"Error: {str(e)}")
        print("Example: python main.py 2,2,4,4,9,9 6,8,1,1,8,6 7,5,3,7,5,3")
        sys.exit(1)

if __name__ == "__main__":
    main()
