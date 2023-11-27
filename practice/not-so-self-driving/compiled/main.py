import sys
def main(cin):

    v0, x0 = map(lambda x: float(x), cin.split(":"))
        

    if v0 >= x0:
        print("SWERVE")
    elif 5*v0 >= x0:
        print("BRAKE")
    else:
        print("SAFE")

if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        main(sys.stdin.readline().rstrip())     
