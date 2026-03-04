import systeminfo as si

sysInfo = si.osInfo()
sysType = sysInfo[0]
osName = sysInfo[1]

ramAmount = si.RamAmount()
ramB = ramAmount[0]
ramGB = ramAmount[1]

battery = si.batteryInfo()

cpuInfo = si.cpuInfo()
cpuCores = cpuInfo[0]
cpuType = cpuInfo[1]

currentDir = si.currentDir()

def fastfetch():
    fastfetchArt = rf"""
 ____________________________________________________
 / \                                                 \.
|   |                                                |.
 \_ |     ____            _                          |.
    |    / ___|  ___ _ __(_)_ __  _ |_               |.
    |    \___ \ / __| '__| | '_ \| __|               |.
    |     ___) | (__| |  | | |_) | |_                |.
    |    |____/ \___|_|  |_| .__/ \__|               |.
    |                      |_|                       |.
    |                                                |.
    |                 ___    ____                    |.
    |                / _ \  / ___|                   |.
    |               | | | | \___ \                   |.
    |               | |_| |  ___) |                  |.
    |                \___/  |____/                   |.
    |                                                |.
    | -----------------System Specs----------------- |.
    | cpu Cores: {cpuCores}          cpu type: {cpuType}         |.
    | system type: {sysType}    OS name: {osName}           |.
    |                                                |.
    | RAM in bytes: {ramB}  RAM in GB: {ramGB}      |.
    |                                                |.
    | Battery info: {battery}                             |.
    |                                                |.
    | Current Directory:                             |.
    | {currentDir}                 |.
    |                                                |.
    |   ____________________________________________ |.
    |  /                                             /.
    \_/_____________________________________________/.
    """
    print(fastfetchArt)

