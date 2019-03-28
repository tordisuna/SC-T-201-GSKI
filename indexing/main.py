from repo import Repo
from contact import Contact

my_repo = Repo(Contact)
a = Contact("Gudni", "9635354", "gudni@email.com")
b = Contact("Lalli", "3453453", "lalli@email.com")
c = Contact("Sigga", "2341123", "sigga@email.com")
d = Contact("Hannes", "03459533", "hannes@email.com")
e = Contact("Gudni", "1234567", "gudni@fakemail.com")
my_repo.add(a, b, c, d, e)

undo_stack = list()
undo_stack.append(((my_repo.remove, (a, b, c, d, e)),))


def undo():
    for undo_method, arguments in undo_stack.pop():
        undo_method(*arguments)


print(my_repo, "\n")
undo()
print(my_repo)

# for item in my_repo.order_by("name"):
#     print(item)

# print()
# for item in my_repo.order_by("phone"):
#     print(item)

# print()
# for item in my_repo.search("name", "Gudni"):
#     print(item)

# print(my_repo.search("name", "Gudni"))

# print()

# print("Multi field search:")
# conditions = {"name": "Gudni", "email": "gudni@fakemail.com"}
# print(my_repo.multi_field_search(conditions))

# to_remove = my_repo.get("name", "Gudni")

# print(to_remove)

# my_repo.remove(to_remove)
# print(my_repo)

# print(my_repo.search_range("name", "A", "J"))


# # print(my_repo.get("name", "Jon"))  # should break
