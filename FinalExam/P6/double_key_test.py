from random import randrange, choice
from double_key import DoubleKeyContainer


def test_add_contact(pydict, dk, id, name, phone):
    dk.add_contact(id, name, id)
    pydict[id] = name


def test_get_name_by_id(pydict, dk, id, name, phone):
    try:
        assert pydict[id] == dk.get_name_by_id(id)
    except KeyError:
        assert id not in pydict
        assert dk.get_name_by_id(id) is None


def test_get_name_by_phone(pydict, dk, id, name, phone):
    try:
        assert pydict[phone] == dk.get_name_by_phone(phone)
    except KeyError:
        assert (phone) not in pydict
        assert dk.get_name_by_id(phone) is None


def test_remove(pydict, dk, id, name, phone):
    try:
        del pydict[id]
    except KeyError:
        pass
    dk.remove(id)


if __name__ == "__main__":
    test_functions = [test_add_contact, test_get_name_by_id,
                      test_get_name_by_phone, test_remove]
    for i in range(1000):
        dk = DoubleKeyContainer()
        my_dict = dict()
        for i in range(10000):
            id = randrange(0, 10000)
            name = randrange(0, 10000)
            phone = randrange(0, 10000)
            fun = choice(test_functions)
            fun(my_dict, dk, id, name, phone)
