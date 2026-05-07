from datetime import datetime


class User:
    def __init__(self, name, tahunLahir, hobby):
        self.name = name
        self.usia = datetime.now().year - tahunLahir 
        self.hoby = hobby
    def tampilkan(self):
        print("nama saya ", self.name)
        print("usia saya ", self.usia)
        if isinstance(self.hoby, list):
            print("hobby saya adalah : ")
            for h in self.hoby:
                print("-", h)
        else: 
            print("hobby saya adalah ", self.hoby)
            
        




a = User("usera", 1995, ["jalan kaki", "berlari"])
b = User("userb", 2000, "bermain")
a.tampilkan()
b.tampilkan()


users = ["andy", "budi"]
user = {
    "name" : "andy",
    "age ": 10
}



