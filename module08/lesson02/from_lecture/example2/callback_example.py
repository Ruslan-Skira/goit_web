def callback(age):
    print(f'my age {age}')


def main(func, age):
    func(age)


main(callback, 34)

