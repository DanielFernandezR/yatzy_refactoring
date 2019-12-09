class Yatzy:

    @staticmethod
    def chance(*dice):

        sum_dice = 0
        for die in dice:
            sum_dice += die
        return sum_dice

    @staticmethod
    def yatzy(*dice):
        for die in dice:
            if dice.count(die) == len(dice):
                return 50
            else:
                return 0

    @staticmethod
    def sum_of_ones(*dice):
        total_of_ones = 0
        for die in dice:
            if die == 1:
                total_of_ones += 1
            else:
                continue
        return total_of_ones

    @staticmethod
    def sum_of_twos(*dice):
        sum_twos = 0
        for die in dice:
            if die == 2:
                sum_twos += 2
            else:
                continue
        return sum_twos

    @staticmethod
    def sum_of_threes(*dice):
        sum_threes = 0
        for die in dice:
            if die == 3:
                sum_threes += 3
            else:
                continue
        return sum_threes

    @staticmethod
    def sum_of_fours(*dice):
        sum_fours = 0
        for die in dice:
            if die == 4:
                sum_fours += 4
            else:
                continue
        return sum_fours

    def sum_of_fives(*dice):
        sum_fives = 0
        for die in dice:
            if die == 5:
                sum_fives += 5
            else:
                continue
        return sum_fives

    def sum_of_sixes(*dice):
        sum_sixes = 0
        for die in dice:
            if die == 6:
                sum_sixes += 6
            else:
                continue
        return sum_sixes

    @staticmethod
    def sum_bigger_pair(*dice):
        pair = 2
        list_numbers = []
        for die in dice:
            if dice.count(die) == 2:
                list_numbers.append(die)
            else:
                continue
        if list_numbers == []:
            return 0
        else:
            list_numbers.sort()
            return list_numbers[-1] * pair

    @staticmethod
    def sum_two_pairs(*dice):
        pair = 2
        list_numbers = []
        for die in dice:
            if dice.count(die) >= pair:
                if list_numbers.count(die) == 0:
                    list_numbers.append(die)
                else:
                    continue
        if list_numbers == [] or len(list_numbers) == 1:
            return 0
        else:
            return (list_numbers[0] * pair) + (list_numbers[-1] * pair)

    @staticmethod
    def sum_three_same_num(*dice):
        three_kind = 3
        list_numbers = []
        for die in dice:
            if dice.count(die) >= three_kind:
                if list_numbers.count(die) == 0:
                    list_numbers.append(die)
                else:
                    continue
        if list_numbers == []:
            return 0
        else:
            return list_numbers[0] * three_kind

    @staticmethod
    def sum_four_same_num(*dice):
        four_kind = 4
        list_numbers = []
        for die in dice:
            if dice.count(die) >= four_kind:
                if list_numbers.count(die) == 0:
                    list_numbers.append(die)
                else:
                    continue
        if list_numbers == []:
            return 0
        else:
            return list_numbers[0] * four_kind

    @staticmethod
    def sum_small_straight(*dice):
        list_numbers = []
        for die in dice:
            if dice.count(die) != 1:
                return 0
            else:
                list_numbers.append(die)
        if 6 in list_numbers:
            return 0
        else:
            return 15

    @staticmethod
    def sum_large_straight(*dice):
        list_numbers = []
        for die in dice:
            if dice.count(die) != 1:
                return 0
            else:
                list_numbers.append(die)
        if 1 in list_numbers:
            return 0
        else:
            return 20

    @staticmethod
    def full_house(*dice):
        list_numbers = []
        for die in dice:
            if dice.count(die) == 2 or dice.count(die) == 3:
                if list_numbers.count(die) == 0:
                    list_numbers.append(die)
                else:
                    continue
            else:
                return 0
        return (list_numbers[0] * dice.count(list_numbers[0])) + (list_numbers[1] * dice.count(list_numbers[1]))
