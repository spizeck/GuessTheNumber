import random


class GuessTheNumber:
    """
    Computer guesses your number getting inputs and
    logs the number to a file for future use.
    """

    def __init__(self, player_name, low, high):
        self.player_name = player_name
        self.low = int(low)
        self.high = int(high)
        self.com_guess = 1

    def start(self):
        print('Hi {}!\nThink of a number between {} and {}.'.format(self.player_name, self.low, self.high))
        self.main_loop()

    def generate_guess(self):
        self.com_guess = random.randint(self.low, self.high)

    def main_loop(self):
        while True:
            self.generate_guess()
            while True:
                var1 = input("Is {} your number, {}?\n(y/n): ".format(self.com_guess, self.player_name)).lower()
                if var1 == 'y' or var1 == 'n':
                    break
                else:
                    print('Invalid input.')
            if var1 == 'y':
                break
            else:
                while True:
                    var2 = input('Is your number bigger?\n(y/n): ').lower()
                    if var2 == 'y' or var2 == 'n':
                        break
                    else:
                        print('Invalid input.')
                if var2 == 'y':
                    self.low = self.com_guess
                else:
                    self.high = self.com_guess
            if self.low == self.high:
                print("I think you are lying to me...")
                break
        self.write_to_file()
        print('Thanks for playing!')

    def write_to_file(self):
        with open('GuessTheNumber_Answers.txt', 'a') as f:
            f.write('\n{} - {}'.format(self.player_name, str(self.com_guess)))


def main():
    player_name = input("Hello! Whats your name?\n")
    game = GuessTheNumber(player_name, "1", "50")
    game.start()


if __name__ == "__main__":
    main()
