import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(patients, columns=['patient_id', 'patient_name', 'conditions'])
    result = patients[patients['conditions'].apply(lambda x: any(cond.startswith('DIAB1') for cond in x.split()))]
    return result