from brags.models.brag.model import Brag
from users.models import CustomUser


class ListBrags():
    def execute(self, user_id: int):
        user = CustomUser.find_user_by_id(
            id=user_id
        )
        brags = Brag.list_brags_by_user(
            user=user
        )
        return brags
       
       