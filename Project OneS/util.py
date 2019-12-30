# -*- coding: utf-8 -*-

#To find out the block
#A generator to form text block
def lines(file):      #为什么最后一行一定要加上空行：因为block函数候采用了elif：block的判断来作为生成文本块的信号
    r'yeild lines in file, add \n after last line'
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ' '.join(block).strip()
            block = []