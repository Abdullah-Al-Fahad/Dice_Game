import sys
import secrets
import hmac
import hashlib
from typing import List, Tuple
from dice import Dice
from game_utils import GameUtils

class Game:
    def __init__(self, dice_list: List[Dice]):
        self.dice_list = dice_list
        
    def get_user_choice(self, prompt: str, options: List[str], max_value: int) -> int:
        print("\n".join(f"{i} - {option}" for i, option in enumerate(options)))
        print("X - exit\n? - help")
        
        while True:
            choice = input(prompt).strip().upper()
            if choice == 'X':
                sys.exit(0)
            elif choice == '?':
                print("\nProbability of winning for each dice combination:")
                print(GameUtils.render_probability_table(self.dice_list))
                continue
                
            try:
                value = int(choice)
                if 0 <= value <= max_value:
                    return value
                print(f"Please enter a number between 0 and {max_value}")
            except ValueError:
                print(f"Invalid input. Please enter a number between 0 and {max_value}")
                
    def generate_fair_number(self, max_value: int):
        key = secrets.token_bytes(32)
        number = secrets.randbelow(max_value + 1)
        hmac_value = hmac.new(key, str(number).encode(), hashlib.sha3_256).hexdigest().upper()
        return number, key, hmac_value
    
    def determine_first_move(self):
        print("Let's determine who makes the first move.")
        computer_number, key, hmac_value = self.generate_fair_number(1)
        print(f"I selected a random value in the range 0..1 (HMAC={hmac_value}).")
        print("Try to guess my selection.")
        
        user_choice = self.get_user_choice("Your selection: ", ['0', '1'], 1)
        print(f"My selection: {computer_number} (KEY={key.hex().upper()}).")
        
        return user_choice != computer_number
    
    def choose_dice(self, available_dice: List[int], player: str) -> Tuple[int, Dice]:
        print(f"Choose {player} dice:")
        dice_idx = self.get_user_choice(
            "Your selection: ", [str(self.dice_list[i]) for i in available_dice], len(available_dice) - 1
        )
        chosen_dice = self.dice_list[available_dice[dice_idx]]
        print(f"You choose the [{str(chosen_dice)}] dice.")
        return available_dice[dice_idx], chosen_dice
    
    def throw_dice(self, dice: Dice, player: str) -> int:
        print(f"It's time for {player} throw.")
        number, key, hmac_value = self.generate_fair_number(5)
        print(f"I selected a random value in the range 0..5 (HMAC={hmac_value}).")
        print("Add your number modulo 6.")
        
        user_number = self.get_user_choice("Your selection: ", ['0', '1', '2', '3', '4', '5'], 5)
        print(f"My number is {number} (KEY={key.hex().upper()}).")
        
        result = (number + user_number) % 6
        throw = dice[result]
        print(f"The result is {number} + {user_number} = {result} (mod 6).")
        if player == "my":
            print(f"My throw is {throw}.")
        else:
            print(f"Your throw is {throw}.")
        return throw
        
    def play_round(self, computer_dice: Dice, user_dice: Dice):
        computer_throw = self.throw_dice(computer_dice, "my")
        user_throw = self.throw_dice(user_dice, "your")
        
        if user_throw > computer_throw:
            print(f"You win ({user_throw} > {computer_throw})!")
        elif user_throw < computer_throw:
            print(f"I win ({computer_throw} > {user_throw})!")
        else:
            print(f"It's a tie ({user_throw} = {computer_throw})!")

    def play(self):
        computer_first = self.determine_first_move()
        available_dice = list(range(len(self.dice_list)))

        if computer_first:
            
            computer_dice_idx = secrets.choice(available_dice)
            computer_dice = self.dice_list[computer_dice_idx]
            available_dice.remove(computer_dice_idx)
            print(f"I make the first move and choose the [{str(computer_dice)}] dice.")
            
           
            user_dice_idx, user_dice = self.choose_dice(available_dice, "your")
        else:
            
            print("You make the first move.")
            user_dice_idx, user_dice = self.choose_dice(available_dice, "your")
            available_dice.remove(user_dice_idx)

            
            computer_dice_idx = secrets.choice(available_dice)
            computer_dice = self.dice_list[computer_dice_idx]
            print(f"I choose the [{str(computer_dice)}] dice.")

    
        self.play_round(computer_dice, user_dice)