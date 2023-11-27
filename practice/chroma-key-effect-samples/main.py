import sys
import math

def getDistance(r1: int, g1: int, b1: int, r2: int, g2: int, b2: int) -> float:
    return math.sqrt( (r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2 )


def main(cin) -> str:
    Cr, Cg, Cb, T, Fr, Fg, Fb, Br, Bg, Bb = list(map(int, cin.split(" ")))
    if getDistance(Fr, Fg, Fb, Cr, Cg, Cb) <= T:
            return f"{Br} {Bg} {Bb}"
    return f"{Fr} {Fg} {Fb}"

    


    
    
if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        print(main(sys.stdin.readline().rstrip()))  
