from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrive_it_later(self):

		self.browser.get('http://localhost:8000')

		print(self.browser.title)
		self.asserIn('To-Do', self.browser.title)
		self.fail('Finish the test!')



		# She is invited to enter a to-do item straight away


if __name__ == '__main__':
	unittest.main(warnings='ignore')
# She types "Buy peackock feathers" int a text box (Edith's hobby
# is tying fly-fishing lures)

# When she hits enter, the page udpates, and now the page lists
# "1: Buy peackock feather's" as an item in a to-do list

# THere is still a text box inviting her to add another item. She
# She enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page update again, and now shows both item on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique ULR for her -- there is same
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

