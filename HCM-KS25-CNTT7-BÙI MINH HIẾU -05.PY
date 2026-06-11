labour = [
    {
    "id" :"TS001"
    "name":"Thiet ke giao dien App",
    "employment":"Nguyễn văn A"
    "date_compl" : 10,
    "date": 14,
    "progress_discrepancies":4,
    "status":"Quá hạn"
    }
]
def show_work():
    if not labour:
        print("Danh sách đang để trống")
        return
    print("___" *30)
    print("id":<5"|Tên công việc/nhiệm vụ+":<15"|Tên nhân viên":<10 "|Ngày dự kiến":<5 "|Ngày thực tế":<5 "|Chêng lệch":<5 "|trạng thái tiến độ":<5)
    
    for item in labour:
        print({item['id']} : <5"|" {item['name']}"|"{item['date_compl']}"|"{item['name']}:<10 )   
        
def add_work():
    new_id = input("Nhập id")    
    new_name = input("Nhập tên công việc")
    new_name_employment = input("Nhập tên nv mới")
    new_date = input("Nhập ngày dự kiến ")
    new_compl = input("Nhập số thực tế")

def update_list(employment):
    
        
        
        
             
def menu ():
    while True:
        print("_____________Quản lý công việc___________")
        print("1.Hiển thị danh sách công việc")
        print("2.Thêm công việc mới")
        print("3.Cập nhật tiến độ")
        print("4.Xoá công việc khỏi dự án")
        print("5.Tìm kiếm côm việc")
        print("6.Thống kê trạng thái tiến độ")
        print("7.Phân loại tiến độ tự động")
        print("8.Thoát chương trình")
        choice = input("Nhập lựa chọn(1-8)")

        match choice:
                case '1':
                    show_work
                case '2':
                   add_work
                
                case '3':
                    update_list
                    
                case '4':
                    
                case '5':
                    
                case '6':
                    
                case '7'
                
                case '8':
                    print("Thoát chương trình xin cảm ơn")
                    break
                case _:
                    print("Vui lòng nhập lại")
    
