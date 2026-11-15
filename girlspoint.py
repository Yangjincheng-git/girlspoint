print("这是一个专门计算我对喜欢的女生的评分的程序")
class girl:
    def __init__(self,name,age,height,weight,looking):#定义女生这一类
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.looking=looking
    def agepoint(self):#年龄分计算
        agepoint=0
        if self.age<16:
            agepoint+=60
        elif  16<=self.age<=26:
            agepoint+=100
        elif  26<self.age<=30:
            agepoint+=80
        elif 30<self.age<=35:
            agepoint+=70
        else:
            agepoint+=50
        return agepoint
    def figurepoint(self):#身材分计算
        figurepoint=0
        bmi=self.weight/((self.height/100)**2)
        if bmi<18:
            figurepoint+=60
        elif 18<=bmi<=22:
            figurepoint+=100
        elif 22<bmi<=24:
            figurepoint+=90
        elif 26<bmi<=30:
            figurepoint+=60
        else:
            figurepoint+=40
        return figurepoint
    def heightpoint(self):#身高分计算
        if self.height==173:
            heightpoint=100
        elif self.height>173:
            heightpoint=100-(self.height-173)*5
        else:
            heightpoint=100-(173-self.height)*2
        return heightpoint
        #计算总分
    def localpoint(self):
        total = (self.agepoint() + self.figurepoint() +self.heightpoint())/3
        return total
girlex=girl("小美",18,173,65,"sexy")
print(f"示例:姓名:{girlex.name}年龄:{girlex.age}身高:{girlex.height}体重:{girlex.weight}\n年龄分:{girlex.agepoint()}\n身材分:{girlex.figurepoint()}\n身高分:{girlex.heightpoint()}\n综合分:{girlex.localpoint()}")
girl_list = []
while True:
    name=input("请输入下一位女生姓名：")
    if name=='q':
        break
    age=int(input("年龄："))
    height = int(input("请输入身高(cm): "))
    weight = int(input("请输入体重(公斤): "))
    looking = input("备注信息: ")

    g = girl(name, age, height, weight, looking)
    girl_list.append(g)  # 添加到列表
for g in girl_list:
    print(f"姓名:{g.name} | 年龄:{g.age} | 身高:{g.height}cm | 体重:{g.weight}公斤")
    print(f"年龄分:{g.agepoint()} | 身材分:{g.figurepoint()} | 身高分:{g.heightpoint()}|综合分:{g.localpoint()}")