welcome_prompt = "Welcome doctor, what would you like to do today?\n \
                 - To list all patients, press 1\n \
                 - To run a new diagnosis, press2\n \
                 - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n \
                 - 1: Normal appearance\n \
                 - 2: Irritable or lethargic\n"
eye_prompt = "How are the patient's eyes?\n \
                 - 1: Normal or slightly sunken eyes\n \
                 - 2: Severely sunken\n"
skin_prompt = "How are is patient's skin when you pinch it?\n \
                 - 1: Normal skin pinch\n \
                 - 2: Slow skin pinch\n"

no_dehydration = "No dehydration"
some_dehydration = "Some dehydration"
severe_dehydration = "Severe dehydration"

error_message = "Input error occured"

patients_and_diagnosis = [
    "Mike: Severe dehydration",
    "Sally: No dehydration",
    "Kate: Some dehydration"
]

def list_patients():
    print(patients_and_diagnosis)

def start_new_diagnosis():
    name = input(name_prompt)  
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)

def assess_appearance():
    appearance = input(appearance_prompt)

    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_eyes(skin)
    
def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    else:
        return ""
    
def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        return ""

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    
    final_diagnosis = name + ": " + diagnosis
    patients_and_diagnosis.append(final_diagnosis)
    print("The final diagnosis: " + diagnosis)


def main():
    while(True):
        selection = input(welcome_prompt)
        
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection =="q":
            print("you quit")
            return
        else:
            print("unknown command")


main()