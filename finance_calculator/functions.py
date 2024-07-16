# functions.py
def calculate_loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
    return payment

def calculate_savings_growth(initial_amount, monthly_contribution, annual_rate, years):
    total_months = years * 12
    growth = initial_amount
    for month in range(total_months):
        growth += monthly_contribution
        growth *= (1 + annual_rate / 12 / 100)
    return growth

def calculate_retirement_savings(current_savings, monthly_contribution, annual_rate, years_until_retirement):
    return calculate_savings_growth(current_savings, monthly_contribution, annual_rate, years_until_retirement)
