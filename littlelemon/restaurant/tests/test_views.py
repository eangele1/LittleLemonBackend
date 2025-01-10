from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(title="Bread", price=80, inventory=100)
        self.menu3 = Menu.objects.create(title="Water", price=80, inventory=100)

    def test_getall(self):
        self.client.login(username="janedoe1", password="JAA06ZvV")
        response = self.client.get("/restaurant/menu/")
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
