from django.test import TestCase
from django.contrib.auth import get_user_model
from brags.models.brag.model import Brag

from brags.models.category.model import Category
from brags.models.tag.model import Tag

class BragModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@gmail.com',
            password='testpassword'
        )
        self.category = Category.objects.create(title='Test Category')

    def test_list_brags_by_user(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.15
        )
        brags_by_user = Brag.list_brags_by_user(self.user)
        self.assertIn(brag, brags_by_user)

    def test_brag_str_method(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.15
        )
        self.assertEqual(str(brag), 'Test Brag')

    def test_create_brag_with_custom_duration(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.duration, 0.5)

    def test_find_brag_by_id(self):
        created_brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        brag = Brag.find_by_id(created_brag.id)        
        self.assertEqual(brag, created_brag)

   
