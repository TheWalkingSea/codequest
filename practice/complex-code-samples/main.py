from sys import stdin

def getLine(c: int=0) -> str|list[str]:
    if c == 0: return stdin.readline().rstrip()
    ret = list()
    for i in range(c):
        ret.append(getLine())
    return ret

def countStr(inp: list[str], phrase: str) -> int:
    return len(list(filter(lambda _x: phrase in _x, inp)))


def main(cin: list[str], c: int, n: int) -> str:
    depth = countStr(cin, "If")
    complexity = countStr(cin, "{")
    if depth <= n and complexity <= c:
        return f"{complexity} {depth} PASS"
    return f"{complexity} {depth} FAIL"
    

if __name__ == "__main__":
    testCases = getLine()
    for i in range(int(testCases)): 
        l, c, n = list(map(int, getLine().split(" ")))
        print(main(getLine(l), c, n))