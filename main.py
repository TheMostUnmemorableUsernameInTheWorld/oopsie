from selenium import webdriver
driver = webdriver.Firefox()
body = driver.find_element_by_tag_name('body')
body.keyDown("q", Keys.CONTROL, Keys.SHIFT)
body.keyDown("q", Keys.CONTROL, Keys.SHIFT)
