# Phần 1 : Input/output 
# Dữ liệu đầu vào 
# num_branches : Số lượng chi nhánh cần quản lý , int 
# attendance : Số lượng học viene học của từng lớp , (int) . Người nhập trực tiếp từ bàn phím qua hàm input 
# Output 
# In ra thông báo trạng thái của từng lớp tương ứng với số lượng sĩ số đã nhập ngay sau khi kiểm tra hợp lệ .
# Các câu thông báo lỗi hoặc bỏ qua nếu rơi vào các Edge Cases 
# Đề xuất giải pháp 
# Cấu trúc vòng lặp lồng nhau 
# Vòng lặp bên ngoài (for branch in range(1,num_branches+1)): Duyệt qua từng chi nhánh thứ 1 đến chi nhánh cuối cùng
# Vòng lặp bên ngoài (for class_num in range(1,3)): Cố định chạy đúng 2 lần cho 2 lớp của mỗi chi nhánh 
# Xử lý bẫy dữ liệu (Edge Cases) bằng vòng lặp while bắt buộc :
# Để giải quyết bẫy 1  (Nhập số âm), ta bọc nhập sĩ của mỗi lớp trong một vòng lặp while true 
# Nếu người dùng nhập số âm , hệ thống sẽ in thông báo lỗi và bắt người dùng nhập lại ngay tại lớp đó (vòng while tiếp tục lặp)
# Nếu nhập số >=0 , ta dùng lệnh break để thoát khỏi vòng whhile kiểm tra và tiến hành phân loại trạng thái 
# Phân loại trạng thái (Cấu trúc if - elif - else):

# attendance == 0: Thông báo vắng toàn bộ và bỏ qua kiểm tra (Thỏa mãn Bẫy 2).

# attendance >= 20: In trạng thái "Lớp học ổn định".

# 0 < attendance < 20: In trạng thái "Lớp cần được nhắc nhở theo dõi".

print("===== HỆ THỐNG ĐÁNH GIÁ SĨ SỐ LỚP HỌC =====")


while True:
    num_branches_input = input("Nhập số lượng chi nhánh: ").strip()
    if num_branches_input.isdigit() and int(num_branches_input) > 0:
        num_branches = int(num_branches_input)
        break
    print("Số lượng chi nhánh phải là một số nguyên dương lớn hơn 0. Vui lòng nhập lại!")


for branch_idx in range(1, num_branches + 1):
    print(f"\nChi nhánh {branch_idx}:")
    
   
    for class_idx in range(1, 3):
        
     
        while True:
            attendance_input = input(f"  Nhập số học viên đi học của lớp {class_idx}: ").strip()
            
           
            if attendance_input.startswith('-') and attendance_input[1:].isdigit():
                print("  [Lỗi] Số học viên không hợp lệ. Vui lòng nhập lại.")
            elif attendance_input.isdigit():
                attendance = int(attendance_input)
                break 
            else:
                print("  [Lỗi] Vui lòng nhập một số nguyên hợp lệ.")

        
        if attendance == 0:
            # Xử lý Bẫy 2: Lớp vắng toàn bộ
            print(f"  -> Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
        elif attendance >= 20:
            print(f"  -> Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp học ổn định")
        else:
            print(f"  -> Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp cần được nhắc nhở theo dõi")

print("\n===== ĐÃ HOÀN THÀNH ĐÁNH GIÁ TOÀN HỆ THỐNG =====")