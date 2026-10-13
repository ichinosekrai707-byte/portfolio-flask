class Skill:
    """ENCAPSULATION: the name is private (__name) and can only be
    read or changed through the property, which validates the value."""

    def __init__(self, skill_id, name):
        self.__id = skill_id
        self.name = name  # goes through the setter below

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = (value or "").strip()
        if not value:
            raise ValueError("Skill name cannot be empty.")
        if len(value) > 45:
            raise ValueError("Skill name must be 45 characters or fewer.")
        self.__name = value


class Project:
    """BASE CLASS for every portfolio project.

    ENCAPSULATION: all data is private (__title, __description ...).
    Other code uses the properties, and the setters check the values.
    """

    def __init__(self, project_id, title, description, tech_stack="", link=""):
        self.__id = project_id
        self.title = title
        self.description = description
        self.tech_stack = tech_stack
        self.link = link

    # ----- getters / setters (properties) -----
    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        value = (value or "").strip()
        if not value:
            raise ValueError("Title cannot be empty.")
        if len(value) > 80:
            raise ValueError("Title must be 80 characters or fewer.")
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        value = (value or "").strip()
        if not value:
            raise ValueError("Description cannot be empty.")
        self.__description = value

    @property
    def tech_stack(self):
        return self.__tech_stack

    @tech_stack.setter
    def tech_stack(self, value):
        value = (value or "").strip()
        if len(value) > 100:
            raise ValueError("Tech stack must be 100 characters or fewer.")
        self.__tech_stack = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        value = (value or "").strip()
        # Only allow normal web links (blocks things like javascript:...).
        if value and not value.startswith(("http://", "https://")):
            raise ValueError("Link must start with http:// or https://")
        if len(value) > 255:
            raise ValueError("Link must be 255 characters or fewer.")
        self.__link = value

    # ----- methods the subclasses OVERRIDE (POLYMORPHISM) -----
    def get_type(self):
        return "PROJECT"

    def get_label(self):
        return "Project"

    def get_summary(self):
        return self.description


class WebProject(Project):
    """INHERITANCE: a WebProject IS a Project.
    POLYMORPHISM: it overrides get_type(), get_label() and get_summary()."""

    def get_type(self):
        return "WEB"

    def get_label(self):
        return "Web Project"

    def get_summary(self):
        return "Website: " + self.description


class AppProject(Project):
    """INHERITANCE: an AppProject IS a Project.
    POLYMORPHISM: it overrides the same methods in its own way."""

    def get_type(self):
        return "APP"

    def get_label(self):
        return "Application"

    def get_summary(self):
        return "Application: " + self.description
