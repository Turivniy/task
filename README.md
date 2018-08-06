# test script

### This script `script.py` gets non empty files created today, finds errors there and sends email with info.

Configure the script.

Edit following variables:
```
WORD_TO_FIND = "For example, 'Error'"
DIRECTORY_WITH_LOGS = "For example, '/var/'"
MAIL_ADDRESS = "YOUR EMAIL HERE"
MAIL_PASSWORD = "YOUR EMAIL PASSWORD HERE"
```

Run script in a terminal:
```
$ python3 script.py
```

Run script every Monday-Friday at 17:00
```
$ crontab -e

0 17 * * 1,2,3,4,5  /usr/bin/python3 /<patch to script>/script.py
```
