import depression


def main():
    bank_account_balance = float(input("Add meg a bankszámlád egyenlegét! "))
    dep = depression.Depression(bank_account_balance)
    print(f"A pénzed euróban: {dep.huf_to_euro()}")
    print(f"A pénzed dízelben (liter): {dep.liters_of_disel()}")
    print(f"A pénzed meggysörben (liter): {dep.liters_of_mort_subite()}")



if __name__ == "__main__":
    main()
