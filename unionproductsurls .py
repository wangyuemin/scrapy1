# coding=utf-8
import selenium2
from multiprocessing import Pool
import re
import os
from selenium import webdriver
import queue
import time
import multiprocessing
from pybloom import BloomFilter
import asyncio
from asyncio import Queue


async def foo(myqueue):
    while not myqueue.empty():
        selenium2.mainurl(myqueue.get())
        for this2plusurl in selenium2.linkurl:
            if not this2plusurl in f:
                f.add(this2plusurl)
                ln.append(this2plusurl)
                myqueue.put(this2plusurl)
        print (len(ln))

if __name__ == '__main__':
    global ln
    ln = []
    f = BloomFilter(capacity=100000, error_rate=0.001)
    global myqueue
    myqueue = queue.Queue()
    url = 'www.dayanghang.net'
    f.add(url)
    ln.append(url)
    selenium2.mainurl(url)
    for this2plusurl in selenium2.linkurl:
        if not this2plusurl in f:
            f.add(this2plusurl)
            ln.append(this2plusurl)
            myqueue.put(this2plusurl)
    print (myqueue.qsize())
    if not myqueue.empty():
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(
            [asyncio.async(foo(myqueue))]))
        loop.close()
    print (len(ln))
    print (ln)
    print (myqueue.qsize())
