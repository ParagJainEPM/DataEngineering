import pandas as pd
import json

df = pd.read_csv('fakeData.csv')
df100 = pd.read_csv('fakeData.csv',nrows=100)

df.head(10)
df100.to_json("conv.json",indent=2)

# json normalized

with open("data.json",'r') as f:
    data = json.load(f)

print(type(data))
dfj = pd.json_normalize(data["records"])
print(dfj.head(3))

dfj.head(10).to_json("conv1.json", indent=2)
dfj.head(10).to_csv("conv1.csv")
dfj.head(10).to_pickle("conv1.pickle")

dfj.head(10).to_json("./out/conv_records.json", orient='records', indent=2)
dfj.head(10).to_json("./out/conv_split.json", orient='split', indent=2)
dfj.head(10).to_json("./out/conv_index.json", orient='index', indent=2)
dfj.head(10).to_json("./out/conv_columns.json", orient='columns', indent=2)
dfj.head(10).to_json("./out/conv_values.json", orient='values', indent=2)
dfj.head(10).to_json("./out/conv_table.json", orient='table', indent=2)

# example of normalizing an index type dict into column format
with open("./out/conv_records.json",'r') as f:
    data2 = json.load(f)
dfnorm = pd.json_normalize(data2)
print(dfnorm.head(5))