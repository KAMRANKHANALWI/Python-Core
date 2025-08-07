import time


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            print("Value from cache")
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        print("value from directly func execution")
        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(2, 3))
print(long_running_function(2, 3))
