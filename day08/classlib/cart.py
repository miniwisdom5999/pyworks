# Cart 클래스 만들기 - 장바구니

class Cart:
    li = []     #빈 리스트 생성

    def __init__(self,goods):
        Cart.li.append(goods)
        
    def __str__(self):      #여기 그냥 init해도 괜찮음
        return Cart.li
    
cart1 = Cart("계란")
print(cart1.li)

cart2 = Cart("두부")
print(cart1.li)

cart3 = Cart("커피")
print(cart1.li)



##할때마다 쌓인다. 유지된다.