from collections import namedtuple

Product = namedtuple('Product', ['title', 'description', 'price','category', 'thumbnail', 'images'])


product1 = Product(title='Phone', description='Smartphone with advanced features', price=500, category='Electronics', thumbnail='phone.jpg', images=['image1.jpg', 'image2.jpg'])
product2 = Product(title='Fridge', description='Very cold fridge', price=450, category='Electronics', thumbnail='fridge.jpg', images=['image3.jpg', 'image4.jpg'])

print(product1.title)
print(product1.price)
print(product1.images)
for key, value in product2._asdict().items():
    print(f"{key}: {value}")
