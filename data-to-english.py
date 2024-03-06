#!/usr/bin/python3

import sys
from Crypto.Util import RFC1751
from Crypto.Util.Padding import pad

data = sys.stdin.buffer.read()

data = pad(data,8)

english = RFC1751.key_to_english(data)

sys.stdout.write(english)

