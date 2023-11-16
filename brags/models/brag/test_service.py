# python manage.py test brags.models.brag.test_service

from datetime import datetime, timedelta, date
from django.test import TestCase
from django.contrib.auth import get_user_model
from brags.models.brag.model import Brag
from brags.models.brag.service import BragService
from brags.models.category.model import Category
from users.models import CustomUser


class BragServiceTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@gmail.com',
            password='testpassword'
        )
        self.category = Category.objects.create(title='Test Category')
        self.today = datetime.today().date()

    def test_list_by_user_by_day(self):
        Brag.create(
            title='Brag 1',
            category=self.category,
            user=self.user
        )
        Brag.create(
            title='Brag 2',
            category=self.category,
            user=self.user
        )       
        result = BragService.list_by_user_by_day(user=self.user, day=self.today)
        self.assertEqual(len(result), 2)

    # def test_list_by_user_by_day_with_correct_order(self):
    #     brag1 = Brag.create(
    #         title='Brag 1',
    #         category=self.category,
    #         user=self.user
    #     )
    #     brag1._set_created_at = date(2000, 11, 10)
    #     brag2 = Brag.create(
    #         title='Brag 2',
    #         category=self.category,
    #         user=self.user
    #     ) 
    #     print(brag1.created_at)
    #     print(brag2.created_at)      
    #     result = BragService.list_by_user_by_day(user=self.user, day=self.today)
    #     self.assertEqual(len(result), 1)