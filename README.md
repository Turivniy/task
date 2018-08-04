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
python3 script.py
```