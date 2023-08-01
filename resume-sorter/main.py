import aspose.words as aw
from pprint import pprint

doc = aw.Document("./resume.pdf")
doc.save("u.txt")
try:
    with open("u.txt", errors="ignore") as file:
        text = file.readlines()
except:
    text = []
    print("error")

words_all = []
text = [elem for elem in text[2:len(text) - 1:]]
for elem in text:
    words_all.extend(elem.split(" "))

words_all = [ele.split(",")[0] for ele in words_all] #this

degrees = ["B.Tech", "btech", "B.TECH", "BTECH", "b.tech", "M.Tech", "mtech", "M.TECH", "MTECH", "m.tech"]
skills = ["html", "javascript", "css", "js", "react.js", "angular.js", "express.js", "c", "c++", "c#", "c-sharp", "node.js",
          "mongoDB", "firebase", "tailwind css", "flask", "django", "selenium", "java", "python"]
skills = [ele.title() for ele in skills]
emails = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@icloud.com"]

info_dict = {
    "name": text[0],
    "education_degree": [],
    "degree_gpa": 0.0,
    "experience": [],
    "email": "",
    "skills": [],
    "skill_count": 0,
    "phone": "",
}

for ele in text:
    if "CGPA" in ele:
        info_dict["degree_gpa"] = ele.split(" ")[-2]

skill_count = 0

for ele in words_all:
    if ele in degrees:
        info_dict["education_degree"].append(ele)
    if ele.title() in skills:
        if ele in info_dict["skills"] or ele.title() in info_dict["skills"]:
            pass
        else:
            info_dict["skills"].append(ele)
            skill_count += 1

info_dict["skill_count"] = skill_count

pprint(info_dict)
