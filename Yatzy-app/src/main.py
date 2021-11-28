from dice import Dice
from scorelogic import Categories as C


def main():
    player_score = C()
    dice_set1 = Dice()

    dice_set1.roll()

    # fixthis
    test_set = dice_set1.print()
    player_score.test_checking(test_set)

    dice_set1.choose()
    dice_set1.choose()


main()
