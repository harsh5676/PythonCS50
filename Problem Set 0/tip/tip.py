def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    rem = float(d.replace("$", ""))
    return rem


def percent_to_float(p):
    remove = float(p.replace("%", ""))
    remove = remove/100
    return remove


main()