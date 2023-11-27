import sys
def main(cin):
    cnt = 0
    for char in cin:
        if char.upper() in ["A", "E", "I", "O", "U"]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        main(sys.stdin.readline().rstrip())     
