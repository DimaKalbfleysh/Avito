#!/usr/bin/env python
import format_keys
import public


@public.add
class Badge:
    """badge generator class"""
    __readme__ = ["image", "link", "title", "markup", "branch", "visible"] + ["md", "rst", "html"]
    image = ""
    link = ""
    title = ""
    markup = "md"
    branch = "master"
    visible = True

    def __init__(self, **kwargs):
        """init from attrs"""
        self.update(**kwargs)

    def update(self, *args, **kwargs):
        """update attrs"""
        inputdict = dict(*args, **kwargs)
        for k, v in inputdict.items():
            setattr(self, k, v)

    def format(self, string):
        """format string"""
        kwargs = dict()
        for key in format_keys.keys(string):
            value = getattr(self, key, None)
            if value is None:
                value = ""
            kwargs[key] = value
        return string.format(**kwargs).replace(" ", "%20")

    @property
    def html(self):
        """render to .html"""
        if not self.link:
            return self.format('<img src="%s" />' % self.image)
        return self.format('<a href="%s">%s</a>' % (self.link, self.img))

    @property
    def md(self):
        """render as .md"""
        return self.format("[![%s](%s)](%s)" % (self.title, self.image, self.link))

    @property
    def rst(self):
        """render as .rst"""
        return self.format(""".. image:: %s
    :target: %s""" % (self.image, self.link if self.link else "none"))

    def render(self, markup):
        if markup == "md":
            return self.md
        if markup == "rst":
            return self.rst
        if markup == "html":
            return self.html
        raise ValueError("'%s' unknown markup" % markup)

    def __bool__(self):
        """return True if self.visible is True"""
        return getattr(self, "visible", True)

    def __nonzero__(self):
        return getattr(self, "visible", True)

    def __str__(self):
        """render badge to string"""
        if self:
            return self.render(self.markup)
        return ""

    def __repr__(self):
        return self.__str__()
