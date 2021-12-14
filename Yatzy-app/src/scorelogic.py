
class Categories:
    """A class for checking the dice against different scoring categories.
    """

    def __init__(self):
        pass

    def check_aces(self, dice_list):
        """Checks the given dice list against this scoring category, in this instance ones.
            This docstring describes all the methods in this class.

        Args:
            dice_list: the dice list which the score will be decided on.

        Returns:
            A score which will be saved to the current players scoreboard.
        """

        score = dice_list.count(1)
        print("Your score for Aces is: ", score)
        return score

    def check_twos(self, dice_list):

        score = dice_list.count(2) * 2
        print("Your score for Twos is: ", score)
        return score

    def check_threes(self, dice_list):

        score = dice_list.count(3) * 3
        print("Your score for Threes is: ", score)
        return score

    def check_fours(self, dice_list):

        score = dice_list.count(4) * 4
        print("Your score for Fours is: ", score)
        return score

    def check_fives(self, dice_list):

        score = dice_list.count(5) * 5
        print("Your score for Fives is: ", score)
        return score

    def check_sixes(self, dice_list):

        score = dice_list.count(6) * 6
        print("Your score for Sixes is: ", score)
        return score

    def check_one_pair(self, dice_list):
        # bugged, will fix later

        score = 0

        dice_list.sort()
        print(dice_list)

        if dice_list[3] == dice_list[4]:
            score = dice_list[4] * 2
            print("Your score for One pair is: ", score)
            return score

        print("Your score for One pair is: ", score)
        return score

    def check_two_pairs(self, dice_list):

        score = 0

        dice_list.sort()
        print(dice_list)

        if (dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]) or (dice_list[0] == dice_list[1] and dice_list[3] == dice_list[4]) or (dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]):
            score = sum(dice_list) - dice_list[4]
            print("Your score for Two pairs is: ", score)
            return score

        print("Your score for Two pairs is: ", score)
        return score

    def check_three_of_a_kind(self, dice_list):

        score = 0

        for i in dice_list:
            if dice_list.count(i) >= 3:
                score = i * 3
                print("Your score for Three of a kind is: ", score)
                return score

        print("Your score for Three of a kind is: ", score)
        return score

    def check_four_of_a_kind(self, dice_list):

        score = 0

        for i in dice_list:
            if dice_list.count(i) >= 4:
                score = i * 4
                print("Your score for Four of a kind is: ", score)
                return score

        print("Your score for Four of a kind is: ", score)
        return score

    def check_yatzy(self, dice_list):

        score = 0

        for i in dice_list:
            if dice_list.count(i) == 5:
                score = 50
                print("Your score for Yatzy is: ", score)
                return score

        print("Your score for Yatzy is: ", score)
        return score

    def check_full_house(self, dice_list):

        score = 0

        dice_list.sort()

        if (len(set(dice_list))) != 2:
            return score

        if dice_list[0] != dice_list[3] or dice_list[1] != dice_list[4]:
            score = sum(dice_list)
            return score

        return score

    def check_low_straight(self, dice_list):

        score = 0

        if len(set(dice_list)) == 5 and sum(dice_list) == 15:
            score = 15
            print("Your score for Low Straight is: ", score)
            return score

        print("Your score for Low Straight is: ", score)
        return score

    def check_high_straight(self, dice_list):

        score = 0

        if len(set(dice_list)) == 5 and sum(dice_list) == 20:
            score = 20
            print("Your score for High Straight is: ", score)
            return score

        print("Your score for High Straight is: ", score)
        return score

    def check_chance(self, dice_list):

        print("Your score for Chance is: ", sum(dice_list))
        return sum(dice_list)
