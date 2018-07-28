from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome('chromedriver.exe')#chrome(r'C:\path)
browser.get('http://www.python.org')
if 'Python' in browser.title:
    print('Open successful')
else:
    print('Page load failed')
field=browser.find_element_by_name('q')
'''r='''
field.send_keys('python')
#print(r)
field.send_keys(Keys.RETURN)

if 'No Result' in browser.page_source:
    print('Not able to search')

print(browser.page_source)


