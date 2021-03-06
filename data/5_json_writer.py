import json

reg = {
    "users": [
        {"Name": "Lolita Lynn", "index": 0, "gender": "female", "company": "HIVEDOM", "book":"Fundamentals of Wavelets" },
        {"Name": "Tonia Hurst", "index": 1, "gender": "female", "company": "VIOCULAR", "book":"Data Smart" },
        {"Name": "Brooks Bright", "index": 2, "gender": "male", "company": "DIGITALUS", "book":"God Created the Integers" },
        {"Name": "Kathrine Sharp", "index": 3, "gender": "female", "company": "QUIZMO", "book":"Superfreakonomics" },
        {"Name": "Shawn Harrell", "index": 4, "gender": "female", "company": "DECRATEX", "book":"Orientalism" },
        {"Name": "Amy Casey", "index": 5, "gender": "female", "company": "JAMNATION", "book":"Nature of Statistical Learning Theory" },
        {"Name": "Lorena Mejia", "index": 6, "gender": "female", "company": "PLASMOX", "book":"Integration of the Indian States" },
        {"Name": "Allyson Wilkins", "index": 7, "gender": "female", "company": "COMTOURS", "book":"Drunkard's Walk, The" },
        {"Name": "Mays Reed", "index": 8, "gender": "male", "company": "COMTENT", "book":"Image Processing & Mathematical Morphology" },
        {"Name": "Katherine Mayer", "index": 9, "gender": "female", "company": "EXTRAGEN", "book":"How to Think Like Sherlock Holmes" },
        {"Name": "Kelly Byers", "index": 10, "gender": "female", "company": "ENAUT", "book":"Data Scientists at Work" },
        {"Name": "Kelly Byers", "index": 11, "gender": "male", "company": "GEOSTELE", "book":"Slaughterhouse Five" },
        {"Name": "Kay Beasley", "index": 12, "gender": "female", "company": "ECOLIGHT", "book":"Birth of a Theorem" },
        {"Name": "Robbins Gordon", "index": 13, "gender": "male", "company": "EXTREMO", "book":"Structure & Interpretation of Computer Programs" },
        {"Name": "Hillary Bauer", "index": 14, "gender": "female", "company": "SENMAO", "book":"Age of Wrath, The" },
        {"Name": "Ruiz Phelps", "index": 15, "gender": "male", "company": "DOGNOSIS", "book":"Trial, The" },
        {"Name": "Carolina Bryant", "index": 16, "gender": "female", "company": "SENTIA", "book":"Statistical Decision Theory'" },
        {"Name": "Sosa Lee", "index": 17, "gender": "female", "company": "NORSUL", "book":"Data Mining Handbook" },
        {"Name": "Lorna Scott", "index": 18, "gender": "female", "company": "QNEKT", "book":"New Machiavelli, The" },
        {"Name": "Bernard Holden", "index": 19, "gender": "male", "company": "ESCHOIR", "book":"Physics & Philosophy" },
        {"Name": "Craft Shields", "index": 20, "gender": "female", "company": "INSURON", "book":"Making Software" },
        {"Name": "Mara English", "index": 21, "gender": "female", "company": "CYCLONICA", "book":"Analysis, Vol I" },
        {"Name": "Fisher Levy", "index": 22, "gender": "female", "company": "XLEEN", "book":"Machine Learning for Hackers" },
        {"Name": "Cecelia Snyder", "index": 23, "gender": "female", "company": "LETPRO", "book":"Signal and the Noise, The" }
    ]
}
with open("example.json", "w") as file_json_write:
    s = json.dumps(reg, indent=4)
    file_json_write.write(s)



