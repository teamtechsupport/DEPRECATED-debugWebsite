import annealing_decryption
import re
import random
import math


def transpos(text, colno):
    key = str(math.floor(1234567890 / (10**(10-colno))))

    return(annealing_decryption.anneal(
        text, key, "transposition", "swap",""))



