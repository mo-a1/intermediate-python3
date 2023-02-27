from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"user({self.user_id})"


ali = User(12)
mazen = User(17)
mona = User(1)
alaa = User(122)

users = [ali, mazen, mona, alaa]
print(sorted(users, key=attrgetter('user_id')))
# or
print(sorted(users, key=lambda x: x.user_id))
