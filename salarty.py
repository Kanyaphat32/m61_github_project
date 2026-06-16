salary = float(input("กรอกเงินเดือน: "))
tax = salary * 0.05
net_salary = salary - tax

print(f"เงินเดือนสุทธิ = {net_salary:.2f} บาท")