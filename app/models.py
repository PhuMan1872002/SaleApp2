from app import db
from sqlalchemy import Column,Integer,String,ForeignKey,Float

class Category(db.Model):
    __tablename__='category'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50),nullable=False,unique=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image=Column(String(100))
    category_id = Column(Integer,ForeignKey(Category.id), nullable=False)
if __name__=='__main__':
    from app import app
    with app.app_context():

        p1=Product(name='Điện thoại 1',price=2400000,category_id=1,image="https://cdn.tgdd.vn/Files/2021/12/25/1406752/vivov23e-58_1280x718-800-resize.jpg")
        p2 = Product(name='Điện thoại 2', price=2500000, category_id=1,
                     image='https://image-us.24h.com.vn/upload/4-2020/images/2020-11-09/1-1604858150-367-width660height440.jpg')
        p3 = Product(name='Tablet 3', price=2900000, category_id=2,
                     image='https://cdn.tgdd.vn/Files/2021/12/25/1406752/vivov23e-58_1280x718-800-resize.jpg')
        p4 = Product(name='Tablet 4', price=30000000, category_id=2,
                     image='https://cdn.tgdd.vn/Files/2021/12/25/1406752/vivov23e-58_1280x718-800-resize.jpg')
        db.session.add_all([p1,p2,p3,p4])
        db.session.commit()
