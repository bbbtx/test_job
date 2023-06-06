#Для запусков контейнера с тестами потребуется выполнить команду
(выполняется из корневой папки, в которой лежит репозиторий) 
docker-compose up --build -d 

Для запусков тестов с полным отображением вывода потребуется выполнить:
docker exec -it jenkins-lts bash -c 'pytest -rA /usr/local/tests'

Для заупсков тестов с кратким отображением вывода потребуется выполнить:
docker exec -it jenkins-lts bash -c 'pytest -rA --tb=no /usr/local/tests'

#Так же можно запустить тестирования при помощи Jenkins 
Необходимо зайти из браузера по следущему адресу:

localhosts:8080
Логин admin
Пароль admin

Появится меню на котором нужно перейти на страницу Server test
<img width="1437" alt="Pasted Graphic" src="https://github.com/bbbtx/test_job/assets/67200856/b6ec6015-2dfd-4d01-b946-8504071ea134">

Затем запустить тест при помощи кнопки "Собрать сейчас"
<img width="1356" alt="Pipeline Server test" src="https://github.com/bbbtx/test_job/assets/67200856/58528fc4-f2b4-49a6-960c-d652bbb5cf5c">

После выполнения тестов можно зайти в результат выполнения сборки и перейдя в "Console output" увидеть лог тетсирования
<img width="949" alt="Pasted Graphic 4" src="https://github.com/bbbtx/test_job/assets/67200856/38b97423-1a9b-4ce9-a03f-496072eb0851">

<img width="805" alt="(Pipeline) Start" src="https://github.com/bbbtx/test_job/assets/67200856/207f34b6-5286-4351-a2d6-a420e26d39da">
