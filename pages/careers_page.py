# careers_page.py

from selenium.webdriver.common.by import By

class CareersPage:
    def __init__(self, driver):
        self.driver = driver  # WebDriver nesnesini sakla
        # Eğer metnin doğrudan ID'si yoksa ki yok. Site üzerinde yaptığım aramları text file olarak arama yapıyorum.
        self.locations_section = (By.XPATH, "//div[contains(text(),'Locations')]")  # Locations metnini içerir
        self.teams_section = (By.XPATH, "//div[contains(text(),'Teams')]")  # Takımlar metnini içerir
        self.life_at_insider_section = (By.XPATH, "//div[contains(text(),'Life at Insider')]")  # Life at Insider metnini içerir
        self.qa_jobs_button = (By.ID, "btn btn-info rounded mr-0 mr-md-4 py-3")  # Butonun ID'si ile bul. Find your dream job idsi bu "btn btn-info rounded mr-0 mr-md-4 py-3"

    def verify_sections_displayed(self):
        # Konumlar bölümünü kontrol et (metin bazlı)
        locations_text = self.driver.find_element(*self.locations_section).text
        assert locations_text, "Locations bölümü bulunamadı."
        
        # Takımlar bölümünü kontrol et (metin bazlı)
        teams_text = self.driver.find_element(*self.teams_section).text
        assert teams_text, "Teams bölümü bulunamadı."
        
        # Insider'da Yaşam bölümünü kontrol et (metin bazlı)
        life_at_insider_text = self.driver.find_element(*self.life_at_insider_section).text
        assert life_at_insider_text, "Life at Insider bölümü bulunamadı."

    def go_to_qa_jobs(self):
        self.driver.find_element(*self.qa_jobs_button).click()  # QA iş ilanları sayfasına git