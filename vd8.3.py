#Chương trình phân loại sinh viên theo ddierm trung bình
diem_TB = eval(input("Nhập điểm trung bình:"))
if diem_TB >=0 and diem_TB <= 10:
    if diem_TB <5:
        print("Xếp loại YẾU")
    elif diem_TB <6:
        print("Xếp loại TRUNG BÌNH")
    elif diem_TB <7:
        print("Xếp loại TRUNG BÌNH-KHÁ") 
    elif diem_TB <8:
        print("Xếp loại KHÁ")
    elif diem_TB <9:
        print("Xếp loại GIỎI")    
    else:
        print("Xếp loại XUẤT SẮC")
else:
    print("Điểm nhập vào không hợp lệ")
