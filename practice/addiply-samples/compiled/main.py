import sys
def main(cin):
    num1, num2 = map(lambda x: int(x), cin.split(" "))
    print(num1+num2, num1*num2)

if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        main(sys.stdin.readline().rstrip())     
