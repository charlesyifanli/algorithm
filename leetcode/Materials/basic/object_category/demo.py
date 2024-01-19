def test_mutable():
    str_0 = 'hello'
    print(id(str_0))
    str_0 += 'world'
    print(id(str_0))

    set_ = {1, 2}
    print(id(set_))
    set_.add(3)
    print(id(set_))


def test_two_dimensions_list():
    list_0 = [[0] * 3] * 3
    print(list_0)
    list_0[1][1] = 1
    print(list_0)

    list_1 = [[0] * 3 for _ in range(3)]
    print(list_1)
    list_1[1][1] = 1
    print(list_1)


test_mutable()
test_two_dimensions_list()
