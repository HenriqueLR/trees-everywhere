from tests import BaseTest



class UrlAccountsTests(BaseTest):
    
    def test_url_sign_in(self):
        '''
        test return 200 login url 
        '''
        response = self.client.get("/accounts/sign_in/")
        self.assertEqual(response.status_code, 200)

    def test_url_sign_out(self):
        '''
        test return 302 redirect logout
        '''
        self.client.force_login(self.user1)
        response = self.client.get("/accounts/sign_out/")
        self.assertEqual(response.url, "/accounts/sign_in/")
        self.assertEqual(response.status_code, 302)


class UrlApiTests(BaseTest):
    
    def test_url_api_list_my_plants(self):
        '''
        test return 200 api url
        '''
        self.client.force_login(self.user1)
        response = self.client.get("/api/v1/trees/list_my_plants/")
        self.assertEqual(response.status_code, 200)


class UrlTreesTests(BaseTest):

    def test_url_list_plants(self): 
        '''
        test return 200 list plants url
        '''
        self.client.force_login(self.user1)
        response = self.client.get("/trees/list_plants/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_plant_tree(self):
        '''
        test return 200 plant tree url
        '''
        self.client.force_login(self.user1)
        response = self.client.get(f"/trees/plant_tree/{self.trees1.pk}/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_add_tree(self):
        '''
        test return 200 add tree url
        '''
        self.client.force_login(self.user1)
        response = self.client.get("/trees/add_tree/")
        self.assertEqual(response.status_code, 200) 
    
    def test_url_list_trees(self):
        '''
        test return 200 list trees url
        '''
        self.client.force_login(self.user1)
        response = self.client.get("/trees/list_trees/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_detail_plnats(self):
        '''
        test return 200 detail plants url
        '''
        self.client.force_login(self.user1)
        response = self.client.get(f"/trees/detail_plants/{self.trees1.pk}/my/")
        self.assertEqual(response.status_code, 200)
