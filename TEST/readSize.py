def readlines(f, separator):
  '''
  读取大文件方法
  :param f:  文件句柄
  :param separator:  每一行的分隔符
  :return:
  '''
  buf = ''
  while True:
    while separator in buf:
        position = buf.index(separator) # 分隔符的位置
        yield buf[:position] # 切片, 从开始位置到分隔符位置
        buf = buf[position + len(separator):] # 再切片,将yield的数据切掉,保留剩下的数据
 
    chunk = f.read(4096) # 一次读取4096的数据到buf中
    if not chunk: # 如果没有读到数据
        yield buf # 返回buf中的数据
        break # 结束
    buf += chunk # 如果read有数据 ,将read到的数据加入到buf中
 
 
with open('TEST/testRead.txt',encoding='utf-8') as f:
  for line in readlines(f,'|||'):
    # 为什么readlines函数能够使用for循环遍历呢, 因为这个函数里面有yield关键字呀, 有它就是一个生成器函数 ......
    print(line)