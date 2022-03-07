import depression


def main():
    bank_account_balance = float(input("Add meg a bankszámlád egyenlegét! "))
    dep = depression.Depression(bank_account_balance)
    print(f"A pénzed euróban: {dep.huf_to_euro()}")
    print(f"A pénzed dízelben (liter): {dep.liters_of_disel()}")


if __name__ == "__main__":
    main()