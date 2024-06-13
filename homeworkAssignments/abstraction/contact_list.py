class ContactList:

    all_contacts = {}

    def __init__(self, list_name, list_of_objects):
        self._list_name = list_name
        self._list_of_objects = list_of_objects
        ContactList.all_contacts[self._list_name] = self._list_of_objects

    def compare_list(self, list_one, list_two):
        compare = ContactList.all_contacts[list_one]
        compare_to = ContactList.all_contacts[list_two]
        output = []

        for contact in compare:
            if contact in compare_to:
                output.append(contact)
        return output

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)


friends_i_work_with = my_friends_list.compare_list('My Friends', 'Work Buddies')
print(friends_i_work_with)

# for item in ContactList.all_contacts:
#     print(ContactList.all_contacts[item])
#     for list_item in ContactList.all_contacts[item]:
#         for key, value in list_item.items():
#             print(f'{key}, {value}')

# friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]