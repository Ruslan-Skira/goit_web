# Введение в NoSQL бази данних
7CXsR4gyQ9C3i9ch hubertnills

## Перше заняття
- Create створити
`db.cats.insertOne({name: 'Bars', age: 3})`
- update - застаріло.
замість `db.cats.update({name: 'Bars'}, {name: 'Tom', age: 5}, {upsert: true})`
Приклад:
*$set* - приводить до того, що якщо документ не містить оновлюване поле, то воно створюється. Інакше буде зроблено заміну документа.
*upsert* - оновлювати документ, якщо він знайдений, і створювати новий, якщо такого документа немає.

`db.cats.updateMany({name: 'Bars'}, {$set:{name: 'Tom', age: 5}}, {upsert: true})`
`db.version()`

- update for one is works
`db.cats.update(
    {name: 'Tom'},
    {$set: {features: ['ходить в лоток', 'не дає себе гладити', 'сірий']}},
)`
- видалити ключ
`db.cats.update({name: 'Tom'}, {$unset: {age: 1}})`

- Видалення всіх документів із зазначеним запитом
`db.cats.remove({name: 'Tom'})`
- видалення тільки одного документу
`db.cats.remove({name: 'Tom'}, true)`

** Робота з масивами **
`db.cats.find({age: {$in: [2, 10]}})`

### Папка `pymongo_example`

Папка `pymongo_example` - приклади `PyMongo`. Завести і показати процесс створення акаунту на https://cloud.mongodb.com
підставити свої креди, показати приклади. Запустити приклад `test_connect.py`.

В прикладі `finish_main.py` показується "правильне" створення декораторів через `wraps` та
дати поняття розуміння необхідності валідування вхідних даних &mdash; функція `validate`. Починаємо з `start_main.py`
приходимо до `finish_main.py`

Приклади команд CLI `finish_main.py`:

```bash
(module08-6Z-0SJgN-py3.10) py .\finish_main.py --action create --name Simon --age 4 --features "Вредний" "Ходить мимо лотка"
{'_id': ObjectId('637b40a5256b93d9e9dd83bd'), 'name': 'Simon', 'age': '4', 'features': ['Вредний', 'Ходить мимо лотка']}
```

```bash
py .\finish_main.py --action find
{'_id': ObjectId('637b40a5256b93d9e9dd83bd'), 'name': 'Simon', 'age': '4', 'features': ['Вредний', 'Ходить мимо лотка']}
```

<hr/>

### Папка `mongoengine_example`

Приклади з документації. Розглянуто повний CRUD.
- `create_records.py`
- `get_records.py`
- `update_record.py`
- `delete_record.py`

<hr/>
## Лекція 2
### Папка `redis_example`

Трошки прикладів з Redis. Redis через docker контейнер

## Друге заняття

RabitMQ

- `01_simple` https://www.rabbitmq.com/tutorials/tutorial-one-python.html
- `02_tasks` https://www.rabbitmq.com/tutorials/tutorial-two-python.html
- `03_pub_sub` https://www.rabbitmq.com/tutorials/tutorial-three-python.html

Celery

- `04_celery`

- Приклад з конспекту [https://textbook.edu.goit.global/python-web-textbook/docs/module-08/module-08-02/celery_04](https://textbook.edu.goit.global/python-web-textbook/docs/module-08/module-08-02/celery_04)
Запустити, показати.