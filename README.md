<h1>Шаблоны curl запросов для проверки работоспособности</h1>
<p>1. Регистрация: curl -X POST "http://127.0.0.1:8000/register" -H "Content-Type: application/json" -d "{\"username\": \"ИМЯ\", \"password\": \"ПАРОЛЬ\"}"</p>
<p>2. Аутентификация(выданный токен будет действителен в течение 30 минут): curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/json" -d "{\"username\": \"ИМЯ\", \"password\": \"ПАРОЛЬ\"}"</p>
<p>3. Добавление заметки(тело заметки проверяется на орфографию): curl -X POST "http://127.0.0.1:8000/notes/" -H "Content-Type: application/json" -H "Authorization: Bearer ТОКЕН" -d "{\"title\": \"Заголовок заметки\", \"body\": \"Тело заметки\"}"</p>
<p>4. Вывод всех заметок пользователя: curl -X GET "http://127.0.0.1:8000/notes/" -H "Content-Type: application/json" -H "Authorization: Bearer ТОКЕН"</p>
<p>5. Удаление заметки: curl -X DELETE "http://127.0.0.1:8000/notes/id_заметки" -H "Content-Type: application/json" -H "Authorization: Bearer ТОКЕН"</p>
<p>6. Редактирование заметки: curl -X PUT "http://127.0.0.1:8000/notes/id_заметки" -H "Content-Type: application/json" -H "Authorization: Bearer ТОКЕН"</p>