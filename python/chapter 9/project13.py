class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ordr2):
        return self.price > ordr2.price
    


ordr1=order("chips",20) 
ordr2=order("lays",15)      

print(ordr1>ordr2)