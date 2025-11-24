# dictionary & set 
info={
    "key":"value",
    "name" : "apnacollege",
    "learning":"coding",
   "age": 35,
   12.99  :  94.4,
    "subject":["math","physics","chemistry"]



}
print(type(info))
print(info)
print(info["name"])
print(info["learning"])
info["name"]="aftab"
info["surname"]="yadav"
print(info)

student={
"name":" mohd aftab",
"subject":{
    "phy":97,
    "chem":98,
    "math":95

}
}
print(student["subject"]["chem"])

print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
print(list(student.values()))

pairs=list(student.items())
print(pairs[0])
print(student["name"])
print(student.get("name"))
student.update({"city":"delhi","age":18,"name":"saba "})
print(student)

#sets
collection={1,2,3,4,"hello","world",2,4}
print(collection)
print(type(collection))
print(len(collection))

collection =set()
print(type(collection))
print(collection)
collection.add(1)
collection.add(2)
collection.add("apnacollege")
collection.add("aftab")
collection.add(3)
collection.remove(1)
collection.clear()
print(len(collection))
print(collection)
collection={"hello","apnacollege","world","coding","pythjon"}
print(collection.pop())
print(collection.pop())

set1={1,3,2}
set2={2,4,3}
print(set1.union(set2)) 
print(set1)
print(set2)
print(set1.intersection(set2))
#practice



men_dic={
    "table":["a piece of ferniture","list of facts & figures"],
     "cat":"a small animal"
} 
print(men_dic)

sub= { 
    "python","java","python","javascript","c++","c","java"
}
print(len(sub))
print(sub)

dic={}
x=input("enter phy: ")
dic.update({"phy":x})

x=input("enter chem: ")
dic.update({"chem":x})


x=input("enter math: ")
dic.update({"math":x})

print(dic)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
list1 = [a,b,c,d,e]
list2=set(list1)

list3 = sorted(list2)
list2=list(list3)
total= sum(list2)
print(list2)
print("max: ",max(list2))
print("min: ",min(list2))
print("total: ",total)


