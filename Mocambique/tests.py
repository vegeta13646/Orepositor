from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class PagPrincipalTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_by_available_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    def testeTemplate(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, 'home.html')
    

class PapoPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/papo/")
        self.assertEqual(response.status_code, 200)
    
    def test_by_available_name(self):
        response = self.client.get(reverse("Papo"))
        self.assertEqual(response.status_code, 200)
    
    def testeTemplate2(self):
        response = self.client.get(reverse("Papo"))
        self.assertTemplateUsed(response, 'AboutP.html')
        self.assertContains(response, "<li>Bugatti</li>")

