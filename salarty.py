# salary.py - โปรแกรมคำนวณเงินเดือนสุทธิ

def calculate_salary():
    print("=== โปรแกรมคำนวณเงินเดือนสุทธิ ===")
    
    # รับค่าข้อมูลจากผู้ใช้
    base_salary = float(input("กรอกเงินเดือนพื้นฐาน (บาท): "))
    OT = float(input("กรอกค่าโอที/เบี้ยขยัน (บาท): "))
    
    # คำนวณประกันสังคม (5% ของเงินเดือน แต่สูงสุดไม่เกิน 750 บาท)
    social_security = min(base_salary * 0.05, 750)
    
    # คำนวณหักภาษี ณ ที่จ่ายแบบคร่าวๆ (เช่น 3%)
    tax = base_salary * 0.03
    
    # คำนวณรายรับรวม และ รายจ่ายรวม
    total_income = base_salary + OT
    total_deduction = social_security + tax
    
    # คำนวณเงินเดือนสุทธิ
    net_salary = total_income - total_deduction
    
    # แสดงผลลัพธ์
    print("\n--- สรุปยอดเงินเดือน ---")
    print(f"รายรับรวม: {total_income:,.2f} บาท")
    print(f"หัก ประกันสังคม: {social_security:,.2f} บาท")
    print(f"หัก ภาษี (3%): {tax:,.2f} บาท")
    print(f"รายจ่ายหักรวม: {total_deduction:,.2f} บาท")
    print("-------------------------")
    print(f"เงินเดือนสุทธิที่จะได้รับ: {net_salary:,.2f} บาท")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    calculate_salary()
