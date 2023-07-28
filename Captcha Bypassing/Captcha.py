from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

connection = webdriver.Chrome(executable_path='/Users/aleksei.semerikov/Downloads/chromedriver')
cita = connection.get('http://www.valencia.es/QSIGE/apps/citaprevia/index.html?idioma=VA#!/newAppointment/75')
connection.implicitly_wait(0.5)

###check Tabacalera
service_select = Select(connection.find_element_by_xpath('//*[@id="servicios"]'))
service_select.select_by_visible_text('PADRON CP - OAC Tabacalera')

name=connection.find_element_by_xpath('//*[@id="nameInput"]').send_keys('Aleksei')
surname = connection.find_element_by_xpath('//*[@id="surnameInput"]').send_keys('Semerikov')


document_type = Select(connection.find_element_by_xpath('//*[@id="tipoDocumentos"]'))
connection.implicitly_wait(0.5)
document_type.select_by_visible_text('NIF/NIE')
NIE = connection.find_element_by_xpath('//*[@id="nifInput"]').send_keys('Y9891004Y')
phone = connection.find_element_by_xpath('//*[@id="tlfnoInput"]').send_keys('695112263')
email = connection.find_element_by_xpath('//*[@id="emailInput"]').send_keys('a.semerikov1@gmail.com')



#
# connection.implicitly_wait(0.5)
# centro_select = Select(connection.find_element_by_xpath('//*[@id="centros"]'))
# connection.implicitly_wait(0.5)
# centro_select.select_by_index(1)
# ##if error than break
# connection.implicitly_wait(0.5)
# if connection.find_element_by_xpath('//*[@id="ngdialog5"]/div[2]').get_attribute('class')=='ngdialog-content':
#     sleep(10)
#     connection.close()






