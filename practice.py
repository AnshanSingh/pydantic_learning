from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # for metadata
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient less then 50 chars', examples=['nitish','Amit'])]
    # name: str = Field(max_length=50)
    email: EmailStr
    # linkdin_url: AnyUrl
    age: int
    weight: float = Field(gt=0)
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info = {'name': 'Arpit', 'age': 21,'email':'abc@gmail.com', 'weight': 63.5, 'married':True, 'allergies':
                ['pollen','dust'],'contact_details':{'email':'abc@gmail.com', 'phone':'1234567898'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

# update_patient_data(patient1)