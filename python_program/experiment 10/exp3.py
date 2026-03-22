class Product:
    def __init__(self,product_id,product_name,price,quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total_amount = 0
        
    def calculate_total(self):
        self.total_amount = self.price * self.quantity
    def display(self):
        print('product id:',self.product_id)
        print('product name:',self.product_name)
        print('price:',self.price)
        print('quantity:',self.quantity)
        print('total amount:',self.total_amount)
        
pid = input('enter product id:')
pname = input('enter product name:')
price = float(input('enter price:'))
quantity = int(input('enter quantity:'))
p = Product(pid,pname,price,quantity)
p.calculate_total()
p.display()        