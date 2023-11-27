from typing import Union, List, Optional, Iterable
import sys

def getLines(lines: Optional[int]=0) -> Union[str, List[str]]:
    if lines == 0: return sys.stdin.readline().rstrip()
    ret = list()
    for _i in range(lines):
        ret.append(getLines())
    return ret


def main(cin: str) -> str:
   out = ""
   for i in range(len(cin)):
     if cin[i] in ["a", "e", "i", "o", "u"]: out += cin[i+1]
   return out

if __name__ == "__main__":
    testCases = int(getLines())
    for _i in range(testCases):
        print(main(getLines()))
        