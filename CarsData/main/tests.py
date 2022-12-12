from django.test import TestCase


class MainViewTestCase(TestCase):

    def test_response_check(self):
        """ Проверка статуса ответа страниц """
        links = ['http://127.0.0.1:8000/', '', 'news', 'about']
        for l in range(1, len(links)):
            response = self.client.get(links[0] + links[l])
            self.assertEqual(response.status_code, 200)

