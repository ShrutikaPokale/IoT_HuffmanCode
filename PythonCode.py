def last_two(arg,count):            #adding last to probabilities
    arg.sort(reverse=True)
    z=arg[-1]+arg[-2]
    add_values.append(z)
    new=arg[0:-2]
    new.append(z)
    new.sort(reverse=True)
    columns.append(new)
    if len(new)==2:
        codeft(new)
    return(new)
    
def codeft(x):                  #assigning codes
    i=len(columns)
    check_code=[]
    while i>0:
        if i==len(columns):
            code.append([x[0],'0'])
            code.append([x[1],'1'])
        else:
            idx=columns[i].index(add_values[i-1])   
            for x in code:
                if x not in check_code:
                    if x[0]==columns[i][idx]:
                        coder=x[1]
                        check_code.append(x)
                        break
            code.append([columns[i-1][-2],coder+'0'])
            code.append([columns[i-1][-1],coder+'1'])
                    
        i=i-1
            
print("Give messages and probabilities separated by ':' and different messages separated by ','")
d=input()
d1=[]
data={}
d1=d.split(",")
for i in range(len(d1)):
    z=d1[i].index(":")
    data[d1[i][:z]]=float(d1[i][z+1:])
#data={'A':0.125,'B':0.125,'C':0.125,'D':0.125,'E':0.125,'F':0.125,'G':0.125,'H':0.125}
n=len(data)
print("The input given: ",data)
msg=data.keys()                             #keys i.e msg signals
values=[]                                   #values i.e probabilities
lst=[ [k,v] for k, v in data.items() ]
for i in range (len(lst)):
    values.append(lst[i][-1])
sum=0
for x in values:
    sum=sum+x
if sum==1:
    final_code={}
    code=[]                                     #storing codes one by one
    if len(values)<=2:
        if len(values)==2:
            values.sort(reverse=True)
            code.append([values[0],'0'])
            code.append([values[1],'1'])
        else:
            code.append([values[0],'0'])
    else:
        add_values=[]                               #storing addition values of last two prob one by one
        columns=[]                                  #storing values of columns
        columns.append(values)
    
        for i in range(n-2):
            if i==0:
                val=last_two(values,i)
            else:
                val=last_two(val,i)
        check=[]
        
        for x in code:
            if (x[0] in add_values and x[0] in values):
                flag=0
                for k in range(len(check)):
                    if x[0]==check[k][0]:
                        flag=1
                        break
                if flag==0:
                    check.append(x)
    for x in msg:
        for i in range(len(code)):
            if data[x]==code[i][0]:
                if len(code)<=2:
                    final=code[i][1] 
                    break
                else:
                    if code[i] not in check:
                        check.append(code[i])
                        final=code[i][1]
                        break
    
        final_code[x]=final
    print("The coded message signals: ",final_code)
    
else:
    print("The input is invalid. The sum of the probabilities should be equal to 1")
    

