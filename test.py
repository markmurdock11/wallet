import subprocess
import json
from pprint import pprint

command = './derive -g --mnemonic = "mass rally dolphin faith hour spatial blood arrange harvest uncover middle rhythm cigar exchange grunt" --cols=path,address,privkey,pubkey --format=jsonpretty'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

#keys = json.loads(output)
json.loads(output,err)
#pprint(keys)