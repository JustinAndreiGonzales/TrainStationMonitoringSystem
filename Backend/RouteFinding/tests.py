from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class TestRouteFindingView(APITestCase):
    def setUp(self):
        routes = [
            ["Quirino", "Pedro Gil"],
            ["Pedro Gil", "Quirino"],
            ["Libertad", "R. Papa"],
            ["Balintawak", "United Nations"],
            ["EDSA", "Anonas"],
            ["Katipunan", "United Nations"],
            ["Doroteo Jose", "Gilmore"],
            ["Recto", "Gil Puyat"],
            ["J. Ruiz", "Doroteo Jose"],
            ["Vito Cruz", "Recto"],
            ["Recto", "Doroteo Jose"],
            ["Doroteo Jose", "Recto"],
            ["Katipunan", "Anonas"],
            ["Santolan2", "Marikina"],
            ["Pureza", "Betty Go-Belmonte"],
            ["Araneta-Cubao", "Legarda"],
            ["V. Mapa", "Taft"],
            ["North Avenue", "Katipunan"],
            ["Araneta-Cubao", "Ortigas"],
            ["Cubao", "Recto"],
            ["Gilmore", "Cubao"],
            ["Shaw Blvd.", "Araneta-Cubao"],
            ["Kamuning", "Quezon Avenue"],
            ["Guadalupe", "Buendia"],
            ["Santolan3", "Magallanes"],
            ["Boni", "Taft"],
            ["Ayala", "Blumentritt"],
            ["Baclaran", "Ortigas"],
            ["Cubao", "Abad Santos"],
            ["Doroteo Jose", "North Avenue"],
            ["Buendia", "Doroteo Jose"],
            ["Tayuman", "Cubao"],
            ["Doroteo Jose", "Cubao"],
            ["Baclaran", "Roosevelt"],
            ["Recto", "Antipolo"],
            ["North Avenue", "Taft"]
        ]

        self.urls = [reverse('route-finding', kwargs={"src": line[0], "dest": line[1]}) for line in routes]

    def test_route_finding(self):
        answer = [
            {'path': [('Quirino', 'Pedro Gil', 1)], 'cost': [14]},
            {'path': [('Pedro Gil', 'Quirino', 1)], 'cost': [14]},
            {'path': [('Libertad', 'R. Papa', 13)], 'cost': [26]},
            {'path': [('Balintawak', 'United Nations', 11)], 'cost': [26]},
            {'path': [('EDSA', 'Doroteo Jose', 9), ('Recto', 'Anonas', 8)], 'cost': [23, 25]},
            {'path': [('Katipunan', 'Recto', 9), ('Doroteo Jose', 'United Nations', 3)], 'cost': [26, 16]},
            {'path': [('Doroteo Jose', 'Doroteo Jose', 0), ('Recto', 'Gilmore', 5)], 'cost': [0, 21]},
            {'path': [('Recto', 'Recto', 0), ('Doroteo Jose', 'Gil Puyat', 7)], 'cost': [0, 21]},
            {'path': [('J. Ruiz', 'Recto', 4), ('Doroteo Jose', 'Doroteo Jose', 0)], 'cost': [19, 0]},
            {'path': [('Vito Cruz', 'Doroteo Jose', 6), ('Recto', 'Recto', 0)], 'cost': [19, 0]},
            {'path': [('Recto', 'Recto', 0), ('Doroteo Jose', 'Doroteo Jose', 0)], 'cost': [0, 0]},
            {'path': [('Doroteo Jose', 'Doroteo Jose', 0), ('Recto', 'Recto', 0)], 'cost': [0, 0]},
            {'path': [('Katipunan', 'Anonas', 1)], 'cost': [13]},
            {'path': [('Santolan2', 'Marikina', 1)], 'cost': [15]},
            {'path': [('Pureza', 'Betty Go-Belmonte', 4)], 'cost': [19]},
            {'path': [('Araneta-Cubao', 'Legarda', 6)], 'cost': [22]},
            {'path': [('V. Mapa', 'Araneta-Cubao', 4), ('Cubao', 'Taft', 9)], 'cost': [20, 24]},
            {'path': [('North Avenue', 'Cubao', 3), ('Araneta-Cubao', 'Katipunan', 2)], 'cost': [16, 16]},
            {'path': [('Araneta-Cubao', 'Araneta-Cubao', 0), ('Cubao', 'Ortigas', 2)], 'cost': [0, 13]},
            {'path': [('Cubao', 'Cubao', 0), ('Araneta-Cubao', 'Recto', 7)], 'cost': [0, 23]},
            {'path': [('Gilmore', 'Araneta-Cubao', 2), ('Cubao', 'Cubao', 0)], 'cost': [16, 0]},
            {'path': [('Shaw Blvd.', 'Cubao', 3), ('Araneta-Cubao', 'Araneta-Cubao', 0)], 'cost': [16, 0]},
            {'path': [('Kamuning', 'Quezon Avenue', 1)], 'cost': [13]},
            {'path': [('Guadalupe', 'Buendia', 1)], 'cost': [13]},
            {'path': [('Santolan3', 'Magallanes', 7)], 'cost': [20]},
            {'path': [('Boni', 'Taft', 5)], 'cost': [20]},
            {'path': [('Ayala', 'Taft', 2), ('EDSA', 'Blumentritt', 12)], 'cost': [13, 25]},
            {'path': [('Baclaran', 'Doroteo Jose', 10), ('Recto', 'Araneta-Cubao', 7), ('Cubao', 'Ortigas', 2)], 'cost': [23, 23, 13]},
            {'path': [('Cubao', 'Cubao', 0), ('Araneta-Cubao', 'Recto', 7), ('Doroteo Jose', 'Abad Santos', 4)], 'cost': [0, 23, 17]},
            {'path': [('Doroteo Jose', 'Doroteo Jose', 0), ('Recto', 'Araneta-Cubao', 7), ('Cubao', 'North Avenue', 3)], 'cost': [0, 23, 16]},
            {'path': [('Buendia', 'Taft', 3), ('EDSA', 'Doroteo Jose', 9)], 'cost': [16, 23]},
            {'path': [('Tayuman', 'Doroteo Jose', 2), ('Recto', 'Araneta-Cubao', 7), ('Cubao', 'Cubao', 0)], 'cost': [15, 23, 0]},
            {'path': [('Doroteo Jose', 'Doroteo Jose', 0), ('Recto', 'Araneta-Cubao', 7), ('Cubao', 'Cubao', 0)], 'cost': [0, 23, 0]},
            {'path': [('Baclaran', 'Roosevelt', 19)], 'cost': [35]},
            {'path': [('Recto', 'Antipolo', 12)], 'cost': [33]},
            {'path': [('North Avenue', 'Taft', 12)], 'cost': [28]},
        ]
        for i in range(len(self.urls)):
            res = self.client.get(self.urls[i])

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data["path"], answer[i]["path"])
            self.assertEqual(res.data["cost"], answer[i]["cost"])