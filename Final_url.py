from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import os

def extract_final_google_maps_url(short_url):
    try:
        options = Options()
        options.add_argument("--headless")  # Запуск браузера в фоновом режиме
        driver_path = os.path.join(os.path.dirname(__file__), 'webdriver', 'msedgedriver.exe')
        service = Service(driver_path)
        driver = webdriver.Edge(service=service, options=options)
        driver.get(short_url)
        driver.implicitly_wait(10) # Ожидание загрузки страницы
        final_url = driver.current_url
        driver.quit()
        return final_url

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

short_url = str(input("Введите ссылку: ")) # Потом можно будет заменить на текстовую ссылку или функцию.
final_google_maps_url = extract_final_google_maps_url(short_url)

if final_google_maps_url:
    print(f"\nНайденная ссылка на Google Maps: {final_google_maps_url}")
else:
    print("\nНе удалось извлечь ссылку на Google Maps.")
