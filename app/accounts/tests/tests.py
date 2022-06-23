from django.test import TestCase
from accounts.models import User, Account, Profile


class AccountsTestCase(TestCase):
    def setUp(self):
        self.account = Account(cpf='11111111111')
        self.account.save()
        self.user = User(email='teste@teste.com', password='123')
        self.user.set_password(self.user.password)
        self.user.save()
        self.user.account.set([self.account])
        self.profile = Profile(first_name='teste first', last_name='teste last', user=self.user)
        self.profile.save()

    def tearDown(self) -> None:
        self.account.delete()
        self.user.delete()
        self.profile.delete()
        return super().tearDown()

    def test_create_account(self):
        '''TestCase for creating a new account'''
        self.assertEqual(Account.objects.get(pk=1), self.account)

    def test_status_account(self):
        '''TestCase for check default status account'''
        self.assertAlmostEqual(self.account.status_account, False)

    def test_create_user(self):
        '''TestCase for creating a new user'''
        self.assertEqual(User.objects.get(pk=1), self.user)
    
    def test_status_is_active_user(self):
        '''Test status is active username default false'''
        self.assertEqual(self.user.is_active, False)
    
    def test_status_is_staff_user(self):
        '''Test status is staff username default false'''
        self.assertEqual(self.user.is_staff, False)
    
    def test_status_is_superuser_user(self):
        '''Test status is superuser username default false'''
        self.assertEqual(self.user.is_superuser, False)
    
    def test_relationship_account_user(self):
        '''Test relationship is account user'''
        self.assertEqual(self.user.account.all().first(), self.account)
    