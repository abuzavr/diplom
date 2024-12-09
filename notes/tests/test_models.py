from django.test import TestCase
from django.contrib.auth.models import User
from notes.models import Note

class NoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.note = Note.objects.create(
            user=self.user,
            title='Test Note',
            content='Test content'
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, 'Test Note')
        self.assertEqual(self.note.user, self.user)
        self.assertIsNotNone(self.note.created_at)
        self.assertIsNotNone(self.note.updated_at)
