weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

print(f"{bmi:.2f}")

if bmi < 18.5:
    print("น้ำหนักน้อย")
elif bmi < 25:
    print("ปกติ")
elif bmi < 30:
    print("น้ำหนักเกิน")
else:
    print("อ้วน")