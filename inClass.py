def create_account(accounts, account_number: str, initial_balance: float):
    accounts[account_number] = initial_balance


def deposit(accounts, account_number: str, amount: float):
    accounts[account_number] += amount


def withdraw(accounts, account_number: str, amount: float):
    accounts[account_number] -= amount


def get_balance(accounts, account_number: str) -> float:
    return accounts[account_number]


def main():
    accounts = {}
    assert accounts == {}

    create_account(accounts, '12345', 0)
    assert accounts['12345'] == 0

    deposit(accounts, '12345', 500)
    assert (accounts['12345'] == 500)
    withdraw(accounts, '12345', 25)
    assert accounts['12345'] == 475

    balance = get_balance(accounts, '12345')
    assert balance == 475
    print(f'Your account has a balance of ${balance:.2f}')


if __name__ == "__main__":
    main()
