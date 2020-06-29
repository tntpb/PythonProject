# conding=utf-8
# author = 'pengben 2020-5-26'
import os
import time
import shutil



def mkSubFile(lines, head, srcName, sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    fout = open(filename, 'w')
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()


def splitByLineCount(filename, count):
    fin = open(filename, 'r')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filename, sub)
    finally:
        fin.close()


if __name__ == '__main__':
    begin = time.time()
    splitByLineCount('E:\Breakfile\log.htm', 100000)
    end = time.time()
    print('time is %d seconds ' % (end - begin))


def objFileName():
    # list.txt记录截取目标文件列表
    fileNameList = r"E:\Breakfile\list.txt"
    objNameList = []

    for i in open(fileNameList, 'r'):
        objNameList.append(i.replace('\n', ''))
        return objNameList

def copyFile():
    # 指定文件原始路径
    sourcePath = r'E:\Breakfile'

    # 指定文件存放目录
    targetPath = r'E:\rsyncdata'

    for i in objFileName():
        objName = i
        shutil.copy(sourcePath + '/' + objName, targetPath + '/' + objName)

if __name__ == '__main__':
    copyFile()