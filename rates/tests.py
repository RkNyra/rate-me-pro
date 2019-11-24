from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


#Testing the profile module
class ProfileTestClass(TestCase):
    
    #setUpMethod
    def setUp(self):
        self.chyle = Profile(bio='Pilot', contact='123457890', user_id=1)
        self.user = User.objects.create_user(id=1, username='cyle', email='cyle@gmail.com', password='chylesecret')
    
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.chyle,Profile))
        
    #testing the save method
    def test_save_method(self):
        self.chyle.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
    #testing profile update
    # def test_update_method(self):
    #     prof = Profile.objects.create(bio='Pilot')
    #     Profile.objects.filter(pk=prof.pk).update(bio='Snr Dev')
    #     prof.save()
    #     self.assertEqual(prof.bio, 'Snr Dev')
    

    def test_update_method(self):
        self.chyle.save()
        new_bio = 'Snr Dev'
        updated = self.chyle.update_bio(self.chyle.id,new_bio)
        self.assertEqual(updated,new_bio)
