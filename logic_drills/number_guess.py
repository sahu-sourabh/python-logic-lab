import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.helper_utils import get_random_number, sanitize_input

def main():
    print("Welcome to the Number Guessing Simulator!")
    
    # Capture the target ONCE before the game starts
    target = get_random_number(1, 100)
    
    while True:
        try:
            raw_input = input('Guess the number between 1 & 100: ')
            user_guess = int(sanitize_input(raw_input))
            
            if user_guess < target:
                print('Too low!')
            elif user_guess > target:
                print('Too high!')
            else:
                print(f'🎉 Congratulations! {target} was the correct number.')
                break
        except ValueError:
            print('⚠️ Please enter a valid number.')

if __name__ == "__main__":
    main()