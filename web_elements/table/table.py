from web_elements.web_element import WebElement


class TableElement(WebElement):

    TABLE = 'table'
    TBODY = 'tbody'
    TD = 'td'

    def __init__(self):
        super().__init__(element_type=self.TABLE)

    def create_table_column(self):
        td = WebElement(element_type=self.TD)

    def set_header(self, headers):
        pass

    def set_content(self, array2d):
        text = ""
        super().set_content(text)
