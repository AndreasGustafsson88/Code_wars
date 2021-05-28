class Event:
    def __init__(self):
        self.handlers = []

    def subscribe(self, func):
        self.handlers.append(func)

    def unsubscribe(self, func):
        self.handlers.remove(func)

    def emit(self, *args):
        for handler in self.handlers:
            handler(*args)


event = Event()


class Testf():
    def __init__(self):
        self.calls = 0
        self.args = []

    def __call__(self, *args):
        self.calls += 1
        self.args += args


f = Testf()

event.subscribe(f)
event.emit(1, 'foo', True)

if f.calls == 1:
    print('pass')# calls a handler
if f.args == [1, 'foo', True]:
    print('pass')# passes arguments

event.unsubscribe(f)
event.emit(2)

if f.calls == 1:
    print('pass')# no second call