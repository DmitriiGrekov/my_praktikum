class Record():
    def __init__(self,amount,date,comment):
        self.amount = amount
        self.date=date
        self.comment = comment
    def record(self):
        return {'amount':self.amount,'date':self.date,'comment':self.comment}
class Calculator():
    def __init__(self,limit):
        self.limit = limit
        self.records = []
    def show_all_records(self):
        print(self.records)

    def add_record(self,amount,date,comment):
        new_record = Record(amount,date,comment)
        self.records.append(new_record.record())


calc = Calculator(10000)
calc.add_record(1000,'21.09.1999','Съел новое блюдо')
calc.add_record(200,'22.09.1999','Купил картошку')
    

