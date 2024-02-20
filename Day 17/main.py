class User:

    def __init__(self, user_id, usermane):
        self.id = user_id
        self.usermane = usermane
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")

print(user_1.id)