from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import os
# class check_availability:
#
#     def main_scipt(self):
#         exec_path = '/Users/aleksei.semerikov/PycharmProjects/CHECK_RESIDENCE_SLOT/chromedriver'
        # os.environ["webdriver.chrome.driver"] = exec_path
driver = webdriver.Chrome(executable_path='/Users/aleksei.semerikov/PycharmProjects/CHECK_RESIDENCE_SLOT/chromedriver')
driver.get('https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus')
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="submit"]').click()
city_select = Select(driver.find_element_by_xpath('//*[@id="form"]'))
city_select.select_by_visible_text('Valencia')
driver.implicitly_wait(5)
# driver.find_element_by_xpath('//*[@id="btnAceptar"]').click()
        # oficina_select = Select(driver.find_element_by_xpath('//*[@id="sede"]'))
        # oficina_select.select_by_index(7)
        # sleep(5)
        # driver.close()




# if __name__ == '__main__':
#     check1 = check_availability()
#     check1.main_scipt()