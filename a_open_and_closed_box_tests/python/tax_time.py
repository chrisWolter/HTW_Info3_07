# translated from java by ChatGPT
import sys

def main():
    global nFamilyMembers, exemption, income, taxTotal
    nFamilyMembers = 0
    exemption = 0
    income = 0.0
    taxTotal = 0.0

    # A Reader stream to read from the console
    print("Welcome to the new Berlin tax calculator.")
    income_str = input("How much did you earn last year? ")
    try:
        income = float(income_str)
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(-1)

    # Check income
    if income < 0:
        print("Even in Berlin, no one has a negative income!")
        print("Start over.")
        sys.exit(-1)

    nFamilyMembers_str = input("Enter the number of dependents you have, including yourself: ")
    try:
        nFamilyMembers = int(nFamilyMembers_str)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        sys.exit(-1)

    # Check number of family members
    if nFamilyMembers <= 0:
        print("Did you forget to count yourself?")
        print("Start over.")
        sys.exit(-1)

    # Compute tax total
    if income < 10000:
        taxTotal = 0.12 * income
    elif income < 50000:
        taxTotal = 300.00 + 0.24 * (income - 10000)
    else:
        taxTotal = 1500.00 + 0.36 * (income - 50000)

    for i in range(nFamilyMembers + 1):
        taxTotal = taxTotal - 100

    # Check negative tax
    if taxTotal < 0:
        taxTotal = 0

    print("=€=€=€=€=€=€=€=€=€=€=€=€=€=€=€")
    print("Wowereit & Sarrazin GmbH")
    print("Tax bill")
    print(f"Your income was {income} €.")
    print(f"You have {nFamilyMembers} family members.")
    print(f"Your total tax is {taxTotal} €.")
    print(f"Family member tax saving is {nFamilyMembers * 100} €.")
    print("=€=€=€=€=€=€=€=€=€=€=€=€=€=€=€")


if __name__ == "__main__":
    main()
