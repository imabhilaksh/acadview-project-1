from datetime import datetime
class Spy:
    def __init__(self,salutation,name,age,rating):
        self.salutation=salutation
        self.name=name
        self.age=age
        self.rating=rating
        self.chats=[]
        self.status=True



spy=Spy('Mr.','Abhilaksh',20,3.5)


class ChatMessage:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me

friend1=Spy('Mr.','Kartik',29,4.3)
friend2=Spy('Mr.','Anuj Dhawan',24,4.5)

friends=[friend1,friend2]
