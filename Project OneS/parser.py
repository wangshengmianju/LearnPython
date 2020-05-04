import sys, re
from handlers import *
from util import *
from rules import *


class Parser:
    """
    A Parser reads a text file, applying rules and controlling a handler. 
    """
    def __init__(self, handler):       #  setup
        self.handler = handler 
        self.rules = [] 
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block) 
        self.filters.append(filter)

    def parse(self, file):              #  here is the common procedure
        self.handler.start('document')  #  Assuming the head is always required
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler) 
            for rule in self.rules:
                    if rule.condition(block): 
                        last = rule.action(block, self.handler) 
                        if last: break
        self.handler.end('document')   #  Assuming the end is always required


class BasicTextParser(Parser):        #  here is the difference of text file
    """
    A specific Parser that adds rules and filters in its constructor. 
    """
    def __init__(self, handler):
        Parser.__init__(self, handler) 
        self.addRule(ListRule()) 
        self.addRule(ListItemRule()) 
        self.addRule(TitleRule()) 
        self.addRule(HeadingRule()) 
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis') 
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url') 
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin)