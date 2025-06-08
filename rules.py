def diagnose_symptoms(symptoms):
    rules = [
        ({"fever", "cough", "fatigue", "body_ache"}, "Flu"),
        ({"headache", "nausea", "sensitivity_to_light"}, "Migraine"),
        ({"chest_pain", "shortness_of_breath", "sweating"}, "Heart Attack"),
        ({"runny_nose", "sore_throat", "sneezing"}, "Common Cold"),
        ({"abdominal_pain", "vomiting", "diarrhea"}, "Food Poisoning"),
        ({"thirst", "frequent_urination", "weight_loss"}, "Diabetes"),
        ({"joint_pain", "morning_stiffness", "swollen_joints"}, "Rheumatoid Arthritis"),
        ({"yellow_skin", "fatigue", "dark_urine"}, "Hepatitis"),
        ({"high_fever", "rash", "muscle_pain", "bleeding"}, "Dengue"),
        ({"neck_pain", "fever", "confusion"}, "Meningitis"),
        ({"dry_cough", "fever", "loss_of_taste"}, "COVID-19"),
        ({"itchy_eyes", "sneezing", "runny_nose"}, "Allergic Rhinitis"),
    ]
    for rule_symptoms, diagnosis in rules:
        if rule_symptoms.issubset(symptoms):
            return diagnosis
    return "No clear diagnosis found. Please consult a doctor."
