# Usage: python3 gbkDecode.py '\xF9\x9A\xF1\xA7\xCD\x8F'

import sys


encodeStr = sys.argv[1]
encodeStr = encodeStr.replace('\\x', '')
encodeByte = bytes.fromhex(encodeStr)
print(encodeByte.decode('gbk'))

