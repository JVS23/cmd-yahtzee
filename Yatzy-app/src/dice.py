import random as r


def roll():
    dice_list = []
    for i in range(5):
        dice_list.append(r.randint(1, 6))

    print("you rolled", dice_list)
    return dice_list


def reroll(user_input, dice_list):
    try:
        dice_list[user_input - 1] = r.randint(1, 6)
    except:
        return


def choose(dice_list):
    state = True
    print("choose the dice to reroll")
    print(dice_list)
    choices = []
    AA = [1, 2, 3, 4, 5]

    while state:
        print("choose the dice to reroll by index, quit with 7")
        user_input = int(input())

        if user_input not in AA or user_input in choices:
            break
        choices.append(user_input)

    for i in choices:
        reroll(i, dice_list)

    print(dice_list)
    return dice_list


# def AAprint(dice_list)
