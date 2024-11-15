# Function Brain for Calculation of E = m * c * c
def brain(m):
    c = 300000000
    # e = m * c * c
    e = int(m * pow(c, 2))
    return e

# Main Function
def main():
    mass = int(input("m: "))
    einstein = brain(mass)
    print("E:", einstein)

# Function Call
main()