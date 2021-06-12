def fun(**k):
    print("Person Informatiion")
    for key, value in k.items():
        print(key, "-", value)


fun(Name="Rahul", Age=24, Score=9.0)
