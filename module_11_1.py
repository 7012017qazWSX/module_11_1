import requests

# URL для запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Отправка GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Вывод данных в консоль
    data = response.json()  # Преобразование ответа в JSON
    for post in data:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")
else:
    print(f"Ошибка при запросе данных: {response.status_code}")