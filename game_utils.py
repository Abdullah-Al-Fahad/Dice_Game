from typing import List
from prettytable import PrettyTable
from colorama import init, Fore, Style

from dice import Dice

init()

class GameUtils:
    @staticmethod
    def calculate_win_probability(dice1: Dice, dice2: Dice) -> float:
        wins = sum(1 for x in dice1.values for y in dice2.values if x > y)
        total = len(dice1.values) * len(dice2.values)
        return round(wins / total, 4)

    @staticmethod
    def render_probability_table(dice_list: List[Dice]) -> str:
        table = PrettyTable()
        header_row = ["User dice v"] + [str(dice) for dice in dice_list]
        table.field_names = [Fore.CYAN + str(header) + Style.RESET_ALL for header in header_row]
        
        for dice1 in dice_list:
            row = [str(dice1)]
            for dice2 in dice_list:
                prob = GameUtils.calculate_win_probability(dice1, dice2)
                row.append(f"- ({prob:.4f})" if dice1 == dice2 else f"{prob:.4f}")
            table.add_row(row)
        
        return """
Probability Table Help:
This table shows the probability of winning for each pair of dice.
- Each row represents the dice you choose
- Each column represents the dice the computer might choose
- Values show your probability of winning with those dice
- Diagonal entries show probabilities when same dice compete
- Higher probabilities (>0.5) mean better chances of winning
""" + "\n" + str(table)
