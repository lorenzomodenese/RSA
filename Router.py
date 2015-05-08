import os

import DataMirroringTCP
import KeysTCP

pid = os.fork()

if (pid == 0):
    DataMirroringTCP.dataMirroring()
else:
    KeysTCP.keysExchange()