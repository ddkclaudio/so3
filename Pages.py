class P_pages:
    PAGESP = 0
    TAB_PAGES = []

    def __init__(self, beg, end, virtual=None):
        self.beg = beg
        self.end = end
        self.virtual = virtual
        self.id = P_pages.PAGESP
        P_pages.PAGESP += 1

    def __str__(self):
        if self.virtual is not None:
            return '- ( Proc: %s | %d %d ) -' % (self.virtual.process.nome, self.beg, self.end)
        else:
            return '- ( Free | %d %d ) -' % (self.beg, self.end)

    def is_free (self):
        return self.virtual is None

class V_pages:
    PAGESV = 0

    def __init__(self, beg, end, process = None, physical = None):
        self.beg = beg
        self.end = end
        self.process = process
        self.physical = physical
        self.id = V_pages.PAGESV
        V_pages.PAGESV += 1
        
    def is_free (self):
        return self.physical is None