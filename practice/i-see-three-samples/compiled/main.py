import sys
def main(cin: list[str]):
    cin: list[float] = sorted(list(map(float, cin.split(" "))))
    # print(cin)
    val, cnt = (cin[0], 0)
    for i in cin:
        if i == val:
            cnt += 1
        else:
            if cnt == 3:
                print("TRUE")
                return
            val, cnt = (i, 1)
    if cnt == 3:
        print("TRUE")
        return
    print("FALSE")

if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        main(sys.stdin.readline().rstrip())     
