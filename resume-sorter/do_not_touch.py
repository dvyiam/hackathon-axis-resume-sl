# import aspose.words as aw
from pprint import pprint
from information import info_dict
import dataset
import spacy

# doc = aw.Document("resume.pdf")
# doc.save("u.txt")
try:
    with open("u.txt", errors="ignore") as file:
        text = file.readlines()
except:
    text = []
    print("error")


# def perform_ner(resume_text):
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(resume_text)
#     entities = {}
#     for ent in doc.ents:
#         entities[ent.label] = entities.get(ent.label_, []) + [ent.text]
#     return entities


words_all = []
text = [elem for elem in text[2:len(text) - 1:]]
for elem in text:
    words_all.extend(elem.split(" "))

words_all = [ele.split(",")[0] for ele in words_all]

info_dict["name"] = text[0]

for ele in text:
    if "CGPA" in ele:
        info_dict["degree_gpa"] = ele.split(" ")[-2]
    for ed in dataset.education:
        if ed in ele or ed.title() in ele:
            info_dict["education"].append(ele)

    # resume_entities = perform_ner(ele)
    # print(resume_entities)

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

info_dict["skill_count"] = skill_count

pprint(info_dict)


