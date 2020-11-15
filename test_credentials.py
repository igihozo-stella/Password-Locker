import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behavior
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_credentials = Credentials("Facebook","igihozo stella", "56789")

    def test_credentials(self):
        '''
        Method to test whether the new credentials have been instantiated correctly
        '''
        self.assertEqual(self.new_credentials.site_name, "Facebook")
        self.assertEqual(self.new_credentials.account_name,"igihozo stella")
        self.assertEqual(self.new_credentials.account_password, "56789")

    def test_save_credentials(self):
        '''
        Method to tests if the new credential created has been saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        Method that saves multiple credentials to credentials list
        '''
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Instagram","stella_igihozo", "34567")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        '''
        Method that clears the credentials list after every test to ensure that there is no error
        '''
        Credentials.credentials_list = []

    def test_find_credential_by_name(self):
        '''
        Test to check if we can find credentials and display information
        '''
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Instagram","stella_igihozo", "34567")
        new_test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Instagram")

        self.assertEqual(found_credential.site_name, new_test_credential.site_name)

    def test_display_all_credentials(self):
        '''
        Test to test whether all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()