# GIL
Global Interpreter Lock
Дивиться за тим щоб все виконувалось у одному потоці.
# Потоки

Тут набір прикладів для потоків.
Можна буде показати для питань по темі, що цікавить.
Вибрати та показати, що було не зрозуміло з конспекту

### Timer
Потік таймера виконає функцію після затримки часу.
Ви можете використовувати об’єкт потоку таймера в Python через клас threading.Timer.
#### Як використовувати Thread Timer.
__03_thread_timer.py__

Python надає потік таймера в класі threading.Timer.
Threading.Timer є розширенням класу threading.Thread, тобто ми можемо використовувати його як звичайний екземпляр потоку.

Він забезпечує зручинй спосіб виконання функції через певний проміжок часу.

По-перше, ми можемо створити екземпляр таймера та налаштувати його. Це включає час очікування перед виконанням у секундах, функцію, яку потрібно виконати після запуску, і будь-які аргументи цільової функції.
Функія start() починає відлік часу.
### Lock
__04_thread_lock.py__

У модулі threading Python як Lock, так і RLock (Reentrant Lock) використовуються для синхронізації між потоками, щоб запобігти конкуренції та гарантувати, що лише один потік може отримати доступ до критичної частини коду одночасно. Основна відмінність між ними полягає в тому, як вони обробляють повторне входження або рекурсивне блокування.


**Lock** — це базовий примітив синхронізації, який забезпечує ексклюзивний доступ до спільного ресурсу. Коли потік отримує блокування, жоден інший потік не може отримати таке ж блокування, доки його не буде звільнено. Якщо потік намагається отримати блокування, яке вже утримується іншим потоком, він заблокується та чекає, поки блокування стане доступним.


**RLock** або Reentrant Lock є розширенням базового блокування. Це дозволяє потоку отримувати те саме блокування кілька разів, не викликаючи взаємоблокування. Це корисно, коли потік потребує введення критичної частини коду, який він уже заблокував. Однак потік повинен зняти блокування стільки ж разів, скільки він його отримав.

### Event
__05_event_thread.py__

Python надає вам кращий спосіб спілкування між потоками за допомогою класу Event із модуля Threads.

Клас Event пропонує простий, але ефективний спосіб координації між потоками: один потік сигналізує про подію, а інші потоки чекають її.

Об’єкт Event містить логічний прапор, який можна встановити (True) або очистити (False). Кілька потоків можуть чекати встановлення події, перш ніж продовжити, або можуть скинути подію до очищеного стану.

```
import threading
event = threading.Event()
def call_my_freand():
    print("waiting when to call")
    event.wait() # давай почекаємо коли потрібна допомога
    print("ring ring")

t1 = threading.Thread(target=call_my_freand)
t1.start()
event.set() # Викликай Кракена
```
### thread_pull_executor-> main.py
У цьому файлі зібрані приклади використання Thread Pull Executor як варіант створення потоків та їх використання.
Цей спосів використовується починаючи з пайтону 3.2


Є практичні завдання:

- Папка `task-runner` - за допомогою потоків збираємо файли javascript в один файл
- Папка `file` - приклад сортування файлів. Аналог домашнього завдання
