# Задание 3
# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Настройка веб-драйвера
driver = webdriver.Chrome()

# Открываем страницу
url = 'https://www.divan.ru/samara/category/divany-i-kresla'
driver.get(url)

# Ждем, чтобы страница загрузилась
time.sleep(5)  # Рекомендуется использовать WebDriverWait вместо sleep для более надежного кода

# Получаем элементы с ценами
prices = driver.find_elements(By.CLASS_NAME, 'KIkOH')
print(f'Цены на диваны: {prices}')  # Выводим цены на диваны в консоль (prices)
# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()