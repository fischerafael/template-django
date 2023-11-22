from brags.models.brag.model import Brag
from brags.models.category.model import Category
from users.models import CustomUser

class CreateBrag():
    def execute(
        self, 
        duration: float, 
        title: str, 
        user_id: int,
        category_id: int
    ):
        user = CustomUser.find_user_by_id(
            id=user_id
        )
        category = Category.find_by_id(category_id)
        brag = Brag.create(
            duration=duration,
            title=title,
            user=user,
            category=category
        )
        return brag