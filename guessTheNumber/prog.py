import sys


def binary_search():
    _min = 1
    _max = 1001
    guess = 500
    response = ""
    while response != "correct":
        print(guess)
        sys.stdout.flush()
        response = sys.stdin.readline().replace("\n", "")
        if response == "lower":
            _max = guess
        elif response == "higher":
            _min = guess
        guess = (_min + _max) // 2



binary_search()
