
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Note


class NotesAPITests(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(body="Learn CI/CD")

    def test_list_notes(self):
        response = self.client.get("/api/notes/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["body"], "Learn CI/CD")

    def test_retrieve_note(self):
        response = self.client.get(f"/api/notes/{self.note.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["body"], "Learn CI/CD")

    def test_create_note(self):
        response = self.client.post(
            "/api/notes/create/",
            {"body": "My first automated test"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            Note.objects.filter(body="My first automated test").exists()
        )

    def test_update_note(self):
        response = self.client.put(
            f"/api/notes/{self.note.id}/update/",
            {"body": "Updated note"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.body, "Updated note")

    def test_delete_note(self):
        response = self.client.delete(
            f"/api/notes/{self.note.id}/delete/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())

