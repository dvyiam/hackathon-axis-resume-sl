# import aspose.words as aw
from pprint import pprint
from information import info_dict
import dataset
# doc = aw.Document("resume.pdf")
# doc.save("u.txt")
try:
    with open("Output.txt", errors="ignore") as file:
        text = file.readlines()
except:
    text = []
    print("error")

words_all = []
text = [elem for elem in text[2:len(text) - 1:]]
for elem in text:
    words_all.extend(elem.split(" "))

words_all = [ele.split(",")[0] for ele in words_all]

info_dict["name"] = text[0]

for ele in text:
    if "CGPA" in ele:
        info_dict["degree_gpa"] = ele.split(" ")[-2]

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

info_dict["skill_count"] = skill_count

pprint(info_dict)
