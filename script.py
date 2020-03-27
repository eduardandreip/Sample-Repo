import math
import os
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)

r = requests.get("http://google.com")

print(r.status_code)


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings
