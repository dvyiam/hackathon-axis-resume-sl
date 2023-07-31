import spacy


def extract_resume_info(resume_text):
    # Load spaCy's English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the resume text
    doc = nlp(resume_text)

    # Initialize variables to store extracted information
    contact_info = {}
    education = []
    skills = []
    work_experience = []

    # Extract contact information
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            contact_info["Name"] = ent.text
        elif ent.label_ == "PHONE":
            contact_info["Phone"] = ent.text
        elif ent.label_ == "EMAIL":
            contact_info["Email"] = ent.text
        elif ent.label_ == "ADDRESS":
            contact_info["Address"] = ent.text

    # Extract education details
    for ent in doc.ents:
        if ent.label_ == "EDUCATION":
            education.append(ent.text)

    # Extract skills
    skills_keywords = ["skills", "competencies"]
    for sent in doc.sents:
        for keyword in skills_keywords:
            if keyword in sent.text.lower():
                skills.extend([ent.text for ent in sent.ents if ent.label_ == "SKILL"])

    # Extract work experience
    experience_keywords = ["work experience", "employment history"]
    for sent in doc.sents:
        for keyword in experience_keywords:
            if keyword in sent.text.lower():
                work_experience.extend([ent.text for ent in sent.ents if ent.label_ == "ORG"])

    # Return the extracted information
    return {
        "Contact Info": contact_info,
        "Education": education,
        "Skills": skills,
        "Work Experience": work_experience
    }

# Sample resume text
resume_text = """
John Doe
Email: johndoe@email.com
Phone: (123) 456-7890
Address: 123 Main Street, City, State, Zip

Objective:
Highly motivated Software Engineer with expertise in Python and Java.

Work Experience:
Software Engineer
ABC Tech Solutions
January 2018 - Present
Location: New York
- Developed and maintained web applications using Django and Flask.
- Collaborated with cross-functional teams to deliver quality software.

Education:
Bachelor of Science in Computer Science
XYZ University
May 2017

Skills:
Python, Java, Django, Flask, SQL, Git

Certifications:
AWS Certified Developer - Associate
Issued: April 2021
"""

# Extract information from the resume
extracted_info = extract_resume_info(resume_text)
print(extracted_info)
