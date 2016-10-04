import hog
if __name__ == '__main__':
    always = hog.always_roll
    hog.four_sided = hog.make_test_dice(1)
    hog.six_sided = hog.make_test_dice(3)
    s0, s1 = hog.play(always(0), always(0))
    print(s0)
    print(s1)