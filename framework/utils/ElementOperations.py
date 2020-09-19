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


class Form(BaseElement):
    pass


class Input(BaseElement):

    def clear(self):
        '''
        :return: nothing
        Clear input textfield
        '''
        self.find()
        logger.info("Trying to clear a field")
        self.element.clear()

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self.find()
        self.element.send_keys(keys)


class Label(BaseElement):
    def get_text(self):
        '''
        :return: text of element
        '''
        self.find()
        logger.info("Trying to get text of element")
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
        logger.info("Trying to get text of element")
        text = self.element.text
        return text
