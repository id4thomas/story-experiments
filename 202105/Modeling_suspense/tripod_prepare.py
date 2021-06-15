import pandas as pd

# Load TRIPOD synopses oath
file_path='/home/inglab/syr/TRIPOD/Synopses_and_annotations/TRIPOD_synopses_test.csv'
df=pd.read_csv(file_path)
print(df.shape)

diehard=df.iloc[-3]
diehard_segtext=diehard["synopsis_segmented"]
# print(diehard_segtext)
diehard_split=diehard_segtext.split(" [END_SENT] ")
sample=" ".join([sent[11:] for sent in diehard_split])

story_nums=[]
lines=[sample]

stories=[]

for idx in range(3):
    story_nums.append(idx+1)
    story=df.iloc[idx]
    story_split=story["synopsis_segmented"].split(" [END_SENT] ")
    stories.append(" ".join([sent[11:] for sent in story_split]))

with open("/home/inglab/syr/tripod_test.txt",'w') as f:
    f.write("\n".join(stories))