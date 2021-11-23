import dice


def main():
    rolled_dice = dice.roll()
    dice.choose(rolled_dice)
    dice.choose(rolled_dice)


main()
