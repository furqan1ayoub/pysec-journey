#parse the log file
def IpChecker(filename):
    try:
        with open(filename,"r") as logFile:
            onlyIpArray = [eachLine.split()[0] for eachLine in logFile] 
            #as for indexing we can't have unless iterable like list so converted each into array using ->split
        countIps(onlyIpArray)
    except FileNotFoundError:print("NO FILE FOUND !")
    except IndexError:print("Index problem ! keep Ip at index 0")
#count the ips
def countIps(onlyIpArray):
    ips_dict_count = {}
    for eachIp in onlyIpArray:
        if eachIp in ips_dict_count:
            ips_dict_count[eachIp]+=1
        else:ips_dict_count[eachIp] = 1
    for ip,ip_total_times in ips_dict_count.items():
        print(f"{ip} - {ip_total_times}times")
    ip_threat=dos_check(ips_dict_count,5)
    if ip_threat:print("\nAlert ! \t",ip_threat,"is suspicious")
    else:print("NO THREATS FOUND")
        
#check dos attack
def dos_check(ips_dict_count,limit):
    for ip,ip_no in ips_dict_count.items():
        if ip_no > 5 :
            return ip
    return False
#for more modular and reusability 
if __name__ == "__main__":
    IpChecker("ips2.log")