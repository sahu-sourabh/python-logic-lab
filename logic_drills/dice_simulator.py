import sys
import os

# Adding the root directory to sys.path so we can import from 'scripts'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.helper_utils import roll_dice_logic, sanitize_input

YES = 'y'
NO = 'n'

def main():
    print("🎲 Welcome to the Modular Dice Simulator!")
    while True:
        choice = sanitize_input(input('Roll the dice? (y/n): '))
        
        if choice == YES:
            d1, d2 = roll_dice_logic()
            print(f'Results: {d1} and {d2} (Total: {d1 + d2})')
        elif choice == NO:
            print('Thanks for playing! 👋')
            break
        else:
            print('⚠️ Invalid choice!')

if __name__ == "__main__":
    main()