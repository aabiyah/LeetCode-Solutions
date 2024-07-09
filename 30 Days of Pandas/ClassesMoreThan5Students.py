import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses.groupby('class').size().reset_index(name='student_count')

    classes_with_five_students = class_counts[class_counts['student_count'] >= 5]

    result = classes_with_five_students[['class']]

    return result