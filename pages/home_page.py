# home_page.py

from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver  # WebDriver nesnesini sakla
        self.company_menu = (By.XPATH, "//a[@id='navbarDropdownMenuLink']")  # Şirket menüsünün XPath'ini tanımla
        self.careers_link = (By.LINK_TEXT, "Careers")  # Kariyer bağlantısının metnine göre bul

    def navigate_to_careers(self):
         # Ana menü öğesine tıkla
        company_menu_element = self.driver.find_element(*self.company_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(company_menu_element).perform()  # Submenüyü açmak için hover yap. Çünkü Careers sayfası; Company ana menüsünün içerisinde mause ile üstüne geldiğimizde açılan bir submenü.

        # Kariyer bağlantısının görünür olmasını bekle. Burada da mause ile üstüne geldiğimizde submenünün açılmasını beklemeyi simüle ediyoruz.
        careers_element = WebDriverWait(self.driver, 10).until( # Burada time.sleep(n) de kullanabilirdim. Ancak işimi garantiye alıyorum.
            EC.visibility_of_element_located(self.careers_link)
        )
        careers_element.click()  # Kariyer sayfasına yönlendir