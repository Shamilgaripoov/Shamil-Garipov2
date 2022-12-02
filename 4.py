class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def view(self):
        print('Я - User. Могу просматривать содержимое.')

class Moderator(User):

    def __init__(self, group_id, login, password):
        super(Moderator, self).__init__(login, password)
        self.group_id = group_id

    def view(self):
        print('я - Moderator. Могу просматривать содержимое.')

    def redact(self):
        print(' Я - Moderator. Могу редактировать содержимое.')

user1 = User
moderat1 = Moderator(123, "Shama123", "12345")
print(user1.view)
print(moderat1.group_id)
print(moderat1.login)
print(moderat1.password)
moderat1.view()
moderat1.redact()


