import xlrd
x1 = xlrd.open_workbook("test.xls")
sheet1=x1.sheet_by_name("理级")
b=sheet1.row_values(0, 0, 15)
a=sheet1.col_values(1, 1, 1200)
name=input()
i1=0#X
i2=0#Y
while(i2<1200):
    if(a[i2]==name):
        i2+=1
        while(i1<15):
            c=sheet1.row_values(i2, 0, 15)
            print(b[i1],":",c[i1])
            i1+=1
        break
    else:
        i2+=1
