import os

def main():
    with open("main.py", "r") as f:
        compiled = "import sys\n" + "".join(f.readlines()) + """

if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        main(sys.stdin.readline().rstrip())     
"""
        if not os.path.exists("compiled"):
            os.mkdir("compiled")
        with open("compiled/main.py", "w") as r:
            r.write(compiled)

if __name__ == "__main__":
    main()