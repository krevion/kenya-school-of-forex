import re

from django.test import SimpleTestCase
from django.test import override_settings
from django.urls import reverse


@override_settings(SECURE_SSL_REDIRECT=False)
class PublicPagesTests(SimpleTestCase):
    def test_health_check(self):
        response = self.client.get(reverse("health"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")

    def test_public_pages_render_with_at_least_three_unsplash_images(self):
        pages = ("home", "about", "curriculum", "programs", "contact")

        for page in pages:
            with self.subTest(page=page):
                response = self.client.get(reverse(page))
                self.assertEqual(response.status_code, 200)
                self.assertGreaterEqual(
                    len(
                        re.findall(
                            r'<img[^>]+src="https://images\.unsplash\.com/',
                            response.content.decode(),
                        )
                    ),
                    3,
                )

    def test_class_fees_and_contact_details_are_visible(self):
        programs_response = self.client.get(reverse("programs"))
        contact_response = self.client.get(reverse("contact"))

        self.assertContains(programs_response, "$</span>600")
        self.assertContains(programs_response, "$</span>400")
        self.assertContains(programs_response, "Lifetime signal room access")
        self.assertContains(contact_response, "0701 818 181")
        self.assertContains(contact_response, "Azure Towers, 6th Floor")
        self.assertContains(contact_response, "8:00 am – 5:00 pm")
