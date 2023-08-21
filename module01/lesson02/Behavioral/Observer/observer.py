import datetime

"""Спостерігач це Поведінковий паттерн"""

# https://refactoring.guru/uk/design-patterns/observer


class Event:
    """“
    Пате­рн Спо­сте­рі­гач про­по­нує збе­рі­га­ти все­ре­ди­ні об’єкта вида­вця спи­сок поси­ла­нь на об’єкти під­пи­сни­ків. При­чо­му вида­ве­ць не пови­нен вести спи­сок під­пи­ски само­сті­йно.
    Він пови­нен нада­ти мето­ди, за допо­мо­гою яких під­пи­сни­ки могли б дода­ва­ти або при­би­ра­ти себе зі списку.
    ”"""
    _observers = []
    # { 'event1' : [], 'event2': [] }

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event, data=None):
        for observer in self._observers:
            observer(event, data)


def logger(event, data):
    """subscripber 1"""
    print(event, data)


class FileLogger:
    """subscriber 2"""
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, "a") as fl:
            fl.write(f"{datetime.datetime.now()}: [{event}] - {data}\n")


if __name__ == "__main__":
    event = Event()

    event.register(logger)

    fl = FileLogger("logss.txt")
    event.register(fl)

    event.notify("PULS", 65)
    event.notify("PULS", 67)
    event.notify("PULS", 69)

    event.notify("UPS", "Sometime it happens")
    event.unregister(fl)

    event.notify("PULS", 120)
    event.notify("PULS", 130)
