from django.test import TestCase
from accounts.models import User, Account, Profile
from trees.models import PlantTree, Trees, PlantTree
from django.contrib.messages import get_messages


class AccountsTestCase(TestCase):
    def setUp(self):
        '''accounts'''
        self.account1 = Account(cpf='11111111111', status_account=True)
        self.account1.save()
        self.account2 = Account(cpf='22222222222')
        self.account2.save()
        '''users'''
        self.user1 = User(email='teste@teste.com', password='123')
        self.user1.set_password(self.user1.password)
        self.user1.is_active = True
        self.user1.save()
        self.user2 = User(email='teste2@teste2.com', password='123')
        self.user2.set_password(self.user2.password)
        self.user2.save()    
        self.user3 = User(email='teste3@teste3.com', password='123')
        self.user3.set_password(self.user3.password)
        self.user3.save()            
        '''profiles'''      
        self.profile1 = Profile(first_name='teste1', last_name='last1', user=self.user1)
        self.profile1.save()
        self.profile2 = Profile(first_name='teste2', last_name='last2', user=self.user2)
        self.profile2.save()
        self.profile3 = Profile(first_name='teste3', last_name='last3', user=self.user3)
        self.profile3.save()  
        '''Relationships objects user, account, profile'''
        self.user1.account.set([self.account1])
        self.user2.account.set([self.account2])
        self.user3.account.set([self.account1])
        '''trees'''
        self.trees1 = Trees(name='teste1',alias='teste1')
        self.trees1.save()
        self.trees2 = Trees(name='teste2',alias='teste2')
        self.trees2.save()
        '''trees'''
        self.plant1 = PlantTree(age=1, lt=123.123, lg=123.123, user=self.user1, trees=self.trees1)
        self.plant1.save()
        self.plant2 = PlantTree(age=1, lt=123.123, lg=123.123, user=self.user2, trees=self.trees2)
        self.plant2.save()
        self.plant3 = PlantTree(age=1, lt=123.123, lg=123.123, user=self.user3, trees=self.trees1)
        self.plant3.save()

    def tearDown(self):
        self.plant1.delete()
        self.plant2.delete()
        self.plant3.delete()

        self.trees1.delete()
        self.trees2.delete()
        
        self.profile1.delete()
        self.profile2.delete()
        self.profile3.delete()

        self.user1.delete()
        self.user2.delete()
        self.user3.delete()

        self.account1.delete()
        self.account2.delete()

    def test_total_count_my_plant_trees_user1(self):
        '''test total count tree plants the user'''
        self.client.force_login(self.user1)
        response = self.client.get("/trees/list_plants/?fp=my")
        for tree in response.context["trees"]:
            self.assertEqual(tree.count_plant, 1)

    def test_total_count_all_plant_trees_user1(self):
        '''Teste total tree plants user accounts'''
        self.client.force_login(self.user1)
        response = self.client.get("/trees/list_plants/?fp=all")
        for tree in response.context["trees"]:
            self.assertEqual(tree.count_plant, 2)
    
    def test_context_render_my_plants_tree_user1(self):
        '''test render all plants tree user'''
        self.client.force_login(self.user1)
        response = self.client.get(f"/trees/detail_plants/{self.trees1.pk}/my/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['plants']), 1)
        for plant in response.context["plants"]:
            self.assertEqual(plant.user, self.user1)
    
    def test_context_render_all_plants_trees_user1(self):
        '''test render all plants tree members account'''
        self.client.force_login(self.user1)
        response = self.client.get(f"/trees/detail_plants/{self.trees1.pk}/all/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['plants']), 2)
        for plant in response.context["plants"]:
            self.assertQuerysetEqual(plant.user.account.all(), self.user1.account.all())
            self.assertQuerysetEqual(plant.user.account.all(), self.user3.account.all())

    def test_302_user_is_active_false_redirect_login(self):
        '''test 302 redirect login'''
        self.account2.status_account = True
        self.account2.save()
        self.client.force_login(self.user2)
        response = self.client.get("/trees/list_plants/?fp=all")
        self.assertEqual(response.url, '/accounts/sign_out/')
        self.assertEqual(response.status_code, 302)

    def test_302_status_account_false_redirect_login(self):
        '''test 302 status account False'''
        self.user2.is_active = True
        self.user2.save()
        self.client.force_login(self.user2)
        response = self.client.get("/trees/list_plants/?fp=all")
        self.assertEqual(response.url, '/accounts/sign_out/')
        self.assertEqual(response.status_code, 302)
    
    def test_multiples_plants_tree(self):
        '''test add multiples plants tree'''
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
