import pandas as pd

from main.application.models.responses.target_data import TargetData

df_joined_data = pd.read_pickle('join_data_df.pkl')

print(df_joined_data)

target_data = TargetData(data_frame=df_joined_data)
serialize_data = target_data.serialize()
print(serialize_data)
