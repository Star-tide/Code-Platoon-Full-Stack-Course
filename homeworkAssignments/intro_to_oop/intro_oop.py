class User:
    
    # class Variables
    all_users = {}
    total_users = len(all_users)
    
    
    #class constructor
    def __init__(self, name, email='', driver_license=None, address=None):
        self.name = name
        self.email = email
        self.address = address
        self.drivers_license = driver_license
        User.total_users += 1
        self.id = User.total_users
        # User.all_users[len(User.all_users)]
        User.all_users[self.id] = {
            "Name":  self.name,
            "Email": self.email,
            "Address" : self.address,
            "Driver License" : self.drivers_license,
            "Posts" : [] # Users.all_users[ID]["Posts"] = ...
            }
        

    # def __repr__(self):
    #     return f"'name':{self.name}, 'email':{self.email}, 'license':{self.drivers_license}"
    
    # @classmethod
    # def add_dict(cls):
    #     new_dict = {}
    @classmethod
    def delete_user(cls, user_id):
        del cls.all_users[user_id]

    # Functionality
    def add_posts(self, post):
       return User.all_users[self.id]["Posts"].append(post)

    # delete all post
    def del_posts(self):
        User.all_users[self.id]["Posts"] = []
        return f"{self.name} posts deleted"
    
    # Getters and Setters
    @property
    def get_id(self):
        return self.id
    @property
    def get_name(self):
        return self.name
    @property
    def get_email(self):
        return self.email
    @property
    def get_address(self):
        return self._address
    @property
    def get_license(self):
        return self._drivers_license
    
    @get_name.setter
    def set_name(self, new_name):
        self.name = new_name

    @get_email.setter
    def set_email(self, new_email):
        self.email = new_email

    @get_address.setter
    def set_address(self, new_address):
        self.address = new_address

    @get_license.setter
    def set_license(self, new_license):
        self.drivers_license = new_license

# class User_base:

#     def __init__(self, user_object={}):

#         self._user_object = user_object

#     def add_user(self, user):
#        self._user_object[user.get_name()] = {
#             "email" : user.get_email(),
#             "address" : user.get_address(),
#             "lisence": user.get_lisence()
#         }

#     def get_all_users(self):
#         for name, identity in self._user_object.items():
#             print(f'{name}: {identity}')

# Create User objects
user_one = User('Brandon', 'bnesslage223@yahoo.com', '8449 Hollyhock ave', 12345)
user_two = User('Michelle', 'michelle.nathe@gmail.com', '8449 Hollyhock ave', 12345)
user_three = User('Lynnze', 'lynnzejean@gmail.com', '8449 Hollyhock ave', 12345)

User.delete_user(2)
# # user_one.add_user('Brandon', 'bnesslage223@yahoo.com', '8449 Hollyhock ave', 12345)
# user_list = User_base()
# user_list.add_user(user_one)
# user_list.add_user(user_two)
# user_list.add_user(user_three)

# get_all = user_list.get_all_users()

user_one.add_posts("THIS IS A TEST")
print(user_one.del_posts())
print(User.all_users)
