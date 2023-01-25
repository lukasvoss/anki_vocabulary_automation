import numpy as np
import pandas as pd
import pickle


import yaml
from pprint import pprint
# convert yaml document to dict
with open("chinese_vocab_list.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    word = data[0]

dict_final = dict()
#print(word["defs"][:2], word["pinyin"], word["example_sentences"])

#print(type(word["example_sentences"][0]))
example_sentence = word["example_sentences"][0]
example_string = f'{example_sentence["trad"]}\n{example_sentence["pinyin"]}\n{example_sentence["eng"]}'
#print(example_string)

arr_keys = []
arr_values = []
for el in data:
    # keys
    arr_keys.append(el["trad"])

    # values

    if "example_sentences" in el is not None:
        example_sentence = el["example_sentences"][0]
        example_string = f'{example_sentence["trad"]}\n{example_sentence["pinyin"]}\n{example_sentence["eng"]}'

        if len(el["defs"]) >= 2:
            def_string = f'{el["defs"][0]}' + '; ' + f'{el["defs"][1]}'
        else:
            def_string = f'{el["defs"][0]}'

        arr_values.append([el["pinyin"], def_string, example_string])
    else:
        if len(el["defs"]) >= 2:
            def_string = f'{el["defs"][0]}' + '; ' + f'{el["defs"][1]}'
        else:
            def_string = f'{el["defs"][0]}'

        arr_values.append([el["pinyin"], def_string, ""])


dict_final = dict(zip(arr_keys, arr_values))
print(dict_final)


# open the file for writing
with open('chinese_database.pickle', 'wb') as handle:
    # serialize the dictionary using pickle.dump()
    pickle.dump(dict_final, handle)


