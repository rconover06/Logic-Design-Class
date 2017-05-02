# Raul Conover
# Program that shows ecamples for: string concatenation, floor division,
# modulus, and a while loop.

while True:
    total = int(input("Enter total seconds:"))
    hours = total // 3600
    seconds = total % 3600

    days = hours // 24
    hours = hours % 24

    mins = seconds // 60
    seconds = seconds % 60

    answer = ""

    if days > 1:
        answer = str(days) + " days "
    else:
        if days == 1:
            answer = "1 day "

    if hours > 1:
        answer = answer + str(hours) + " hours "
    else:
        if hours == 1:
            answer = answer + str(hours) + " 1 hour "

    answer = answer + str(mins) + " minutes " + str(seconds) + " seconds."
    print(answer)
    print()
