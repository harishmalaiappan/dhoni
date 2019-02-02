class cname:
    def __init__(self,name,no):
        self.a=name
        self.b=no
    def fun(self):
        print(self.a)
    def fun1(self):
        print(self.a,self.b)
c=cname('Dhoni',7)
c.fun()
c.fun1()
var={'name':['dhoni','kholi'],'Age':27}
for x in var:
    print(x)
var={'name':['dhoni','kholi'],'Age':27}
for x in var.items():
    print(x)
var={'name':['dhoni','kholi'],'Age':27}
for x in var.values():
    print(x)
var={'name':['dhoni','kholi'],'Age':27}
print(var['name'])
var={'name':['dhoni','kholi'],'Age':27}
print(var['country'])
var={'name':['dhoni','kholi'],'Age':27}
print(var.get('country'))
var={'name':['dhoni','kholi'],'Age':27}
print(var.get('country','no key'))
var={'name':['dhoni','kholi'],'Age':27}
var1={'country':['india','australia'],'no':10}
print(var+var1)
var={'name':['dhoni','kholi'],'Age':27}
var1={'country':['india','australia'],'no':10}
var.update(var1)
print(var)
var={True:'dhoni',1:'india'}
print(var[True])
var={False:'dhoni',0:'india'}
print(var[False])
var={False:'dhoni',1:'india'}
print(var[False])
def fun():
    print("success")
fun()
def add(eng,tam):
    print(eng+tam)
add(30,40)
add(30,30)
def Av(name,avg):
    print(name,"has an average",avg)
Av('dhoni','59.27')
def Av(name,avg):
    print(name,"has an average",avg)
Av('dhoni')
def Av(name,avg="NA"):
    print(name,"has an average",avg)
Av('dhoni')
def Av(name,avg):
    print(name,"has an average",avg)
Av(37)
def Av(avg,name="dhoni"):
    print(name,"has an average",avg)
Av(37)
def Av(name,avg):
    print(name,"has an average",avg)
Av(avg=37,name="dhoni")
def Av(*name):
    print(name)
Av("dhoni")
Av("dhoni","ashwin")
def Av(**name):
    print(name)
Av(Name='dhoni')
Av(avg=50,country='india')




























































































