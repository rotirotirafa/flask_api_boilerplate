from app.models.tables import User


class UsersService:
    user_model = User

    def test(self, user_id):
        return self.user_model.find_by_id(user_id)
