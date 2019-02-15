from .web_classes import WebClasses


class WebElement:

    def __init__(self, element_type, parent=None):
        super().__init__()
        self.element_type = element_type
        self.content = ""
        self.classnames = WebClasses()
        self.parent = parent

    def get_element_properties(self):
        classnames = self.classnames
        class_property = classnames.create_classnames_property()
        s = "".join
        if class_property is not "":
            class_property = " " + class_property
        return s(class_property)

    def create_element(self):
        head_lb = "<%s" % self.element_type
        head_property = self.get_element_properties()
        head_rb = ">"
        head = head_lb + head_property + head_rb
        tail = "</%s>" % self.element_type
        content = self.content
        element = head + content + tail
        return element
