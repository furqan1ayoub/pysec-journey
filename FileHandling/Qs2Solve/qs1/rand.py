import new as logAn
filename = "ips2.log"
threshold = 3
threatIp = logAn.logAnalyzer(filename,threshold)
if threatIp:
    with open("Threat.log","w") as fileThreat:
        fileThreat.write(f"Threat Detected - ip ->{threatIp}")