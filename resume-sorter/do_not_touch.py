# import aspose.words as aw
from pprint import pprint
from information import info_dict
import dataset
import re

# doc = aw.Document("resume.pdf")
# doc.save("u.txt")
try:
    with open("u.txt", errors="ignore") as file:
        lines_all = file.readlines()
except:
    lines_all = []
    print("error")

text_all = ""
words_all = []
lines_all = [elem for elem in lines_all[2:len(lines_all) - 1:]]
for elem in lines_all:
    words_all.extend(elem.split(" "))
    text_all += elem

words_all = [ele.split(",")[0] for ele in words_all]

info_dict["name"] = lines_all[0]

for ele in lines_all:
    if "CGPA" in ele:
        info_dict["degree_gpa"] = ele.split(" ")[-2]
    for ed in dataset.education:
        if ed in ele or ed.title() in ele:
            info_dict["education"].append(ele)

skill_count = 0

for ele in words_all:
    if ele in dataset.degrees:
        info_dict["education_degree"].append(ele)
    if ele.title() in dataset.skills:
        if ele in info_dict["skills"] or ele.title() in info_dict["skills"]:
            pass
        else:
            info_dict["skills"].append(ele)
            skill_count += 1
    for mail in dataset.emails:
        if mail in ele:
            info_dict["email"] = ele
    phone_numbers = re.findall(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]", ele)
    info_dict["phone"].extend(phone_numbers)

info_dict["skill_count"] = skill_count
print(text_all)
pprint(info_dict)


