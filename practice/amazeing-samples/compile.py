import os

def main():
    with open("main.py", "r") as f:
        compiled = "import sys\n" + "".join(filter(lambda x: not x.startswith("print"), f.readlines())) + """

if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        outp = main(sys.stdin.readline().rstrip())
        print(outp)
"""
        if not os.path.exists("compiled"):
            os.mkdir("compiled")
        with open("compiled/main.py", "w") as r:
            r.write(compiled)

if __name__ == "__main__":
    main()