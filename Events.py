class Events:
    DELETE = 0
    COMPACT = 1
    INSERT = 2
    ACCESS = 3

    def __init__(self, kind, moment, proc, acc=None):
        self.kind = int(kind)
        self.moment = int(moment)
        self.proc = proc
        self.acc = acc

    def __lt__(self, other):
        return self.kind < other.kind

class Access:

    def __init__(self, proc, space):
        self.proc = proc
        self.space = space
