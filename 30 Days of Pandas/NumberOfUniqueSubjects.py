import pandas as pd

def count_unique_subjects(teachers: pd.DataFrame) -> pd.DataFrame:
    unique_subjects = teachers.drop_duplicates(subset=['teacher_id', 'subject_id'])

    subject_counts = unique_subjects.groupby('teacher_id').size().reset_index(name='cnt')

    return subject_counts