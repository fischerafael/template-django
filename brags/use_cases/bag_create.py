from brags.models.brag.model import Brag
from users.models import CustomUser

class CreateBrag():
    def execute(
        self, 
        duration: float, 
        title: str, 
        user_id: int
    ):
        user = CustomUser.find_user_by_id(
            id=user_id
        )
        brag = Brag.create(
            duration=duration,
            title=title,
            user=user,
        )
        return brag