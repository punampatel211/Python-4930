# classes.py
class Loan:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years

    def monthly_payment(self):
        from functions import calculate_loan_payment
        return calculate_loan_payment(self.principal, self.annual_rate, self.years)

class Savings:
    def __init__(self, initial_amount, monthly_contribution, annual_rate, years):
        self.initial_amount = initial_amount
        self.monthly_contribution = monthly_contribution
        self.annual_rate = annual_rate
        self.years = years

    def future_value(self):
        from functions import calculate_savings_growth
        return calculate_savings_growth(self.initial_amount, self.monthly_contribution, self.annual_rate, self.years)
