class Contact:
    #конструктор
    def __init__(self,name,phone,address,birthday):
        self.name=name
        self.phone = phone
        self.address = address
        self.birthday = birthday
        print(f'Создан новый контакт {name}')

    #метод
    def show(self):
        print(f'Имя: {self.name}, телефон: {self.phone}, день рождения: {self.birthday}')
    

    def __str__(self):
        """Python обращается к этому методу когда он видит, что необходимо преобразовать объект в строку"""
        return 'Контакт: '+self.name


leo= Contact(name='Лев Толсой',phone='7292732322',address= 'Ясная поляна',birthday='21.01.2000')
tom = Contact('Том Круз','8239829232','Сша','9.09.1930')

print()
print(leo)
