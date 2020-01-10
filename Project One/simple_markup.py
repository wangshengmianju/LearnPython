# -*- coding: utf-8 -*-

import os, sys, re
from util import blocks, lines

fileTobeturned = open('Project One/test_input.txt')
fileOutput = open('Project One/text_output.html','w')

fileOutput.write('<html><head><title>...</title><body>\n')

title = True
for block in blocks(fileTobeturned):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        fileOutput.write('<h1>')
        fileOutput.write(block)
        fileOutput.write('</h1>\n')
        title = False
    else:
        fileOutput.write('<p>')
        fileOutput.write(block)
        fileOutput.write('</p>\n')
    
fileOutput.write('</body></html>')