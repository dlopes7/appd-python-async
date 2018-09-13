import time

from django.http import HttpResponse
from concurrent.futures import ThreadPoolExecutor


class Slow1():
    def run_check(self):
        time.sleep(1)
        return 1


class Slow2():
    def run_check(self):
        time.sleep(2)
        return 2


class Slow3():
    def run_check(self):
        time.sleep(3)
        return 3


plugins = [Slow1(), Slow2(), Slow3()]


def _run(plugin):
    return plugin.run_check()


def index(request):
    with ThreadPoolExecutor(max_workers=5) as executor:
        for ers in executor.map(_run, plugins):
            print(ers)

    return HttpResponse("Hello, world. You're at the polls index.")
