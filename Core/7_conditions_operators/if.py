USA = ["x", "y", "z"]
UK = ["l", "m", "n","o"]
India = ["a", "b", "c","d"]
C1 = input("Enter a city name:")
C2 = input("Enter a city name:")


if C1 in USA and C2 in USA:
    print("The cities are in USA:")
elif C1 in UK and C2 in UK:
    print("The cities are in UK:")
elif C1 in India and C2 in India:
    print("The cities are in India:")
else:
    print("The cites are not in same country:")
