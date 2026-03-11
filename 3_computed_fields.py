from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("BMI",patient.bmi)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish','height':'6.5','email':'abc@hdfc.com','age':'30','weight':75.2,'married': True,
                 'allergies':['pollen','dust'],'contact_details':{'phone':'12434343'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)


# @property allows you to access the method like a normal attribute.