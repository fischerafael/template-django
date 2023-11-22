from datetime import date
from brags.models.brag.service import BragService
from brags.models.category.model import Category
from users.models import CustomUser


class ListCategories():
    def execute(self, user_id: int):
        user = CustomUser.find_user_by_id(
            id=user_id
        )
        categories = Category.list_all()
        return categories
       
       