#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__() \
            .replace('<', '&lt;') \
            .replace('\&lt;', '<') \
            .replace('>', '&gt;')  \
            .replace('\&gt;', '>') \
            .replace('"', '&quot;') \
            .replace('\&quot;', '"') \
            .replace('\n', '\n<br />\n')



class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    offset = [0]

    class ValidationError(Exception):
        def __init__(self):
            super().__init__("Validation error!")

    def __make_double_tag(self):
        self.offset[0] += 1
        open_tag = "<" + self.tag + self.__make_attr() + ">"
        content = self.__make_content()
        self.offset[0] -= 1
        close_tag_offset = ''
        if content != '':
            close_tag_offset = '  ' * self.offset[0]
        close_tag = "</" + self.tag + ">"
        return open_tag + content + close_tag_offset + close_tag

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if tag_type == 'simple' and content != None:
            ValueError("simple tag can't content any thing")
        if type(tag) != str:
            raise ValueError("tag parameter must be string")
        self.tag = tag
        self.attr = attr
        self.content = []
        if content == None:
            self.add_content(Text(''))
        elif type(content) == Text:
            self.add_content(content)
        else:
            self.add_content(content)
        if type(tag_type) != str \
           or tag_type != 'double' \
           and tag_type != 'simple':
            raise ValueError("tag_type parameter must be 'double' or 'simple'")
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = self.__make_double_tag()
        elif self.tag_type == 'simple':
            result = "<" + self.tag + self.__make_attr() + ' ' + "/>"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += '  ' * self.offset[0] + str(elem) + '\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    print(Elem(tag='html', \
        content=[\
            Elem(tag='head', \
                content=Elem(tag='title', \
                    content=Text('\\"Hello ground!\\"'))), \
            Elem(tag='body', \
                content=[\
                    Elem(tag='h1', \
                        content=Text('\\"Oh no, not again!\\"')), \
                    Elem(tag='img', tag_type='simple',\
                         attr={'src' : 'http://i.imgur.com/pfp3T.jpg'})
                    ]) \
            ]))
