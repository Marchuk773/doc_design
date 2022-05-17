class UserController:
    def __init__(self, user_dao, file_reader):
        self.user_dao = user_dao
        self.file_reader = file_reader

    def get_user(self, user_id):
        return self.user_dao.get_user(user_id)

    def get_users(self):
        return self.user_dao.get_users()

    def create_user(self, **kwargs):
        return self.user_dao.create_user(**kwargs)

    def create_users_from_csv(self):
        users = self.file_reader.read_csv('user')
        self.user_dao.create_users(users)
