from datetime import date
from brags.models.brag.service import BragService
from users.models import CustomUser


class ListBrags():
    def execute(self, user_id: int, day: date):
        user = CustomUser.find_user_by_id(
            id=user_id
        )
        brags = BragService.list_by_user_by_day(
            user=user,
            day=day
        )
        return brags
       
       