#input() รับข้อมูลที่ผู้ใช้พิมพ์เข้ามา float() แปลงข้อมูลเป็นตัวเลขทศนิยม
salary = float(input())

#นำเงินเดือนมาคูณ 3% 3% เขียนเป็นเลขทศนิยมคือ 0.03
tax = salary * 0.03

#นำเงินเดือนมาลบภาษี
net_salary = salary - tax

#print() ใช้แสดงผลบนหน้าจอ
print(f"{net_salary:.2f}")
