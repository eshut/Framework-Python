from framework.Base.BaseElement import *
import random


class Button(BaseElement):

    def getText(self):
        '''
        :return: text of element
        '''
        self._find()
        return self.element.text

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self._find()
        self.element.send_keys(keys)


class Form(BaseElement):
    pass


class Input(BaseElement):

    def clear(self):
        '''
        :return: nothing
        Clear input textfield
        '''
        self._find()
        logger.info("Trying to clear a field")
        self.element.clear()

    def send(self, keys):
        '''
        :param keys: Text to send
        :return: nothing
        Entering a text to field
        '''
        self._find()
        self.element.send_keys(keys)


class Label(BaseElement):
    def getText(self):
        '''
        :return: text of element
        '''
        self._find()
        logger.info("Trying to get text of element")
        return self.element.text

    def getAttr(self, attr):
        self._find()
        return self.element.get_attribute(attr)

class DropDown(BaseElement):
    def random(self):
        '''
        :return: random element of dropdown
        '''
        element = self._finds()
        element = random.choice(element)
        return element


class CheckBox(BaseElement):
    def random(self):
        '''
        :return: random element of dropdown
        '''
        self.element = random.choice(self.elem)
        return self.element

    def getText(self):
        '''
        :return: text of element
        '''
        self._find()
        logger.info("Trying to get text of element")
        text = self.element.text
        return text









