

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from JerrySpam.utils import load_plugins
import logging
from telethon import events
from . import Jerry, Jerry2, Jerry3, Jerry4, Jerry5, Jerry6, Jerry7, Jerry8, Jerry9, Jerry10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "JerrySpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("JerryS Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @THEJERRY_NETWORK")

if __name__ == "__main__":
    Jerry.run_until_disconnected()
    
if __name__ == "__main__":
    Jerry2.run_until_disconnected()

if __name__ == "__main__":
    Jerry3.run_until_disconnected()
    
if __name__ == "__main__":
    Jerry4.run_until_disconnected()

if __name__ == "__main__":
    Jerry5.run_until_disconnected()
    
if __name__ == "__main__":
    Jerry6.run_until_disconnected()
    
if __name__ == "__main__":
    Jerry7.run_until_disconnected()

if __name__ == "__main__":
    Jerry8.run_until_disconnected()
    
if __name__ == "__main__":
    Jerry9.run_until_disconnected()

if __name__ == "__main__":
    Jerry10.run_until_disconnected()    
