import subprocess
import json
from constants import *
from pprint import pprint

test_mnemonic = "mass rally dolphin faith hour spatial blood arrange harvest uncover middle rhythm cigar exchange grunt"

def wallet_derive():

    command = './derive -g --mnemonic= "mass rally dolphin faith hour spatial blood arrange harvest uncover middle rhythm cigar exchange grunt" --format=jsonpretty'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    pprint(output)

wallet_derive()
