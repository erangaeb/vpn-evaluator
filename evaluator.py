#!/usr/bin/python

import os
import thread
import logging
import time


logging.basicConfig(level=logging.DEBUG,
                    filename='logs/evaluator.log',
                    filemode='w',
                    format='[%(asctime)s] %(message)s',)


def upload(server):
    """
    SCP local file to remote. This need to be call from a thread in order to
    evaluate the netwotk peformace. Copying file need to be more than
    10MB in size. Scp file more than 10 times to evaluate the peformance

    Args:
        server - server IP
    """
    for i in range(10):
        start_time = time.time()
        logging.debug('Start uploading: %d' % i)
        os.system("scp uploads/18UPLOAD %s:" % server)
        end_time = time.time()
        logging.debug('End uploading: ')
        logging.debug('Time taken by uploader: %s' % (end_time - start_time))


def download(server):
    """
    SCP file in rmote host to local. This function need to be call from thread
    in order to evaluate the netwotk peformace. Copying file need to be more
    than 10MB in size. SCP file more than 10 times to evaluate the peformance

    Args:
        server - server IP
    """
    for i in range(10):
        start_time = time.time()
        logging.debug('Start downloading: %d' % i)
        os.system("scp %s:18DOWNLOAD downloads/" % server)
        end_time = time.time()
        logging.debug('End downloading...')
        logging.debug('Time taken by downloader: %s' % (end_time - start_time))

# Create two threads as follows
try:
    thread.start_new_thread(upload, ("cmb_service1", ))
    thread.start_new_thread(download, ("cmb_service1", ))
except:
    print "Error: unable to start thread"

while 1:
    pass
