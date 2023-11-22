thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict)
x=thisdict["model"]
print(x)
y=thisdict.keys()
print(y)
thisdict["color"]="black"
print(y)
z=thisdict.values()
print(z)

dic={
    1:"anu",
    2:"prar",
    3:"man",
    4:"jij"
}
acc=sorted(dic.keys())
dec=sorted(dic.keys(),reverse=True)
print("accending oder od dictionary",acc)
print("descending order of dictionary",dec)

acc_v=sorted(dic.values())
dec_v=sorted(dic.values(),reverse=True)
print("accending oder od dictionary",acc_v)
print("descending order of dictionary",dec_v)