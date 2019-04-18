
class DoubleKeyContainer(object):
    def __init__(self):
        self.id_map = dict()  # maps ID to phone and name
        self.phone_map = dict()  # maps phone to ID

    def add_contact(self, id, name, phone):
        if id in self.id_map:
            del self.phone_map[self.id_map[id][1]]
        self.id_map[id] = (name, phone)
        self.phone_map[phone] = id

    def get_name_by_id(self, id):
        try:
            return self.id_map[id][0]
        except KeyError:
            return None

    def get_name_by_phone(self, phone):
        try:
            return self.get_name_by_id(self.phone_map[phone])
        except KeyError:
            return None

    def remove(self, id):
        try:
            phone = self.id_map[id][1]
            del self.id_map[id]
            del self.phone_map[phone]
        except KeyError:
            pass


if __name__ == "__main__":

    print("TESTING DOUBLE KEY - MAKE BETTER TESTS!!!\n")

    dkc = DoubleKeyContainer()
    dkc.add_contact(23, "Kári", 23543)
    dkc.add_contact(21, "Sigurður", 12342153)
    dkc.add_contact(13, "Kristmundur", 63567356)
    dkc.add_contact(87, "Eysteinn", 73345)
    dkc.add_contact(3, "Hrafn", 93543)

    print(dkc.get_name_by_id(13))
    print(dkc.get_name_by_phone(23543))
    print(dkc.get_name_by_id(87))
    print(dkc.get_name_by_phone(73345))
    dkc.remove(87)
    print(dkc.get_name_by_id(87))
    print(dkc.get_name_by_phone(73345))

    dkc.remove(5134)

    # test overwrite
    print(dkc.get_name_by_id(13))
    dkc.add_contact(13, "Guðni", 4445555)
    print(dkc.get_name_by_id(13))
    print(dkc.get_name_by_phone(4445555))

    # test duplicated phone number
    dkc.add_contact(53, "Natan", 4445555)
    print(dkc.get_name_by_id(53))
    print(dkc.get_name_by_id(13))
    print(dkc.get_name_by_phone(4445555))

    dkc.remove(13)
    print(dkc.get_name_by_phone(4445555))
    print(dkc.get_name_by_id(53))  # messed up
