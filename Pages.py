class F_pages:
    PAGESP = 0

    def __init__(self, beg, end, virtual=None):
        self.beg = beg
        self.end = end
        self.virtual = virtual
        self.id = F_pages.PAGESP
        F_pages.PAGESP += 1


class V_pages:
    PAGESV = 0

    def __init__(self, beg, end, phisical = None):
        self.beg = beg
        self.end = end
        self.phisical = phisical
        self.id = V_pages.PAGESV
        V_pages.PAGESV += 1