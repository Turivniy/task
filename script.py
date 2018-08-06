#!/usr/bin/python3

import datetime as dt
import logging
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import gmtime, strftime

WORD_TO_FIND = 'Error'
DIRECTORY_WITH_LOGS = '/tmp/tmp/'
MAIL_ADDRESS = 'turivniy@gmail.com'
MAIL_PASSWORD = ''


def generate_log_filename():
    """Generates filename.

    Returns:
        string: log filename
            For example, 018-08-04_19-37-44.log
    """
    return strftime("%Y-%m-%d_%H-%M-%S.log", gmtime())


log_filename = generate_log_filename()

# Activete logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# create a file handler
handler = logging.FileHandler(log_filename)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


def check_for_errors_in_files(files, word='Error'):
    """
    Check for word inside a file.

    Args:
        files (list): list of the files
        word (string): word tofind

    Returns:
        list: List of the files
    """
    found_files = []

    for file in files:
        if word in open(file).read():
            found_files.append(file)
            logger.info("Some Errors in file: {}".format(file))
    return found_files


def get_files(directory='/tmp/tmp/'):
    """
    Get non empty files created today:

    Args:
        directory (string): the directory to find files

    Returns:
        list: list of the non empty files created today
    """
    today = dt.datetime.now().date()
    found_files = []

    for file in os.listdir(directory):
        full_patch_to_file = directory + file
        filetime = dt.datetime.fromtimestamp(os.path.getctime(full_patch_to_file))
        if filetime.date() == today and os.stat(full_patch_to_file).st_size != 0:
            found_files.append(full_patch_to_file)
            logger.info('Today created file: {}'.format(directory + file))
    return found_files


def generate_message(patch_to_log_file):
    """
    Generates a message to send by email.

    Args:
        patch_to_log_file (string): patch to file with info to send

    Returns:
        string: the message to send by email
    """
    with open(patch_to_log_file, 'r') as content_file:
        return content_file.read()


def send_email(log_filename, message, mail_address, mail_password):
    """
    Sends an email with info

    Args:
        log_filename (string): a file with some info to send
        message (string): a message to send
        mail_address (string): mail address to send (your mail address)
        mail_password (string): your mail address password
    """

    fromaddr = mail_address
    toaddr = mail_address
    msg = MIMEMultipart()
    msg['From'] = mail_address
    msg['To'] = mail_address
    msg['Subject'] = log_filename

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, mail_password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


found_files = get_files(directory=DIRECTORY_WITH_LOGS)
files_with_errors = check_for_errors_in_files(found_files, word=WORD_TO_FIND)
message = generate_message(log_filename)
send_email(log_filename=log_filename, message=message, mail_address=MAIL_ADDRESS, mail_password=MAIL_PASSWORD)
