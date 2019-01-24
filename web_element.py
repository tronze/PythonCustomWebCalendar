from web_classes import WebClasses


class WebElement:

    DIV = 'div'
    UL = 'ul'
    LI = 'li'

    def __init__(self, element_type):
        super().__init__()
        self.element_type = element_type
        self.content = ""
        self.classnames = WebClasses()

    def set_content(self, text):
        self.content = text

    def get_element_properties(self):
        classnames = self.classnames
        class_property = classnames.create_classnames_property()
        s = "".join
        return s(" " + class_property)

    def create_element(self):
        head_lb = "<%s" % self.element_type
        head_property = self.get_element_properties()
        head_rb = ">"
        head = head_lb + head_property + head_rb
        tail = "</%s>" % self.element_type
        content = self.content
        element = head + content + tail
        return element
