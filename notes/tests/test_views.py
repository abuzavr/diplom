from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from notes.models import Note

class NoteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.client.login(username='testuser', password='password')
        self.note = Note.objects.create(user=self.user, title='Test Note', content='Test')

    def test_note_list_view(self):
        response = self.client.get(reverse('notes:note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        response = self.client.get(reverse('notes:note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
