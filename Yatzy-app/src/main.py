from dice import Dice
from scorelogic import Categories as C


def main():
    player_score = C()
    dice_set1 = Dice()

    dice_set1.roll()

    dice_set1.choose()
    dice_set1.choose()
    # fixthis
    test_set = dice_set1.print()
    player_score.check_for_aces(test_set)
    print("---"*10)
    player_score.check_for_twos(test_set)
    #


main()
