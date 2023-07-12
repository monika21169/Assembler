#code for ques5
import math
print("Enter space in memory ")
m=str(input())

print("4 Types Of Memory")
print("1. Bit Addressable Memory - Cell Size = 1 bit")
print("2. Nibble Addressable Memory - Cell Size = 4 bit")
print("3. Byte Addressable Memory - Cell Size = 8 bits(standard)")
print("4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")
print("Input how the memory is addressed among(1,2,3,4) ")

h=int(input())

j=0
i=m[j]
l2=[]
l1=['0','1','2','3','4','5','6','7','8','9',' ']

l3=['K','M','G','T']
l5=[2**10,2**20,2**30,2**40]
l8=[10,20,30,40]
l4=['b','B']
l9=[1,3]
l6=[1,8]

l7=[]

while(j<10000):
    if(m[j] in l1):
        if(m[j]!=' '):
            l7.append((m[j]))
        j=j+1
        continue
    else:
        l2.append(m[j])
        l2.append(m[j+1])
        break


for i in range(0,4):
    if(l2[0]==l3[i]):
        k=l5[i]
        k1=l8[i]
        break

for j in range(0,2):
    if(l2[1]==l4[j]):
        s=l6[j]
        break
    else:
        s=1

m=''
for i in range (0,len(l7)):
    m=m+l7[i]

mi=int(m)

q=mi*k*s
q1=math.log2(mi)

if(h==3):
    q3=mi*k
    q2=q1+k1
elif(h==2):
    q3=mi*k*2
    q2=q1+k1+1
else:
    q3=mi*k
    q2=q1+k1

print("First type of question is ISA and Instructions related")
print("1. Type A: <Q bit opcode> <P-bit address> <x bit register>")
print("2. Type B: <Q bit opcode> <R bits filler> <x bit register> <x bit register>")

print("Length of one instruction in bits")
lns=int(input())

print("Length of register in bits")
reg=int(input())


while(True):
    if h==1:
        SD=1
        break
    elif h==2:
        SD=4
        break
    elif h==3:
        SD=8
        break
    else:
        SD=1
        break

print("minimum bits are needed to represent an address in this architecture is ")
g=int(q/SD)
print(g)

print("Number of bits needed by opcode: ")
v=lns-g-reg
print(abs(v))

print("Number of filler bits in Instruction type 2")
print(lns-v-(2*reg))

print("Maximum numbers of instructions this ISA can support")
b=int(g/lns)
print(b)

print("Maximum number of registers this ISA can support")
print(2**reg)

print("The second type of question is System enhancement related")
print("TYPE 1")
print("Write how many bits the cpu is")

cb_=int(input())

cb=cb_/8
as_=q3/cb
cc=math.log2(as_)

print("1. Bit Addressable Memory - Cell Size = 1 bit")
print("2. Nibble Addressable Memory - Cell Size = 4 bit")
print("3. Byte Addressable Memory - Cell Size = 8 bits(standard)")
print("4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")

print("How you would want to change the current addressable memory to any of the rest 3 options(1,2,3,4)")
new=int(input())

if(new==4 and h==3):
    if(int(cc-q2)>0):
        print("+"+str(int(cc-q2)))
    else:
        print(int(cc-q2))

elif(new==3 and h==2):
    if(int(cc-q2+1)>0):
        print("+"+str(int(cc-q2+1)))
    else:
        print(int(cc-q2+1))

elif(new==3 and h==4):
    g_=int(math.log2((q3*cb))-q2)

    if (int(math.log2((q3*cb))-q2)):
        print("+"+str(g_))
    else:
        print(g_)
else:
    print(int(cc-q2))

print("TYPE 2")

print("Enter how many bits the cpu is")
ccb_=int(input())
ccb=ccb_/8
fp=math.log2(ccb)

print("Enter how many address pins it has")
ad=int(input())
ad_=ad+fp
print("Enter what type of addressable memory it has(1,2,3,4)\n")
print("1. Bit Addressable Memory - Cell Size = 1 bit")
print("2. Nibble Addressable Memory - Cell Size = 4 bit")
print("3. Byte Addressable Memory - Cell Size = 8 bits(standard)")
print("4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")

am=int(input())

if(am != 4):
    if(ad>10):
        if(ad<20):
            d="KB"
            c=abs(10-ad)
        elif(20<ad<30):
            d='MB'
            c=abs(20-ad)
        elif(30<ad<40):
            d='GB'
            c=abs(30-ad)
        elif(40<ad<50):
            d='TB'
            c=abs(40-ad)
        else:
            d='PB'
            c=abs(50-ad)
    else:
        d='B'
        c=ad

else:
    if(ad_>10):
        if(ad_<20):
            d="KB"
            c=abs(10-ad_)
        elif(20<ad_<30):
            d='MB'
            c=abs(20-ad_)
        elif(30<ad_<40):
            d='GB'
            c=abs(30-ad_)
        elif(40<ad_<50):
            d='TB'
            c=abs(40-ad_)
        else:
            d='PB'
            c=abs(50-ad_)
    else:
        d='B'
        c=ad_

if(am==2):
    print(((str(int((2**c)/2))+' '+d)))
else:
    print((str(int((2**c)))+' '+d))  
