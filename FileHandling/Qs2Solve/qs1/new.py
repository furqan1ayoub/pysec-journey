# 1) Count unique IPs in a log file (ips.log) and detect potential DDoS attempts

# Define function for reusability
def logAnalyzer(filename, threshold):
#puts ips from logs into the array
    with open(filename, "r") as logFile:
        ipArray = [eachLine.split()[0] for eachLine in logFile]
        print('-----------')
#print all ips 
        print(" - TOTAL IPS - ")
#for counting occurence   
        dict1 = {}
        for eachIp in ipArray:
            if eachIp in dict1:
                dict1[eachIp] += 1
            else:
                dict1[eachIp] = 1
        threatIps = []
        for key, value in dict1.items():
            print(f"Ip - {key} -> {value} times")
            #for dos/ddos-check
            if value > threshold:
                print("---BF Attempt-----")
                print(f"Ip - {key} -> {value} times")
                msg = f"ATTACK ATTEMPTS FROM THE IP - {key}"
                print(msg)
                return key
            print("NO ATTACKS/SECURITY Threats")

if __name__ == "__main__":
    filename = "ips.log"
    threshold = 5
    logAnalyzer(filename,threshold)