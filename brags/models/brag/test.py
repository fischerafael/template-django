# python manage.py test brags.models.brag.test

from django.contrib.auth import get_user_model
from django.test import TestCase

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

    def test_create_brag(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.15
        )
        self.assertEqual(brag.title, 'Test Brag')
        self.assertEqual(brag.user, self.user)
        self.assertEqual(brag.category, self.category)
        self.assertEqual(brag.duration,  0.15)

    def test_find_brag_by_id(self):
        created_brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        brag = Brag.find_by_id(created_brag.id)        
        self.assertEqual(brag, created_brag)

    def test_update_brag_title(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.title, 'Test Brag')
        brag.update_title('new title')
        self.assertEqual(brag.title, 'new title')

    def test_not_update_brag_title_if_title_not_provided(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.title, 'Test Brag')
        brag.update_title()
        self.assertEqual(brag.title, 'Test Brag')

    def test_update_duration(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.title, 'Test Brag')
        brag.update_duration(1)
        self.assertEqual(brag.duration, 1)

    def test_not_update_duration_if_not_provided(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.duration, 0.5)
        brag.update_duration()
        self.assertEqual(brag.duration, 0.5)

    def test_add_tag_to_brag(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )           
        tag = Tag.create(title='Test tag')
        brag.add_tag(tag=tag)
        self.assertEqual(len(brag.tags), 1)

    def test_category(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.category, self.category)
        new_category = Category.objects.create(title='new cat')
        brag.update_category(new_category)
        self.assertEqual(brag.category, new_category)

    def test_not_update_duration_if_not_provided(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.category, self.category)
        brag.update_duration()
        self.assertEqual(brag.category, self.category)

    def test_edit_description(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        brag.edit_description('some description')
        self.assertEqual(brag.description, 'some description')
        brag.edit_description('')
        self.assertEqual(brag.description, '')
        brag.edit_description()
        self.assertEqual(brag.description, '')

    def test_make_public(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.is_public, False)
        brag.make_public()
        self.assertEqual(brag.is_public, True)

    def test_make_private(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.is_public, False)
        brag.make_public()
        self.assertEqual(brag.is_public, True)
        brag.make_private()
        self.assertEqual(brag.is_public, False)

    def test_add_tag(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(len(brag.tags), 0)
        tag = Tag.create('test')
        brag.add_tag(tag)
        self.assertEqual(len(brag.tags), 1)

    def test_delete_tag(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(len(brag.tags), 0)
        tag = Tag.create('test')
        brag.add_tag(tag)
        self.assertEqual(len(brag.tags), 1)
        brag.remove_tag(tag)
        self.assertEqual(len(brag.tags), 0)

    def test_delete_non_existing_tag(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(len(brag.tags), 0)
        tag = Tag.create('test')
        brag.add_tag(tag)
        self.assertEqual(len(brag.tags), 1)
        other_tag = Tag.create('another')
        brag.remove_tag(other_tag)
        self.assertEqual(len(brag.tags), 1)

    def test_remove_brag(self):
        brag = Brag.create(
            title='Test Brag',
            user=self.user,
            category=self.category,
            duration=0.5
        )
        self.assertEqual(brag.title, 'Test Brag')
        brag.remove()
        brag = Brag.find_by_id(brag.id)
        self.assertEqual(brag, None)

