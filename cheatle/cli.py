from email.policy import default
import click
from cheatle import WordleSolver
import re
import sys
from random import randint

@click.command()
@click.option('--guess',default='.....',help="Current guess, used '.' for blanks")
@click.option('--has',default='',help="Unordered letters that the word has")
@click.option('--used',default='',help="Unordered letters that are not in the word")
@click.option('--all',default=False,is_flag=True)
@click.option('--n',default=1,help="Number of matches to print")
def main(guess,has,all,n,used):
    solver = WordleSolver()
    cur_set = solver.get_list(guess,has,used)
    n_matches = len(cur_set)
    if n_matches <= 0:
        print("No matches for current guess :(")
        sys.exit(1)
    print(f"Found {n_matches} matches!")
    if all:
        print(f"Printing all {n_matches} matches")
        [print(wd) for wd in cur_set]
    else:
        print(f"Printing {n} randomly selected word")
        for _ in range(n):
            selected_word = cur_set[randint(0,n_matches-1)]
            print(selected_word)
    sys.exit(0)
    