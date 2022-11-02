import pandas as pd

file = open('kkk.txt','r')
d = {"name":[],"address":[],'contact':[],"Date":[],"Policy.no":[],"Premium":[],"Good & service tax":[],"Add(Previous shortage)":[],"Less (Excess amount)":[],"Amount Payable":[],"Premium paying term":[],"Policy term":[],"Maturity Date":[],"Policy lapse":[],"Bonus / Guaranteed Additions":[],"Premium due fall":[]}
read = file.readlines()

for doc in range(0,1):
    lk = read[doc]

d['name'].append(lk)

list1 = [read[row] for row in range(1,6)]
# print(lj)
ff = ''.join(list1)
# print(ff)

d['address'].append(ff)
# okkk = " kk"
list3 = []
# print(read)
cont_a = False
for row in read:
    if "additions" in row.lower():
        # d['Bonus / Guaranteed Additions'].append(n.split(":")[1])
        d['Bonus / Guaranteed Additions'].append(row.split(":")[1])
        cont_a = True
if not cont_a:
    d["Bonus / Guaranteed Additions"].append("Null")


for row1 in read:
    # print(i.strip())
    if "contact no" in row1.lower():
        n = row1.split(":")[1]
        n1 = slice(11)
        d['contact'].append(n[n1])
        # n = i.split(':')[1]
        # print(n)
        # d['contact'].append(n.replace(',','\n'))

    elif "date :" in row1.lower():
        list3.append(row1)
    elif "premium paying term :" in row1.lower():
        d["Premium paying term"].append(row1.split(":")[1])
    elif "policy term" in row1.lower():
        d["Policy term"].append(row1.split(":")[1])
    elif "fall" in row1.lower():
        d["Premium due fall"].append(row1.split(" ")[5])
    elif "ltd" in row1.lower():
        d["Policy.no"].append(row1.split(" ")[3])
    elif "lapse" in row1.lower():
        d["Policy lapse"].append(row1.split(" ")[12])
# print(read)
# for index in range(103,112):
#     print(read[index])
list2 = [] 
for row2 in range(read.index("Payable\n") + 2 , read.index('We assure you of our best services and look forward to a long association with you.\n') - 1 ):
    list2.append(read[row2])

d["Premium"].append(list2[0])
d["Good & service tax"].append(list2[2])
d["Add(Previous shortage)"].append(list2[4])
d["Less (Excess amount)"].append(list2[6])
d["Amount Payable"].append(list2[8])


d["Date"].append(list3[0].split(":")[1])
d["Maturity Date"].append(list3[1].split(":")[1])

df = pd.DataFrame.from_dict(d)
df.to_csv("omk.csv")
pd.read_csv('omk.csv')
df