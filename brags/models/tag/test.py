# python manage.py test brags.models.tag.test

from django.test import TestCase

from brags.models.tag.model import Tag


class TagModelTest(TestCase):
    def test_create_tag(self):
        tag = Tag.create(title='Test Tag')
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(tag.title, 'Test Tag')

    def test_tag_str_method(self):
        tag = Tag.create(title='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')

    def test_tag_min_length_validator(self):
        with self.assertRaises(ValueError):
            Tag.create(title='AB')
    
