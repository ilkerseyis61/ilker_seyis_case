#test_insider.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.job_listings_page import JobListingsPage

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Chrome WebDriver'ı başlat
    driver.get("https://useinsider.com/")  # Insider ana sayfasını aç
    driver.maximize_window()  # Tarayıcı penceresini büyüt
    
    assert "Insider" in driver.title, "Ana sayfa yüklenmedi!"  # Ana sayfanın yüklendiğini doğrula
    
    home_page = HomePage(driver)
    home_page.navigate_to_careers()  # Kariyer sayfasına git
    
    careers_page = CareersPage(driver)
    careers_page.verify_sections_displayed()  # Kariyer sayfasındaki bölümleri kontrol et
    careers_page.go_to_qa_jobs()  # QA iş ilanları sayfasına git
    
    jobs_page = JobListingsPage(driver)
    jobs_page.apply_filters("Istanbul, Turkey", "Quality Assurance")  # İstanbul ve QA filtrelerini uygula
    jobs_page.verify_jobs_list()  # İş ilanlarının listelendiğini doğrula
    jobs_page.click_view_role()  # İlk iş ilanına tıkla
    
    assert "lever.co" in driver.current_url, "Yönlendirme başarısız!"  # Yönlendirme işlemini doğrula
    
    driver.quit()  # Tarayıcıyı kapat
