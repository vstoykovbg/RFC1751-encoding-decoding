#!/usr/bin/python3

import sys
from Crypto.Util import RFC1751
from Crypto.Util.Padding import unpad

english = sys.stdin.buffer.read()

english = english.decode()

data = RFC1751.english_to_key(english)

unpadded = unpad(data, 8)

sys.stdout.buffer.write(unpadded)

