class Patient:
    daily_rate = 2500
    count = 0

    def __init__(self, first, last, age, diagnosis):
        self.first = first
        self.last = last
        self.age = int(age)
        self.diagnosis = diagnosis
        Patient.count += 1

    @classmethod
    def from_string(cls, patient_info):
        first, last, age, diagnosis = patient_info.split(",")
        new_patient = cls(first, last, age, diagnosis)
        return new_patient

print(f"As of now, there are {Patient.count} patients.")

patient_1 = Patient("John", "Doe", "25", "Tuberculosis")
patient_2 = Patient("Mary", "Benson", "33", "Pneumonia")
patient_3 = Patient("Glen", "Turner", "43", "Appendicitis")

print(f"As of now, there are {Patient.count} patients.")
print(f"As of now, there are {patient_2.count} patients.")

patient_4 = Patient.from_string("Bill,Baker,70,Kidney stones")
print(f"The new patient is {patient_4.first} {patient_4.last} with diagnosis of {patient_4.diagnosis}")
print(f"As of now, there are {Patient.count} patients.")