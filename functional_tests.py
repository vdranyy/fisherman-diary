from selenium import webdriver
import unittest


class NewVisitorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_note_and_retrieve_it_later(self):
        
        # Bob is a fisherman. He often goes fishing and he want's to
        # note everything that happens that day.
        # He want to see date of fishing, and text area to make notes like
        # in diary.


        # Bob has heard about cool new diary for fisherman. He goes to its site to check it out

        self.browser.get('http://localhost:8000')

        # He notices the page title 'Fisherman Diary'

        self.assertIn('Fisherman Diary', self.browser.title)
        self.fail('Incomplete test')

        # He is invited to enter a new note in diary


        # He types 'Today was a good day to fishing. I has catch five trouts and one harius.
        # The weather was cloudly, temperture 20 degree per celcium. Wind was from west.' to
        # the text field.
        # He types 'Fishing near Havrontsy' to the title text field.
        # Bob enters date of fishing '21.04.2015'

        # When he press button 'Save', the page updates and now the page list contains 
        # '21.04.2015: Fishing near Havrontsy'.


        # There is still a form that inviting to add one more note. He enters
        # 'Fishing was awesome. Many many trouts was catched throughout 2 hours.'
        # Title 'Wild trout', date '05.06.2015'


        # The page updates again, and now shows both notes on the page.


        # Bobs wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.
        # He visits that URL - his diary notes is still there.
        # Satisfied, he goes back to sleep.
if __name__ == '__main__':
   unittest.main()
