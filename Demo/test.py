from selenium import webdriver

# initiating the chrome drivers **Note first verify the chrome driver version and download the
driver = webdriver.Chrome(r"D:\Data\Learning0249\Selenium Using Python\Drivers\chromedriver_win32\chromedriver.exe")

# getting the required website on drivers where we want to find the elements
# this will also launch the link
driver.get(r"https://www.imdb.com/")

# finding the required search element by id
# find element by name
# find element using link this type of locator helps in identifying hyperlink texts
# find element using the css selector using "#"
# find element using partial link text
# find element using XPATH
driver.find_element_by_name("q").send_keys("lucy")
driver.find_element_by_id("suggestion-search-button").click()


