from classes import Loan, Savings

def main():
    while True:
        print("Finance Calculator")
        print("1. Loan Payment Calculation")
        print("2. Savings Growth Calculation")
        print("3. Retirement Savings Calculation")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            principal = float(input("Enter the loan principal amount: "))
            annual_rate = float(input("Enter the annual interest rate (in %): "))
            years = int(input("Enter the number of years: "))
            loan = Loan(principal, annual_rate, years)
            print(f"Monthly Loan Payment: ${loan.monthly_payment():.2f}")
        elif choice == '2':
            initial_amount = float(input("Enter the initial savings amount: "))
            monthly_contribution = float(input("Enter the monthly contribution amount: "))
            annual_rate = float(input("Enter the annual interest rate (in %): "))
            years = int(input("Enter the number of years: "))
            savings = Savings(initial_amount, monthly_contribution, annual_rate, years)
            print(f"Future Savings Value: ${savings.future_value():.2f}")
        elif choice == '3':
            current_savings = float(input("Enter the current savings amount: "))
            monthly_contribution = float(input("Enter the monthly contribution amount: "))
            annual_rate = float(input("Enter the annual interest rate (in %): "))
            years_until_retirement = int(input("Enter the number of years until retirement: "))
            retirement_savings = Savings(current_savings, monthly_contribution, annual_rate, years_until_retirement)
            print(f"Retirement Savings Value: ${retirement_savings.future_value():.2f}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
