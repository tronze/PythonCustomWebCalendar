from web_elements.web_element import WebElement
from web_elements.table.table import TableElement


class TheadElement(WebElement):

    THEAD = 'thead'
    TH = 'th'

    def __init__(self):
        super().__init__(element_type=self.THEAD)

    def create_table_header_column(self):
        th = WebElement(element_type=self.TH)
        return th
