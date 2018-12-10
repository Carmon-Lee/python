from operator import attrgetter
class User:
    def __init__(self,user_id):
        self.user_id=user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users=[User(99),User(3),User(5)]
print(users)


def function1(u):
    return u.user_id


print(sorted(users, key=lambda u:u.user_id))
print(users)
