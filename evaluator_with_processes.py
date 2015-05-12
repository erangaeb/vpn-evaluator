from multiprocessing import Process
import logging
import time
import os


logging.basicConfig(level=logging.DEBUG,
                    filename='logs/evaluator.log',
                    filemode='w',
                    format='[%(asctime)s] %(message)s',)


def upload(server):
    """
    SCP local file to given remote host. This function will be called by
    seperate process. Seperate process can be use to execute this functiona
    paralley with downloader.

    Args
        server: server ip/name
    """
    for i in range(10):
        start_time = time.time()
        logging.debug('Start uploading by process %s' % os.getpid())
        os.system("scp uploads/18UPLOAD %s:" % server)
        end_time = time.time()
        logging.debug('End uploading')
        logging.debug('Time taken by uploader: %s' % (end_time - start_time))


def download(server):
    """
    SCP file in a given rmote host to local. This function will be called by
    seperate process. By using seperate process we can execute this function
    parellely with uploader

    Args
        server: server ip/name
    """
    for i in range(10):
        start_time = time.time()
        logging.debug('Start downloading by process %s' % os.getpid())
        os.system("scp %s:18DOWNLOAD downloads/" % server)
        end_time = time.time()
        logging.debug('End downloading')
        logging.debug('Time taken by downloader: %s' % (end_time - start_time))


if __name__ == "__main__":
    """
    We are creating two seperate process here
        1. uploader - upload file to a given server
        2. downloader - download file from given server
    """
    uploader = Process(target=upload, args=('staging_service1', ))
    uploader.start()
    downloader = Process(target=download, args=('staging_service1', ))
    downloader.start()
