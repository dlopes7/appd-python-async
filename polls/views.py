import time

from django.http import HttpResponse
from concurrent.futures import ThreadPoolExecutor

from appdynamics.agent import api as appd


class Slow1():
    def __init__(self):
        self.name = 'Slow1'

    def run_check(self):
        time.sleep(1)
        return 1


class Slow2():
    def __init__(self):
        self.name = 'Slow2'

    def run_check(self):
        time.sleep(2)
        return 2


class Slow3():
    def __init__(self):
        self.name = 'Slow3'

    def run_check(self):
        time.sleep(3)
        return 3


plugins = [Slow1(), Slow2(), Slow3()]


def _run(plugin):
    start = time.time()
    ret = plugin.run_check()
    return (ret, plugin.name, time.time() - start)


def index(request):

    appd_bt = appd.get_active_bt_handle(request)

    with ThreadPoolExecutor(max_workers=5) as executor:
        for ers in executor.map(_run, plugins):

            # If we have a Business Transaction, lets add snapshot data
            # Another way to do this is to pass the request object directly
            # In this case we would create the BTs directly on the objects
            # (plugin) code
            if(appd_bt):
                print('Adding snapshot data')
                appd.add_snapshot_data(appd_bt, ers[1], ers)
            print(ers)

    return HttpResponse("Hello, world. You're at the polls index.")
