import pandas as pd
import matplotlib.pyplot as plt


# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

df = pd.DataFrame(data)
print(f"Средняя цена - {df['Price'].mean():.2f} руб.")

# Столбец с ценами называется 'price'
prices = data['Price']



# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()