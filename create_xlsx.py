import pandas as pd
import pickle
from functions import to_pinyin, translation

# open the file for reading
with open('chinese_database.pickle', 'rb') as handle:
    # deserialize the dictionary using pickle.load()
    db = pickle.load(handle)



df = pd.read_excel(r"hanzi_list.xlsx")
list_hanzi = df["Hanzi"]

headers = ["Hanzi", "Pinyin", "English", "Example"]
final_df = pd.DataFrame(columns=headers)
#final_df["Hanzi"] = list_hanzi

for ind in range(len(list_hanzi)):
    hanzi = list_hanzi[ind]
    if hanzi in db is not None:
        final_df.loc[ind, "Hanzi"] = hanzi
        final_df.loc[ind, "Pinyin"] = db[hanzi][0]
        final_df.loc[ind, "English"] = db[hanzi][1]
        final_df.loc[ind, "Example"] = db[hanzi][2]

    else:
        final_df.loc[ind, "Hanzi"] = hanzi
        final_df.loc[ind, "Pinyin"] = to_pinyin([hanzi][0])
        final_df.loc[ind, "English"] = translation(hanzi, from_language="zh", to_language="en")
        final_df.loc[ind, "Example"] = ""

        print(ind+1, hanzi)


final_df.to_excel("output_to_anki.xlsx", index=None)
final_df = final_df[1:]
final_df.to_csv("output_to_anki.csv", index=None, header=False)