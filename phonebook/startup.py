import time
import sys
import os

def typetext(text):

  for c in text:
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.1)

os.system('cls')
