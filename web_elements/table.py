from .web_element import WebElement


class TableElement(WebElement):

    TABLE = 'table'
    THEAD = 'thead'
    TBODY = 'tbody'
    TR = 'tr'
    TD = 'td'

    def __init__(self):
        super().__init__(element_type=self.TABLE)
