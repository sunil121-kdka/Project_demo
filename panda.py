import pandas as pd

students_data={
    'studentID':[101,102,103,104],
    'name':['hari','bob','ram','sita'],
    'age':[20,19,21,18],
    'Grade':['A','B','A+','B+']
}

student_df=pd.DataFrame(students_data)
print(student_df)