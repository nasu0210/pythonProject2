import pickle

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total=price*quantity

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print("상품이 추가되었습니다.")

    def view_products(self):
        if len(self.products) == 0:
            print("상품이 없습니다.")
        else:
            print("상품 목록:")
            for product in self.products:
                print(f"이름: {product.name}, 가격: {product.price}원, "
                      f"수량: {product.quantity}, 금액:{product.total}원")

    def update_product(self, name, price, quantity):
        for product in self.products:
            if product.name == name:
                product.price = price
                product.quantity = quantity
                product.total=price*quantity
                print("상품 정보가 업데이트되었습니다.")
                return
        print("해당 이름의 상품을 찾을 수 없습니다.")

    def delete_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("상품이 삭제되었습니다.")
                return
        print("해당 이름의 상품을 찾을 수 없습니다.")

    def save_products(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.products, file)
        print("상품 정보가 저장되었습니다.")

    def load_products(self, filename):
        try:
            with open(filename, "rb") as file:
                self.products = pickle.load(file)
            print("상품 정보가 불러와졌습니다.")
        except FileNotFoundError:
            print("저장된 상품 정보 파일이 없습니다.")

def main():
    product_manager = ProductManager()

    while True:
        print("\n===== 상품 관리 프로그램 =====")
        print("1. 상품 추가")
        print("2. 상품 조회")
        print("3. 상품 수정")
        print("4. 상품 삭제")
        print("5. 상품 정보 저장")
        print("6. 상품 정보 불러오기")
        print("7. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            name = input("상품 이름을 입력하세요: ")
            price = int(input("상품 가격을 입력하세요: "))
            quantity = int(input("상품 수량을 입력하세요: "))
            product_manager.add_product(name, price, quantity)
        elif choice == "2":
            product_manager.view_products()
        elif choice == "3":
            name = input("수정할 상품의 이름을 입력하세요: ")
            price = int(input("새로운 가격을 입력하세요: "))
            quantity = int(input("새로운 수량을 입력하세요: "))
            product_manager.update_product(name, price, quantity)
        elif choice == "4":
            name = input("삭제할 상품의 이름을 입력하세요: ")
            product_manager.delete_product(name)
        elif choice == "5":
            filename = input("저장할 파일 이름을 입력하세요: ")
            product_manager.save_products(filename)
        elif choice == "6":
            filename = input("불러올 파일 이름을 입력하세요: ")
            product_manager.load_products(filename)
        elif choice == "7":
            print("상품 관리 프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택지를 입력하세요.")

if __name__ == "__main__":
    main()
