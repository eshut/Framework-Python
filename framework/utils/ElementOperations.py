"""Framework: https://github.com/eshut/Framework-Python"""

import random

from framework.Base.BaseElement import *


class Button(BaseElement):

    def get_text(self):
        '''
        :return: text of element
        '''
        self.find()
        return self.element.text

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self.find()
        self.element.send_keys(keys)

    def get_attr(self, attr):
        self.find()
        return self.element.get_attribute(attr)

    def move_mouse(self):
        self.move()


class Form(BaseElement):
    pass


class Input(BaseElement):

    def clear(self):
        '''
        :return: nothing
        Clear input textfield
        '''
        self.find()
        self.logger.debug("Trying to clear a field")
        self.element.clear()

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self.find()
        self.element.send_keys(keys)

    def move_mouse(self):
        self.move()

class Label(BaseElement):
    def get_text(self):
        '''
        :return: text of element
        '''
        self.find()
        self.logger.debug("Trying to get text of element")
        return self.element.text

    def get_attr(self, attr):
        self.find()
        return self.element.get_attribute(attr)


class DropDown(BaseElement):
    def random(self):
        '''
        :return: random element of dropdown
        '''
        element = self.finds()
        element = random.choice(element)
        return element


class CheckBox(BaseElement):
    def random(self):
        '''
        :return: random element of dropdown
        '''
        self.element = random.choice(self.elem)
        return self.element

    def get_text(self):
        '''
        :return: text of element
        '''
        self.find()
        self.logger.debug("Trying to get text of element")
        text = self.element.text
        return text


class Div(BaseElement):
    def get_element(self, parent=None):
        self.elem = parent
        return self.find()

    def get_elements_list(self, parent=None):
        self.elem = parent
        return self.finds()

    def get_attr(self, attr, parent=None):
        self.get_element(parent)
        return self.element.get_attribute(attr)

    def get_text(self, parent=None):
        self.get_element(parent)
        self.logger.debug("Trying to get text of element")
        text = self.element.text
        return text

    def wait_for_element(self, wait_time):
        return self.wait_elem(wait_time)
