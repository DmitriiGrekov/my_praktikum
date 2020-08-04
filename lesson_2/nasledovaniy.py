class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show(self):
        print(f'{self.name} ({self.phone})')

# объявляем класс Friend, дочерний по отношению к классу User
class Friend(User):
    #пишем конструктор класса наследника
    def __init__(self,name,phone,address):
        #Наследуем функциональность конструктора класса родителя
        super().__init__(name,phone)
        #добавляем новую функциональность
        self.address = address

    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone} || Адресс: {self.address}')

# создаём объекты User и Friend
father = User("Дюма-отец", "+33 3 23 96 23 30")
father.show()
son = Friend("Дюма-сын", "+33 3 23 96 23 30",'Дом пердяево')
son.show()
