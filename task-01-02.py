from concurrent.futures import ThreadPoolExecutor

data = range(1, 10)
pool_size = 5


def f1(item):
    # Возведение в квадрат
    return item ** 2


def f2(data):
    # Подсчёт суммы элементов массива
    result = 0
    for element in data:
        result += element
    return result


def worker(data):
    """
    Возведение всех элементов массива в квадрат и
    подсчёт суммы всех элементов
    """
    with ThreadPoolExecutor(max_workers=pool_size) as pool:
        # Взаимодействие с пулом для возведения в квадрат и подсчёта суммы всех элементов
        result = list(pool.map(f1, data))
        result = pool.submit(f2, result)
        result = result.result()

    return result


if __name__ == '__main__':
    print(worker([1, 2, 3, 4, 5]))
