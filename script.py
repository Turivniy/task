import os
import datetime as dt
import smtplib


def check_for_errors_in_files(files, word='Error'):
    found_files = []

    for file in files:
        if word in open(file).read():
            found_files.append(file)
            print("Some Errors in file:", file)
    return found_files


def get_files(directory='/tmp/tmp/'):
    today = dt.datetime.now().date()
    found_files = []

    for file in os.listdir(directory):
        full_patch_to_file = directory + file
        filetime = dt.datetime.fromtimestamp(os.path.getctime(full_patch_to_file))
        if filetime.date() == today and os.stat(full_patch_to_file).st_size != 0:
            found_files.append(full_patch_to_file)
            print('Today created file:', file)

    return found_files


def send_email(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Allow less secure apps: ON
    server.login("turivniy@gmail.com", "")

    msg = message
    server.sendmail("turivniy@gmail.com", "turivniy@gmail.com", msg)
    server.quit()


# found_files = get_files()
# files_with_errors = check_for_errors_in_files(found_files, word='Error')

send_email('Hello Serg!')