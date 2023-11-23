from brags.models.brag.model import Brag
from brags.models.brag.service import BragService
from users.models import CustomUser


class DeleteBrag():
    def execute(self, user_id: int, brag_id: int):
        user = CustomUser.find_user_by_id(
            id=user_id
        )
        brag = Brag.find_by_id(           
            id=brag_id
        )
        if not brag:
            raise ValueError('Not found')
        if brag.user != user:
            raise ValueError('Brag does not belong to user')
        brag.remove()
        return
       
       