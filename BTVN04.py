print("===== HỆ THỐNG CHUẨN HÓA MÃ ĐĂNG KÝ KHÓA HỌC =====")

while True:
    num_tickets_input = input("Nhập số lượng phiếu đăng ký cần xử lý: ").strip()
    
   
    if not num_tickets_input.isdigit() or int(num_tickets_input) <= 0:
        print("Số lượng phiếu đăng ký không hợp lệ")
        print("Chương trình kết thúc.")
        exit()  
    else:
        num_tickets = int(num_tickets_input)
        break


for idx in range(1, num_tickets + 1):
    print(f"\nNhập phiếu đăng ký thứ {idx}:")
    raw_string = input(" -> ")
    
  
    parts = [part.strip() for part in raw_string.split("|")]
    
    
    if len(parts) != 4:
        print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
        continue
        
    
    raw_name, raw_course, raw_student_id, raw_email = parts
    
  
    name = raw_name.title()
    course = raw_course.title()
    student_id = raw_student_id.upper()
    email = raw_email.lower()
    
   
    if "@" not in email:
        print("Email không hợp lệ. Bỏ qua phiếu này")
        continue
        
    
    if len(student_id) < 5:
        print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
        continue
        
    
    course_slug = course.upper().replace(" ", "-")
    confirmation_code = f"{student_id}_{course_slug}"
    
    
    print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
    print(f"Học viên: {name}")
    print(f"Khóa học: {course}")
    print(f"Mã học viên: {student_id}")
    print(f"Email: {email}")
    print(f"Mã xác nhận: {confirmation_code}")
    print("======================================")