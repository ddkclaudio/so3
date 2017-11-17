class Events:
    ACCESS = 0
    DELETE = 1
    INSERT = 2

    def __init__(self, kind, moment, proc, acc=None):
        self.kind = kind
        self.moment = moment
        self.proc = proc
        self.acc = acc

    def __lt__(self, other):
        return self.kind < other.kind

class Access:

    def __init__(self, proc, space):
        self.proc = proc
        self.space = space