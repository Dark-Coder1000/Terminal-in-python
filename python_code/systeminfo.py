import psutil, os, platform, sys

def osInfo():
    systemName = sys.platform
    osName = os.name
    return systemName, osName

def RamAmount():
    memory = psutil.virtual_memory()
    totalMem = memory.total
    total_GB = round(totalMem / (1024**3), 2)
    return totalMem, total_GB

def batteryInfo():
    battery = psutil.sensors_battery()
    return battery

def cpuInfo():
    cpuCores = os.cpu_count()
    cpuType = platform.processor()
    return cpuCores, cpuType

def currentDir():
    directory = os.getcwd()
    return directory
