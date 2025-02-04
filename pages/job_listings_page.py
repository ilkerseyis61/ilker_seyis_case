#job_listings_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class JobListingsPage:
    def __init__(self, driver):
        self.driver = driver  # WebDriver nesnesini sakla
        self.location_filter = (By.XPATH, "//select[@id='filter-by-location']")  # Lokasyon filtresi XPath'i
        self.department_filter = (By.XPATH, "//select[@id='filter-by-department']")  # Departman filtresi XPath'i
        self.view_role_buttons = (By.XPATH, "//a[contains(text(),'View Role')]")  # "View Role" düğmesi XPath'i

    def apply_filters(self, location, department):
        self.driver.find_element(*self.location_filter).send_keys(location)  # Lokasyon filtresini uygula
        self.driver.find_element(*self.department_filter).send_keys(department)  # Departman filtresini uygula
        # Burada zaten filtreleme yaptıktan sonra otomatik filtrelenen iş ilanları gözükmeye başlıyor. Bir şey yapmamıza gerek yok.

    def verify_jobs_list(self):
        jobs = self.driver.find_elements(By.CLASS_NAME, "job-item")  # İş ilanlarını listele
        assert len(jobs) > 0, "İş ilanı bulunamadı!"  # İş ilanı olup olmadığını kontrol et
        for job in jobs:
            assert "Quality Assurance" in job.text, "İş ilanı kriterlere uymuyor"  # İlanların kriterlere uygun olup olmadığını kontrol et

    def click_view_role(self):
        # İş ilanını bul
        job_item = self.driver.find_element(By.CLASS_NAME, "job-item")  # İş ilanının genel alanını bul
        actions = ActionChains(self.driver)
        actions.move_to_element(job_item).perform()  # Fareyi iş ilanı öğesinin üzerine getir

        # "View Role" butonuna tıkla
        self.driver.find_element(*self.view_role_buttons).click()  # "View Role" düğmesine tıkla
        # Sayfanın yönlendirildiğini kontrol et
        time.sleep(2)  # Sayfanın yüklenmesi için kısa bir bekleme ekledik
        current_url = self.driver.current_url  # Şu anki URL'yi al
        assert current_url.startswith("https://jobs.lever.co/"), f"Beklenen URL'ye yönlendirilmedi. Mevcut URL: {current_url}"