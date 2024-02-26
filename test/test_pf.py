from pa_lib.webdriver import get_browser, free_browser


# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestX():
	def setup_method(self, method):
		self.driver= get_browser()
		self.vars= {}

	def teardown_method(self, method):
		self.driver= None
		free_browser()

	def test_x(self):
		self.driver.get("https://www.bbva.com.ar/simulador-plazo-fijo/")
		self.driver.set_window_size(1333, 704)
		self.driver.find_element(By.ID, "option-no").click()
		self.driver.find_element(By.ID, "option-pesos").click()
		self.driver.find_element(By.CSS_SELECTOR, "label").click()
		self.driver.find_element(By.ID, "text-24").send_keys("$ 100.000")
		self.driver.find_element(By.CSS_SELECTOR, ".diasContainer:nth-child(1) > .mobile:nth-child(1) .font").click()
		WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".p-table-title:nth-child(2)"), "Interés ganado"))

		time.sleep(20)

		interes = self.driver.find_element(By.CSS_SELECTOR, ".tna__value > .span-importe").text

		with open('resultados/pf.txt','ta') as fout:
			fout.write(f'{interes}\n')

		dst_fname= 'resultados/x_ej_screenshot_pf.png'
		self.driver.save_screenshot(dst_fname)
		print(f'Screenshot guardado como {dst_fname}')
