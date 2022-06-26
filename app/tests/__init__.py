from django.test import TestCase
from accounts.models import User, Account, Profile
from trees.models import Trees, PlantTree


class BaseTest(TestCase):

    
    def setUp(self):
        '''accounts'''
        self.account1 = Account(cpf='11111111111', status_account=True)
        self.account1.save()
        self.account2 = Account(cpf='22222222222')
        self.account2.save()
        '''users'''
        self.user1 = User(email='test@test.com', password='123')
        self.user1.set_password(self.user1.password)
        self.user1.is_active = True
        self.user1.save()
        self.user2 = User(email='test2@test2.com', password='123')
        self.user2.set_password(self.user2.password)
        self.user2.save()    
        self.user3 = User(email='test3@test3.com', password='123')
        self.user3.set_password(self.user3.password)
        self.user3.save()            
        '''profiles'''      
        self.profile1 = Profile(first_name='first1', last_name='last1', user=self.user1)
        self.profile1.save()
        self.profile2 = Profile(first_name='first2', last_name='last2', user=self.user2)
        self.profile2.save()
        self.profile3 = Profile(first_name='first3', last_name='last3', user=self.user3)
        self.profile3.save()  
        '''Relationships objects user, account, profile'''
        self.user1.account.set([self.account1])
        self.user2.account.set([self.account2])
        self.user3.account.set([self.account1])
        '''trees'''
        self.trees1 = Trees(name='tree1',alias='tree1')
        self.trees1.save()
        self.trees2 = Trees(name='tree2',alias='tree2')
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
        
        return super().tearDown()