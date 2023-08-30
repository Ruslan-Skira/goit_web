## Докер
# Dockerfile
Це креслення образу.
# Dockerimage
Це шаблон по котрому буде запускатись контейнер.
# Dockercontainer
Це ваш запущенний процесс.
1. Встановлення докера

2. Реєстрація DockerHUB

3. Показати основні команди докерів (можно з конспекта показати)

4. Робота з Docker Desktop

### Створення нового проекту.
1. `docker init` - створить структуру для Docker проекту.
### Докеризація проекту.
1. Докеризація додатка: `app_flask`. Якщо є бажання завантажити отриманий образ на DockerHUB

    - Працювати з [Python Docker Images](https://hub.docker.com/_/python)
    - `docker build -t goit-python-app .` Створення докер образу з тегом goit-python-app у поточній директорії.
    - `docker images --all` список всіх образів(images)
    - `docker run -it -p 8000:8000 --rm --name app-simple-test goit-python-app `

        -d :-d=false: Detached mode: Run container in the background, print new container id

        -t : Розподіл псевдо-TTY (псевдотерміналу) означає створення пари віртуальних пристроїв, які ведуть себе як фізичний термінал. Можливість "показувати" данні в терміналі.

        -i : Інтерактивний режим. Keep STDIN open even if not attached. Таким чином, «зберігати stdin відкритим, навіть якщо він не підключений» означає забезпечення того, що процес може приймати вхідні дані від stdin, навіть якщо він працює у фоновому режимі або як служба без прямого підключення до терміналу.

        -p : publicPort:InsideDockerPort  -  8000:8000
        --rm : Видалення Контейнера після закінчення роботи.

### Викладання образу у Docker Hub.

Docker Registry, також відомий як Docker Hub, — це спільнота сховищ, де користувачі Docker створюють, тестують і керують контейнерами. Якщо ви працювали з GitHub, цей розділ буде вам добре знайомий.
1. `docker login`
2. docker tag flask_docker your-docker-hub-username/repository-name

    `docker tag goit-python-app ruslanskira/app-simple-test`

3. `docker push goit-python-app ruslanskira/app-simple-test`
    Відкрити ДокерХаб і о чудо! Там ваш образ. Котрі інши можуть завантажити.
4. Подивитись на шари через тег образа. Свого та python.
6. Якщо група розуміє, можна піти далі та показати докер-компонування: `app_compose`. У БД вручну додайте дані, простий документ з полем `name`. Контейнер вернет JSON. Важен просто принцип роботи.

### Зайти в середину
1. `docker ps -a`  знайти імʼя образу та скопіювати ід контейнеру.
2. `docker exec -it <id> bash` може бути id, а може бути імʼя контейнеру.

