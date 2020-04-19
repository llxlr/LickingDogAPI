# 关于函数的一些常用方法
from functools import wraps
import time


def delay(func):
    """延迟调用函数"""
    print(f"initial cache for {func.__name__}")
    cache = {}

    @wraps(func)
    def delay_func(*args, **kwargs):
        key = func.__name__  # 函数的名称作为key
        result = None
        if key in cache.keys():  # 判断是否存在缓存
            (result, updateTime) = cache[key]
            if time.time() - updateTime < 10:  # 过期时间固定为10秒
                print("limit call 10s", key)
                result = updateTime
            else:
                print("cache expired !!! can call ")
                result = None
        else:
            print("no cache for ", key)
        if result is None:  # 如果过期，或则没有缓存调用方法
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
        return result
    return delay_func


# 测试延迟调用函数
@delay
def a(x):
    print(f'调用函数{a.__name__} {x}')


def coroutine(func):
    """通过协程实现记录所有函数被调用次数"""
    @wraps(func)
    def execute_next(*args, **kwargs):
        result = func(*args, **kwargs)
        next(result)
        return result
    return execute_next


@coroutine
def cor(start=0):
    while True:
        yield start
        start += 1


def total(func):
    cc = cor()

    @wraps(func)
    def count(*args, **kwargs):
        co = cc.send(1)
        print('调用次数： %s' % co)
        result = func(*args, **kwargs)
        return result
    return count


# 这里是用作统计的函数
@total
def b(x):
    pass


if __name__ == '__main__':
    # 测试延迟调用函数
    # a(1)
    # a(2)
    # 测试记录所有函数被调用次数
    # import random
    # for i in range(random.randint(1, 10)):
    #     b(i)
    pass
