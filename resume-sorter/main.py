# import aspose.words as aw
from pprint import pprint
# doc = aw.Document("resume.pdf")
# doc.save("u.txt")
try:
    with open("u.txt", errors="ignore") as file:
        text = file.readlines()
except:
    text = []
    print("error")

text_all = []
text = [elem for elem in text[2:len(text) - 1:]]
for elem in text:
    text_all.extend(elem.split(" "))

degrees = ["B.Tech", "btech", "B.TECH", "BTECH", "b.tech", "M.Tech", "mtech", "M.TECH", "MTECH", "m.tech"]
skills = ["html","javascript", "css", "js","react.js","angular.js","express.js", "c","c++","c#","node.js","mongoDB","firebase","tailwind css","flask","django", "selenium"]
emails = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com","@icloud.com"]




info_dict = {
    "name": text[0],
    "education_degree": [],
    "degree_gpa": 0.0,
    "experience": [],
    "email": "",
    "skills": 0,
    "phone": "",
}

for ele in text:
    if "CGPA" in ele:
        info_dict["degree_gpa"] = ele.split(" ")[-2]

for ele in text_all:
    if ele in degrees:
        info_dict["education_degree"].append(ele)

pprint(info_dict)
