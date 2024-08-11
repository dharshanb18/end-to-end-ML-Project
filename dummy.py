from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data = pd.DataFrame({
    "gender": ["female"],
    "race_ethnicity": ["group B"],
    "parental_level_of_education": ["bachelor's degree"],
    "lunch": ["standard"],
    "test_preparation_course": ["none"],
    "reading_score": [72],
    "writing_score": [74]
})

encoder = OneHotEncoder(handle_unknown='ignore')
try:
    transformed = encoder.fit_transform(data[['gender', 'race_ethnicity']])
    print(transformed)
except AttributeError as e:
    print(e)
