from pathlib import Path

from django.test import TestCase
from django.contrib.auth.models import User

from papermerge.core.models import (
    Document,
    Page
)

# points to papermerge.testing folder
BASE_DIR = Path(__file__).parent


class TestPage(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'admin',
            'admin@admin.com',
            'ohmyshell',
        )

    def test_language_is_inherited(self):
        """
        Whatever document model has in doc.language field
        will be inherited by the related page models.
        """
        doc = Document.create_document(
            title="kyuss.pdf",
            user=self.user,
            language="ENG",
            file_name="kyuss.pdf",
            size=1222,
            page_count=3
        )

        doc.save()

        self.assertEqual(
            doc.page_set.count(),
            3
        )

        languages = [
            page.language for page in doc.page_set.all()
        ]

        self.assertEqual(
            ['ENG', 'ENG', 'ENG'],
            languages
        )