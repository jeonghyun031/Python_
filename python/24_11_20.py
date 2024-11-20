import pandas as pd
data = { '이름' : ['김','정','박','이'], '나이' : [23,2,25,30], '성적' : [98.3,89.7,85.2,79.5]}
df = pd.DataFrame(data)
print(df)
df.mean(numeric_only=True)
df.나이.mean()