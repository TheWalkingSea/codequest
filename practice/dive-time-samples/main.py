from typing import List, Any, Iterable
import sys

def getLines(lines: int=0) -> Any:
    if lines == 0: return sys.stdin.readline().rstrip()
    ret = list()
    for i in range(lines):
        ret.append(getLines())
    return ret

def getNextBest(table: List[List[int]], target: int, index: int=0) -> int:
    for row in table:
        if row[index] >= target:
            return row[index]
    
    

def getRow(table: Any, target: int, index: int=0) -> List[int]:
    return list(filter(lambda row: row[index] == target, table))

def main(table: List[List[int]], dives: List[List[int]]) -> Iterable[str]:
    """Parses the dives with table
    
    Paramters:
    table(List[int][int]): Every row, with each row containing 4 integers being max depth, 
        max bottom time, depth when compression stop is needed, time diver must stop at that depth.
    dives(List[int][int]): Every row, with each row containg 2 integers being the max depth reached by that diver, 
        and the diver's bottom time (MAX_DEPTH)
    
    Returns:
    (str): Yields multiple strings which will be the 2 integers, the depth at which a compression should be made,
        and the amount of time the diver should remain there
    """
    for maxDepth, bTime in dives:
        bestDepth = getNextBest(table, maxDepth)
        for entry in reversed(getRow(table, bestDepth)):
            bestTime = getNextBest(table, bTime, 1)
            if entry[1] == bestTime:
                yield f"aaa {entry[2]} {entry[3]}"
                continue
        yield "No Stop"


        
if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        x = list()
        d = list()
        xLength, dLength = list(map(int, getLines().split(" ")))
        for _i in range(xLength):
            row: List[int] = list(map(int, getLines().split(" ")))
            x.append(row)
        for _j in range(dLength):
            row: List[int] = list(map(int, getLines().split(" ")))
            d.append(row)
        for out in main(x, d):
            print(out)

