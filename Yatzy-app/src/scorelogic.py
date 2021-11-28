
class Categories:
    def __init__(self):
        pass

    def test_checking(self, dice_list):
        print("test dice: ", dice_list)

    def check_for_aces(self, dice_list):

        score = dice_list.count(1)
        print("Your score for Aces is: ", score)
        return score

    def check_for_twos(self, dice_list):

        score = dice_list.count(2) * 2
        print("Your score for Twos is: ", score)
        return score

    def check_for_threes(self, dice_list):

        score = dice_list.count(3) * 3
        print("Your score for Threes is: ", score)
        return score

    def check_for_fours(self, dice_list):

        score = dice_list.count(4) * 4
        print("Your score for Fours is: ", score)
        return score

    def check_for_fives(self, dice_list):

        score = dice_list.count(5) * 5
        print("Your score for Fives is: ", score)
        return score

    def check_for_sixes(self, dice_list):

        score = dice_list.count(6) * 6
        print("Your score for Sixes is: ", score)
        return score

    def three_of_a_kind(self, dice_list):

        score = 0

        for i in dice_list:
            if dice_list.count(i) == 3:
                score = i * 3
                print("Your score for Three of a kind is: ", score)
                return score

        print("Your score for Three of a kind is: ", score)
        return score
