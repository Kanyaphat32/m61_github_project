#input() รับค่าจากผู้ใช้ float() แปลงข้อมูลเป็นตัวเลขทศนิยม
units = float(input("กรอกจำนวนหน่วยไฟฟ้า: "))

#ค่าไฟคิดหน่วยละ 4.50 บาท นำจำนวนหน่วยไฟฟ้ามาคูณ 4.50
electricity_bill = units * 4.50

#print() ใช้แสดงผล
print(f"ค่าไฟฟ้า = {electricity_bill:.2f} บาท")
