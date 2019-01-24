class WebElement:

    DIV = 'div'
    UL = 'ul'
    LI = 'li'

    def __init__(self, element_type):
        super().__init__()
        self.element_type = element_type
        self.content = ""
        self.attr = {
            'classnames': [],
        }

    def set_text(self, text):
        self.content = text

    def add_classname(self, classname):
        if classname is not None and classname is not "" and self.classname_exist(classname) is False:
            self.attr.get('classnames').append(classname)

    def get_classnames(self):
        classnames = self.attr.get('classnames')
        return classnames

    def delete_classname(self, classname):
        pass

    def classname_exist(self, classname):
        classnames = self.get_classnames()
        return classname in classnames

    def create_classnames_property(self):
        classnames = self.get_classnames()
        prefix = "class=\""
        postfix = "\""
        class_properties = ""
        for classname in classnames:
            if class_properties is "":
                class_properties = classname
            else:
                class_properties += " " + classname
        return prefix + class_properties + postfix

    def get_element_properties(self):
        class_property = self.create_classnames_property()
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
