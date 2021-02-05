import subprocess #calls the ./derive script from python
import json
import os
from dotenv import dotenv_values

none = dotenv_values('.env')
mnemonic = none["mnemonic"]

command = 'php derive -g --mnemonic="'+str(mnemonic)+'" --numderive='+str(numderive)+' --coin='+str(coin)+' --format=jsonpretty' 

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

(output, err) = p.communicate()

keys =  json.loads(output)

print(keys)
