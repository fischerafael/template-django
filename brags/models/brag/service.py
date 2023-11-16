from datetime import date

from brags.models.brag.model import Brag
from users.models import CustomUser

class BragService:
    @staticmethod
    def list_by_user_by_day(user: CustomUser, day: date):
        brags = Brag.objects.filter(user=user, created_at=day)
        brags.order_by('-created_at')
        print('********** brags', brags)
        return brags