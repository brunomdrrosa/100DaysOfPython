from selenium import webdriver

chrome_driver_path = "C:/Users/bruno/OneDrive/Documentos/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

dia_eventos = driver.find_elements_by_css_selector(".event-widget time")
nome_eventos = driver.find_elements_by_css_selector(".event-widget li a")

eventos = {}
for n in range(len(dia_eventos)):
    eventos[n] = {
        "time": dia_eventos[n].text,
        "name": nome_eventos[n].text,
    }

print(eventos)