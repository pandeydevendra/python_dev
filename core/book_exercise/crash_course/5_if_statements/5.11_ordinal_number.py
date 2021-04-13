"""5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if - elif - else chain inside the loop to print the proper ordinal end-
ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th" , and each result should be on a separate line."""
ordinal_numbers = [number for number in range(1, 10)]
print(ordinal_numbers)
for number in ordinal_numbers:
    if number <= 3:
        if number == 1:
            print("{}st".format(number))
        elif number == 2:
            print("{}nd".format(number))
        else:
            print("{}rd".format(number))
    else:
        print("{}th".format(number))

#completed chapter_05 :; formally