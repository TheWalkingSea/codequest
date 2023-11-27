def main(cin):

    v0, x0 = map(lambda x: float(x), cin.split(":"))
        

    if v0 >= x0:
        print("SWERVE")
    elif 5*v0 >= x0:
        print("BRAKE")
    else:
        print("SAFE")