class user_input:
    def __init__(self):
        self.area = input("Enter area: ")

    def h_dis(self,area):
        if self.area == "aavadi":
            self.hot_rate = [{"hotel":"hotel1", "rate":"5-star"},
                        {"hotel":"hotel2", "rate":"4.5-star"},
                        {"hotel":"hotel3", "rate":"4-star"},
                        {"hotel":"hotel4", "rate":"4.5-star"}]
        elif self.area == "tharamani":
            self.hot_rate = [{"hotel":"hotel1", "rate":"5-star"},
                        {"hotel":"hotel2", "rate":"4.5-star"},
                        {"hotel":"hotel3", "rate":"4-star"},
                        {"hotel":"hotel4", "rate":"4.5-star"}]
        elif self.area == "thiruvanmaiyur":
            self.hot_rate = [{"hotel":"hotel1", "rate":"5-star"},
                        {"hotel":"hotel2", "rate":"4.5-star"},
                        {"hotel":"hotel3", "rate":"4-star"},
                        {"hotel":"hotel4", "rate":"4.5-star"}]
        elif self.area == "guindy":
            self.hot_rate = [{"hotel":"hotel1", "rate":"5-star"},
                        {"hotel":"hotel2", "rate":"4.5-star"},
                        {"hotel":"hotel3", "rate":"4-star"},
                        {"hotel":"hotel4", "rate":"4.5-star"}]
        else:
            print("area out of survey!")
    def disp(self):        
        for i in self.hot_rate:
            f={}
            f=i
            for k,v in f.items():
                print(k,"\t--- \t",v,)

class hot_sel(user_input):
    def __init__(self):
        self.uh = input("Enter hotel: ")
        self.h=["hotel1","hotel2","hotel3","hotel4"]
        #fself.di()
        

    def di(self):
        for i in self.h:
            print("\n",i)
                
    def uh_val(self):
        for i in self.h:
            if (i != self.uh):
                raise ValueError("Invalid hotel")
            
class dish(hot_sel):
    def __init__(self):
        self.f=["dish1","dish2","dish3","dish4","dish5"]
        self.disp()
        self.user_dis= input("Enter dish: ")

    def dish_val(self):
        for i in self.f:
            if (i != self.user_dis):
                raise ValueError ("dish not available")
            else:
                print("Packing....")
                break
            
    def disp(self):
        print("\n Available dish")
        print("---------------")
        for i in self.f:
            print(i)
class swiggy:
    def __init__(self,area,hotel,dish):
        self.p = area
        self.h = hotel
        self.d = dish
        
    def beforeorder(self):
        print("order details",self.p,self.h,self.d)

    def display(self):
        print("order confirmed :",self.d," \n @",self.h," in ",self.p)

class user_dis(swiggy):
    def __init__(self):
        self.bill = 500
        self.sgst = 5
        self.cgst = 10
        self.total = (self.bill+self.sgst+self.cgst)

    def delivery(self):
        self.addr = input("Enter address: ")


    def addvalid(self):
        if isinstance (self.addr,str):
            if isinstance(len(self.addr) <= 25):
                raise ValueError ("enter valid address")
            elif self.addr != None:
                raise ValueError ("invalid address")
                
        
    def display(self):
        print("Delivary address : ",self.addr)
        print("Total bill Rs.",self.total)
        ob1.display()


ob = user_input()
ob.h_dis(ob.area)
ob.disp()
h = hot_sel()
d = dish()
d.dish_val()
ob1 = swiggy(ob.area,h.uh,d.user_dis)
ob1.beforeorder()
ob2 = user_dis()

ob2.delivery()
ob2.addvalid
ob2.display()
