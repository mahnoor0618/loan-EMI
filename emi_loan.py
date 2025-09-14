def loan_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    return f"Monthly EMI = Rs {emi:.2f}"

# Example run
print(loan_emi(500000, 10, 5))
