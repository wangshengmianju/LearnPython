# -*- conding utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):
    
    def startElement(self, name, attrs):
        print(name, attrs.keys())

class HeadlineHandler(ContentHandler):
    
    in_headline = False
    headlines = in_headline

    def __init__(self, headlines):
        super().__init__()
        self.headlines = headlines      #由于列表是可变对象，因此这里不是复制，而是引用
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1': self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False
    
    def characters(self, string):
        if self.in_headline:
            self.data.append(string)

class PageMaker(ContentHandler):

    passthrough = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open('ProjectTwo/' + attrs['name'] + '.html','w')
            self.out.write('<html><head>\n')
            self.out.write('<title>{}</title>\n'.format(attrs['title']))
            self.out.write('</head><body>\n')
        elif self.passthrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write('>')
    
    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</{}>'.format(name))
    
    def characters(self, chars):
        if self.passthrough: self.out.write(chars)

    
    
parse('ProjectTwo/website.xml', PageMaker())


