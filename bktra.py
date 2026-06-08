products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products(products_list):
    if len(products) == 0:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
    for product in products:
        print("ID  | TÊN SẢN PHẨM | GIÁ BÁN   ")
        print(f"{product["id"]} | {product["name"]} | {product["price"]}")
        
def add_product(products_list):
    check = False
    while True:
        new_id_product = input("Nhập mã sản phẩm")
        if new_id_product == "":
            print("Id sản phẩm không được để trống")
            check = True
        new_product = input("Nhập tên sản phẩm")
        if new_product == "":
            print("Tên sản phẩm không được để trống")
            check = True
        new_price = float(input("Nhập giá sản phẩm"))
        if new_price < 0:
            print("giá sản phẩm không hợp lệ")
            check = True
        new_product = {
            "id" : new_id_product,
            "name" : new_product,
            "price" : new_price
        }
        print("Thêm sản phẩm thành công")
        break
    
    products.append(new_product)
    
def update_price(products_list):
    product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
    
    found_product = None
    for product in products:
        if product["id"] == product_id:
            found_product = product
            break
            
    if found_product == None:
        print("Không tìm thấy sản phẩm mang mã " + id + " trong hệ thống!")
        return
    
    while True:
        id_input = input("Nhập id mới: ")
        if id_input != None:
            product["id"] = id_input
            break
        print("ID KHÔNG HỢP LỆ!")

    while True:
        new_name = input("Nhập tên sản phẩm mới: ")
        if new_name != None:
            product["name"] = new_name
            break
        print("TÊN SẢN PHẨM KHÔNG HỢP LỆ!")
    while True:
        new_price = float(input("Nhập giá sản phẩm mới: "))
        if new_price != None:
            product["price"] = new_price
            break
        print("GÍA SẢN PHẨM KHÔNG HỢP LỆ!")

    print("Cập nhật sản phẩm thành công!")
while True:
    print("====================================")
    print("    QUẢN LÝ CỬA HÀNG - MINI STORE   ")
    print("====================================")
    print("1.Xem danh sách sản phẩm hiện có")
    print("2.Thêm mới một sản phẩm")
    print("3.Cập nhật giá sản phẩm theo ID")
    print("4.Thoát chương trình")
    choice = input("Chọn chức năng:")
    match choice:
        case "1":
            show_products(products)
        case "2":
            add_product(products)
        case "3":
            update_price(products)
        case "4":
            print("Thoát chương trình")
            break