from dataclasses import dataclass

@dataclass
class InventoryItem:
    
    name: str 
    unit_price: float
    quantity_on_hand: int=0 

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


i  = InventoryItem('Modak', 17.5, 75)
print(i.total_cost())
print(i)
j = InventoryItem('bondi ke laddo', 10, 75)
print(j.total_cost())
print(j)
print(i == j)



#* ==============================================
#^ ------ nested data class ----------------- 

# @dataclass
# class Address:
#     street:str
#     city:str
#     zip_code:str 

# @dataclass
# class Person:
#     name:str
#     age:str
#     address:Address

# ad = Address('Vijay Nagar','Indore','452001',)

# person = Person("Vishal", '20', ad) 
# print(person)