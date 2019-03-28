from structures.meta_tree import MetaTree
from contact import Contact


class ContactList(object):
    def __init__(self, *args, **kwargs):
        self.__contacts = MetaTree(Contact)

    def add_contact(name, phone, email):
        contact = Contact(name, phone, email)
        self.__contacts.add(contact)

    def get_by_name()
