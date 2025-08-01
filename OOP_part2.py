class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

user1 = User("01", "ilanukijr")
user2 = User("02", "ilanuki")

user1.follow(user2)
print(user2.follower)