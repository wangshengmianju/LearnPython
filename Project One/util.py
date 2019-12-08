#To find out the block
#A generator to form text block
def lines(file):      
    r"yeild lines in file, add \n after last line "#为什么必须要在最后加上一个空行
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