# salary.py - คำนวณเงินเดือนสุทธิ
salary = float(input("เงินเดือน: "))
ot = float(input("ค่า OT: "))
tax = float(input("ภาษี/หักอื่นๆ: "))

net_salary = (salary + ot) - tax

print(f"เงินเดือนสุทธิที่ได้รับ: {net_salary:,.2f} บาท")
