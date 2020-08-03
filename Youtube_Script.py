# please read the help file to make this script wotrk.
from selenium import webdriver
import time
import getpass
from selenium.webdriver.common.keys import Keys
PATH = 'C:\\Users\\ad\\Desktop\\selenium\\chromedriver.exe' #here you will enter the chrome driver path
driver = webdriver.Chrome(PATH)
driver.get('https://youtube.com')
user_inpt = input('Please enter yes')
if(user_inpt=='yes'):
	counter = True
	while(counter):
		driver.get('https://www.youtube.com/watch?v=N0MHgEVttgE') #here you will enter your video link
		time.sleep(3)
		views= driver.find_element_by_css_selector('span.view-count.style-scope.yt-view-count-renderer')
		view_count = views.get_attribute('innerHTML').split(' ')[0]
		title_of_video = driver.find_elements_by_class_name('ytd-video-primary-info-renderer')[0]
		title_of_video_views = title_of_video.get_attribute('innerHTML').split(' ')[3]
		if not title_of_video == title_of_video_views:
			driver.get('https://studio.youtube.com/video/N0MHgEVttgE/edit') #here you will share the edit video path for your video
			time.sleep(2)
			title_element = driver.find_element_by_css_selector('div#textbox.style-scope.ytcp-mention-textbox')
			for i in range(0,50):
				title_element.send_keys(Keys.BACK_SPACE)
			title_element.send_keys(f'This Video Has {int(view_count)} Views')
			time.sleep(2)
			#html_head = driver.find_element_by_tag_name('html')
			#html_head.send_keys(Keys.TAB)
			element = driver.find_element_by_css_selector('dom-if.style-scope.ytcp-button')
			actions = webdriver.ActionChains(driver)
			tab_key = actions.send_keys(Keys.TAB)
			for i in range (1,44):
				tab_key.perform()
			tab_key = actions.send_keys(Keys.RETURN)
			tab_key.perform()
			time.sleep(3)
