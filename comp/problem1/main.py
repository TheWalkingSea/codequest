from typing import Union, List, Optional, Iterable
import sys

def getLines(lines: Optional[int]=0) -> Union[str, List[str]]:
    if lines == 0: return sys.stdin.readline().rstrip()
    ret = list()
    for _i in range(lines):
        ret.append(getLines())
    return ret


def main(cin: List[str]) -> Iterable[str]:
    ipmac = dict()
    ret = list()
    for line in cin:
        ip, mac = line.split(" ")
        if ip in ipmac.keys():
            if mac not in ipmac[ip]:
                ipmac[ip].append(mac)
        else:
            ipmac[ip] = [mac]
    ipssorted = [list(map(int, ip.split('.'))) for ip in ipmac]
    ipssorted.sort()
    # print(sorted_dict)
    ipssorted = ['.'.join(map(str, ip)) for ip in ipssorted]
    for ip in ipssorted:
        yield f"{ip} {len(ipmac[ip])}"

if __name__ == "__main__":
    testCases = int(getLines())
    for _i in range(testCases):
        x = int(getLines())
        ips = list()
        for _j in range(x):
            ips.append(getLines())
        for out in main(ips):
            print(out)