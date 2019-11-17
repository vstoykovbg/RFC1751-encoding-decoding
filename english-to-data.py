#!/usr/bin/python3

import sys
from Cryptodome.Util import RFC1751
from Cryptodome.Util.Padding import unpad

english = sys.stdin.buffer.read()

english = english.decode()

data = RFC1751.english_to_key(english)

unpadded = unpad(data, 8)

sys.stdout.buffer.write(unpadded)
