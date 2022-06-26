from tests import BaseTest
from django.contrib.messages import get_messages



class ContextViewTests(BaseTest):

    def test_total_count_my_plant_trees_user1(self):
        '''
        total test of trees planted by the user
        '''
        self.client.force_login(self.user1)
        response = self.client.get("/trees/list_plants/?fp=my")
        for tree in response.context["trees"]:
            self.assertEqual(tree.count_plant, 1)

    def test_total_count_all_plant_trees_user1(self):
        '''
        total test of trees planted by accounts
        '''
        self.client.force_login(self.user1)
        response = self.client.get("/trees/list_plants/?fp=all")
        for tree in response.context["trees"]:
            self.assertEqual(tree.count_plant, 2)
    
    def test_context_render_my_plants_tree_user1(self):
        '''
        test return context trees planted by the user
        '''
        self.client.force_login(self.user1)
        response = self.client.get(f"/trees/detail_plants/{self.trees1.pk}/my/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['plants']), 1)
        for plant in response.context["plants"]:
            self.assertEqual(plant.user, self.user1)
    
    def test_context_render_all_plants_trees_user1(self):
        '''
        test return context trees planted by accounts
        '''
        self.client.force_login(self.user1)
        response = self.client.get(f"/trees/detail_plants/{self.trees1.pk}/all/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['plants']), 2)
        for plant in response.context["plants"]:
            self.assertQuerysetEqual(plant.user.account.all(), self.user1.account.all())
            self.assertQuerysetEqual(plant.user.account.all(), self.user3.account.all())

    def test_multiples_plants_tree(self):
        '''
        test add multiples trees planted
        '''
        self.client.force_login(self.user1)
        data = {'csrfmiddlewaretoken': ['KjjrTXL3rnAwx1Enr1UhfvKVnSxkTPKBC6D5yiFIqVWej0X0g1mOCVSz10sK5tls'], 
                'form-TOTAL_FORMS': ['3'], 'form-INITIAL_FORMS': ['0'], 'form-MIN_NUM_FORMS': ['0'], 
                'form-MAX_NUM_FORMS': ['1000'], 
                'form-0-age': ['1'], 'form-0-lt': ['123.123'], 'form-0-lg': ['123.123'], 
                'form-1-age': ['1'], 'form-1-lt': ['123.123'], 'form-1-lg': ['123.123'], 
                'form-2-age': ['1'], 'form-2-lt': ['123.123'], 'form-2-lg': ['123.123']}
        response = self.client.post(f"/trees/plant_tree/{self.trees1.pk}/", data)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Tree planted', messages)
        self.assertEqual(response.status_code, 302)                
        self.assertEqual(response.url, '/trees/list_plants/')
