from web_elements.web_element import WebElement


class TableElement(WebElement):
    TR = 'tr'

    def __init__(self):
        super().__init__(element_type=self.TR)
