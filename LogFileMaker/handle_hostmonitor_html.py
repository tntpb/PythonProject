# coding:utf-8
import sys
from imp import reload
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing import Pool, Queue, Process
import multiprocessing as mp
import time
import random
import os
import codecs
import jieba.analyse

jieba.analyse.set_stop_words("yy_stop_words.txt")


def extract_keyword(input_string):
    # print("Do task by process {proc}".format(proc=os.getpid()))
    tags = jieba.analyse.extract_tags(input_string, topK=5)
    # print("key words:{kw}".format(kw=" ".join(tags)))
    return tags


# def parallel_extract_keyword(input_string,out_file):
def parallel_extract_keyword(input_string):
    # print("Do task by process {proc}".format(proc=os.getpid()))
    tags = jieba.analyse.extract_tags(input_string, topK=5)
    # time.sleep(random.random())
    # print("key words:{kw}".format(kw=" ".join(tags)))
    # o_f = open(out_file,'w')
    # o_f.write(" ".join(tags)+"\n")
    return tags


if __name__ == "__main__":
    data_file = sys.argv[1]
    with codecs.open(data_file) as f:
        lines = f.readlines()
        f.close()

    out_put = data_file.split('.')[0] + "_tags.txt"
    t0 = time.time()
    for line in lines:
        parallel_extract_keyword(line)
    # parallel_extract_keyword(line,out_put)
    # extract_keyword(line)
    print("串行处理花费时间{t}".format(t=time.time() - t0))

    pool = Pool(processes=int(mp.cpu_count() * 0.7))
    t1 = time.time()
    # for line in lines:
    # pool.apply_async(parallel_extract_keyword,(line,out_put))
    # 保存处理的结果，可以方便输出到文件
    res = pool.map(parallel_extract_keyword, lines)
    # print("Print keywords:")
    # for tag in res:
    # print(" ".join(tag))
    pool.close()
    pool.join()
    print("并行处理花费时间{t}s".format(t=time.time() - t1))
