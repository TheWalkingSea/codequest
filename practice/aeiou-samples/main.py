def main(cin):
    cnt = 0
    for char in cin:
        if char.upper() in ["A", "E", "I", "O", "U"]:
            cnt += 1
    print(cnt)
