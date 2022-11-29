# aplicando for


def loop_for():
    for x in range(0, 51):
        if x % 2 == 0:
            print(x)


loop_for()


def loop_for_enum():
    list = ["a", "b", "c", "d", "e"]
    for i, x in enumerate(list):
        if i % 2 == 0:
            print(i, x)


loop_for_enum()
