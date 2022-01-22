#lex_auth_012727119215337472135
#Start writing your code here
class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None

    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name

    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg

    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available

    def get_flower_name(self):
        return self.__flower_name

    def get_price_per_kg(self):
        return self.__price_per_kg

    def get_stock_available(self):
        return self.__stock_available

    def validate_flower(self):
        flowers=["Orchid","Rose","Jasmine"]
        converted_flowers=[item.upper() for item in flowers]
        if self.get_flower_name().upper() in converted_flowers:
            return True
        else:
            return False

    def validate_stock(self,required_quantity):
        if required_quantity<=self.get_stock_available():
            return True
        else:
            return False

    def check_level(self):
        if self.get_flower_name().upper()=="ROSE":
            order=25
            if self.get_stock_available()<order:
                return True
            else:
                return False
        elif self.get_flower_name().upper()=="ORCHID":
            order=15
            if self.get_stock_available()<order:
                return True
            else:
                return False
        elif self.get_flower_name().upper()=="JASMINE":
            order=40
            if self.get_stock_available()<order:
                return True
            else:
                return False
        else:
            return False



    def sell_flower(self,required_quantity):
        if self.validate_flower()==True and self.validate_stock(required_quantity)==True:
            self.__stock_available-=required_quantity
            return self.__stock_available
        else:
            return self.__stock_available

flower = Flower()
flower.set_flower_name(input())
flower.set_price_per_kg(int(input()))
flower.set_stock_available(int(input()))
flower.validate_flower()
flower.validate_stock(int(input()))
print(flower.sell_flower(int(input())))
print(flower.check_level())
