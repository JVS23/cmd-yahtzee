
class Categories:
    def __init__(self):
        pass

    def test_checking(self, dice_list):
        print("test dice: ", dice_list)

    def check_for_aces(self, dice_list):

        print("Checking for aces..")
        score = dice_list.count(1)
        print("Your score for Aces is: ", score)
        return score

    def check_for_twos(self, dice_list):

        print("Checking for Twos..")
        score = dice_list.count(2) * 2
        print("Your score for Twos is: ", score)
        return score

    def check_for_threes(self, dice_list):

        print("Checking for Threes..")
        score = dice_list.count(3) * 3
        print("Your score for Threes is: ", score)
        return score

    def check_for_fours(self, dice_list):

        print("Checking for Fours..")
        score = dice_list.count(4) * 4
        print("Your score for Fours is: ", score)
        return score

    def check_for_fives(self, dice_list):

        print("Checking for Fives..")
        score = dice_list.count(5) * 5
        print("Your score for Fives is: ", score)
        return score

    def check_for_sixes(self, dice_list):

        print("Checking for Sixes..")
        score = dice_list.count(6) * 6
        print("Your score for Sixes is: ", score)
        return score
