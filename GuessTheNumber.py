import random


class GuessTheNumber:
    """
    Computer guesses your number getting inputs and
    logs the number to a file for future use.
    """

    def __init__(self, low, high):
        self.test = False
        self.check_win = True
        self.player_name = input("Hello! Whats your name?\n")
        self.low = int(low)
        self.high = int(high)
        self.com_guess = 1

    def start(self):
        print('Think of a number between {} and {}.'.format(self.low, self.high))
        self.main_loop()

    def generate_guess(self):
        self.com_guess = random.randint(self.low, self.high)

    def main_loop(self):
        while self.check_win is False:
            self.generate_guess()
            while self.test is False:
                var1 = input('Is {} your number, {}?\n(y/n): '.format(self.com_guess, self.player_name))
                if var1.lower() == 'y' or var1.lower() == 'n':
                    self.test = True
                else:
                    self.test = False
            if var1.lower() == 'y':
                pass
            elif var1.lower() == 'n':
                var2 = input('Is your number higher?\n(y/n): ')
                if var2.lower() == 'y':
                    self.low = self.com_guess
                    self.test = False
                else:
                    self.high = self.com_guess
        self.write_to_file()

    def write_to_file(self):
        with open('GuessTheNumber_Answers.txt', 'a') as f:
            f.write('\n{} - {}'.format(self.player_name, str(self.com_guess)))


def main():
    game = GuessTheNumber("1", "50")
    game.start()


if __name__ == "__main__":
    main()
