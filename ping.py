
import subprocess
import re
from termcolor import cprint

welcome = """
|||||             ~ Average Ping ~            |||||
 ||||          Coded By : AmirTyper           ||||
  |||        My Instagram : @amir_typer       |||
   ||       https://github.com/AmirTyper      ||
    |                    V1                   |
"""
print(welcome)

x = input("Write the Domain or IP: ")

print("Testing...")
try:
    output = subprocess.check_output("ping "+ x, shell = False, universal_newlines=True).splitlines()
    for i in output:
        if "Packets" in i:
            var1 = int(re.search(r'\d+', str(re.findall(r'Lost =\s\d*',i))).group())
            cprint("Packet lost: {0}".format(var1),"red")
        if "Minimum" in i:
            var2 = int(re.search(r'\d+', str(re.findall(r'Average =\s\d*',i))).group())
            cprint("Average ms: {0}".format(var2),"green")
except:
    cprint("Error!","red")


