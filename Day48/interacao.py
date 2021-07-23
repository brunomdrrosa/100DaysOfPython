from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/bruno/OneDrive/Documentos/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# numero_artigos = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Bruno")

first_name = driver.find_element_by_name("lName")
first_name.send_keys("Machado")

first_name = driver.find_element_by_name("email")
first_name.send_keys("brunomdr46@gmail.com")

botao = driver.find_element_by_tag_name("button")
botao.click()
