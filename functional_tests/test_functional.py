from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewVisitorTestCase(StaticLiveServerTestCase):
    
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()


	def test_can_register_new_user_on_site(self):
		
		# Bob find out Fisherman Diary in Internet
		# he wants to try out this diary. But before
		# he can try it out he must register and log in. 
		# Bob visits the main page of our site.
		main_page = self.browser.get(self.live_server_url + '/')
		
		# He seeing the link to log in and the link Register
		# on the page. He press the link and he goes to registration
		# page. He enters his username, password and confirm password.
		# After that he press Register button in the bottom of the
		# form.
		self.browser.find_element_by_id('id_registration').click()
		self.browser.find_element_by_id('id_login_form')
		username = self.browser.find_element_by_id('id_username')
		username.send_keys('fisherman-bob')
		password1 = self.browser.find_element_by_id('id_password1')
		password1.send_keys('BoBfish23')
		password2 = self.browser.find_element_by_id('id_password2')
		password2.send_keys('BoBfish23')
		self.browser.find_element_by_tag_name('button').submit()
		
		# He seeing message that says that Bob is successfuly
		# register on Diary site. He sees link "Make new post"
		# and link "Go to Diary" rigth after message of registration.
		# Bob goes to main page.
		self.browser.get(self.live_server_url + '/registration/register-complete/')
		text_message = self.browser.find_element_by_tag_name('p')
		self.assertEqual(text_message.text, 'You are successfuly register on Fisherman Diary!')
		new_post_link = self.browser.find_element_by_link_text('Make new post')
		self.assertEqual(new_post_link.text, 'Make new post')
		main_page_link = self.browser.find_element_by_link_text('Go to Diary')
		self.assertEqual(main_page_link.text, 'Go to Diary')
		main_page_link.click()
		# Bob is login to Fisherman Diary right after registration.
		# He knows that because he see his username in top right
		# corner of the screen.
		username_link = self.browser.find_element_by_id('auth_username')
		self.assertEqual(username_link.text, 'fisherman-bob')

"""
	def test_can_start_a_note_and_retrieve_it_later(self):
        
		# Bob is a fisherman. He often goes fishing and he want's to
		# note everything that happens that day.
		# He want to see date of fishing, and text area to make notes like
		# in diary.

		# Bob has heard about cool new diary for fisherman. He goes to its site to check it out
		self.browser.get(self.live_server_url + '/')

		# He notices the page title 'Fisherman Diary'
		self.assertIn('Fisherman Diary', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Fisherman Diary', header_text)

		# He is invited to enter a new note in diary
		form_note = self.browser.find_element_by_id('id_form_note')
		title = self.browser.find_element_by_id('id_new_title')
		self.assertEqual(title.get_attribute('placeholder'), 'Enter a title')
		date = self.browser.find_element_by_id('id_new_date')
		self.assertEqual(date.get_attribute('placeholder'), 'Enter a date')
		note = self.browser.find_element_by_id('id_new_note')
		self.assertEqual(note.get_attribute('placeholder'), 'Enter a note')

		# He types 'Today was a good day to fishing. I had catch five trouts and one harius.
		# The weather was cloudly, temperature 20 degree per celcium. West wind.' to
		# the text field.
		# He types 'Fishing near Havrontsy' to the title text field.
		# Bob enters date of fishing '21.04.2015'
		title.send_keys('Fishing near Havrontsy')
		date.send_keys('21.04.2015')
		text = 'Today was a good day to fishing. I had catch five trouts and one harius. The weather was cloudly, temperature 20 degree per celcium. West wind.'
		note.send_keys(text)

		# When he press button 'Save', the page updates and now the page list contains 
		# '21.04.2015: Fishing near Havrontsy'.
		button = self.browser.find_element_by_id('id_save_button')
		button.click()

		table = self.browser.find_element_by_id('id_notes_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == '21.04.2015 Fishing near Havrontsy' for row in rows))

		# There is still a form that inviting to add one more note. He enters
		# 'Fishing was awesome. Many many trouts was catched throughout 2 hours.'
		# Title 'Wild trout', date '05.06.2015'
		self.fail('Incomplete test')


		# The page updates again, and now shows both notes on the page.


		# Bobs wonders whether the site will remember his list. Then he sees
		# that the site has generated a unique URL for him -- there is some
		# explanatory text to that effect.
		# He visits that URL - his diary notes is still there.
		# Satisfied, he goes back to sleep.
"""

