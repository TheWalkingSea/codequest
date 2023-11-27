def main(cin):
    cin = map(int, cin.split(" ")).sort()
    val, cnt = (cin[0], 0)
    for i in cin:
        if i == val:
            cnt += 1
        else:
            if cnt == 3:
                return True
            val, cnt = (i, 0)