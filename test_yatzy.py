from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance_scores_sum_of_all_dice():
    assert Yatzy.chance(2, 3, 4, 5, 1) == 15
    assert Yatzy.chance(3, 3, 4, 5, 1) == 16


def test_yatzy_scores_50():
    assert Yatzy.yatzy(4, 4, 4, 4, 4) == 50
    assert Yatzy.yatzy(6, 6, 6, 6, 6) == 50
    assert Yatzy.yatzy(6, 6, 6, 6, 3) == 0


def test_sum_of_ones():
    assert Yatzy.sum_of_ones(1, 2, 3, 4, 5) == 1
    assert Yatzy.sum_of_ones(1, 2, 1, 4, 5) == 2
    assert Yatzy.sum_of_ones(6, 2, 2, 4, 5) == 0
    assert Yatzy.sum_of_ones(1, 2, 1, 1, 1) == 4


def test_sum_of_twos():
    assert Yatzy.sum_of_twos(1, 2, 3, 2, 6) == 4
    assert Yatzy.sum_of_twos(2, 2, 2, 2, 2) == 10


def test_sum_of_threes():
    assert Yatzy.sum_of_threes(1, 2, 3, 2, 3) == 6
    assert Yatzy.sum_of_threes(2, 3, 3, 3, 3) == 12


def test_sum_of_fours():
    assert Yatzy.sum_of_fours(4, 4, 4, 5, 5) == 12
    assert Yatzy.sum_of_fours(4, 4, 5, 5, 5) == 8
    assert Yatzy.sum_of_fours(4, 5, 5, 5, 5) == 4


def test_sum_of_fives():
    assert Yatzy.sum_of_fives(4, 4, 4, 5, 5) == 10
    assert Yatzy.sum_of_fives(4, 4, 5, 5, 5) == 15
    assert Yatzy.sum_of_fives(4, 5, 5, 5, 5) == 20


def test_sum_of_sixes():
    assert Yatzy.sum_of_sixes(4, 4, 4, 5, 5) == 0
    assert Yatzy.sum_of_sixes(4, 4, 6, 5, 5) == 6
    assert Yatzy.sum_of_sixes(6, 5, 6, 6, 5) == 18


def test_sum_of_bigger_pair():
    assert Yatzy.sum_bigger_pair(3, 4, 3, 5, 6) == 6
    assert Yatzy.sum_bigger_pair(5, 3, 3, 3, 5) == 10
    assert Yatzy.sum_bigger_pair(5, 3, 6, 6, 5) == 12


def test_sum_of_two_pairs():
    assert Yatzy.sum_two_pairs(3, 3, 5, 4, 5) == 16
    assert Yatzy.sum_two_pairs(3, 3, 6, 6, 6) == 18
    assert Yatzy.sum_two_pairs(3, 3, 6, 5, 4) == 0


def test_sum_of_three_same_num():
    assert Yatzy.sum_three_same_num(3, 3, 3, 4, 5) == 9
    assert Yatzy.sum_three_same_num(5, 3, 5, 4, 5) == 15
    assert Yatzy.sum_three_same_num(3, 3, 3, 3, 5) == 9


def test_sum_of_four_same_num():
    assert Yatzy.sum_four_same_num(3, 3, 3, 3, 5) == 12
    assert Yatzy.sum_four_same_num(5, 5, 5, 4, 5) == 20
    assert Yatzy.sum_four_same_num(3, 3, 3, 3, 3) == 12
    assert Yatzy.sum_four_same_num(3, 3, 3, 2, 1) == 0


def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
