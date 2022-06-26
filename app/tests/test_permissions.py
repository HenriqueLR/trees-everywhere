from tests import BaseTest



class LoginRequiredTests(BaseTest):

    def test_url_api_my_plants(self):
        '''
        test return 403 not authenticated user
        '''
        response = self.client.get("/api/v1/trees/list_my_plants/")
        self.assertEqual(response.status_code, 403)
    
    def test_url_list_plants(self):
        '''
        test return 302 redirect login not authenticated
        '''
        response = self.client.get("/trees/list_plants/")
        self.assertEqual(response.url, "/accounts/sign_out/")
        self.assertEqual(response.status_code, 302)        
    
    def test_url_plant_tree(self):
        '''
        test return 302 redirect login not authenticated
        '''        
        response = self.client.get(f"/trees/plant_tree/{self.trees1.pk}/")
        self.assertEqual(response.url, "/accounts/sign_out/")
        self.assertEqual(response.status_code, 302)

    def test_url_add_tree(self):
        '''
        test return 302 redirect login not authenticated
        '''        
        response = self.client.get("/trees/add_tree/")
        self.assertEqual(response.url, "/accounts/sign_out/")
        self.assertEqual(response.status_code, 302)
    
    def test_url_list_trees(self):
        '''
        test return 302 redirect login not authenticated
        '''        
        response = self.client.get("/trees/list_trees/")
        self.assertEqual(response.url, "/accounts/sign_out/")
        self.assertEqual(response.status_code, 302)
    
    def test_url_detail_plnats(self):
        '''
        test return 302 redirect login not authenticated
        '''        
        response = self.client.get(f"/trees/detail_plants/{self.trees1.pk}/my/")
        self.assertEqual(response.url, "/accounts/sign_out/")
        self.assertEqual(response.status_code, 302)


class StatusAccountTests(BaseTest):

    def test_status_account_permissions(self):
        '''
        test status account False not allowed access
        '''
        self.account2.status_account = True
        self.account2.save()
        self.client.force_login(self.user2)
        response = self.client.get("/trees/list_plants/?fp=all")
        self.assertEqual(response.url, '/accounts/sign_out/')
        self.assertEqual(response.status_code, 302)


class StatusIsActiveUserTests(BaseTest):

    def test_satus_is_active_user_permissions(self):
        '''
        test status user is active False not allowed access
        '''
        self.user2.is_active = True
        self.user2.save()
        self.client.force_login(self.user2)
        response = self.client.get("/trees/list_plants/?fp=all")
        self.assertEqual(response.url, '/accounts/sign_out/')
        self.assertEqual(response.status_code, 302)
      