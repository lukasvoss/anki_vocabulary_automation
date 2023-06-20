import pandas as pd
from pinyin import pinyin
import pickle
from googletrans import Translator
import jieba
import itertools
from hanziconv import HanziConv


# Reads in a pickle file that serves as a database (db) for Chinese characters. 
# This db covers already many characters, has Pinyin and also an example sentence
with open('chinese_database.pickle', 'rb') as handle:
    # deserialize the dictionary
    db = pickle.load(handle)

def create_anki_csv(input_file, output_file):
    # Read in the input Excel-sheet. It expects a file with one column named 'Hanzi' that has
    # Chinese characters, so called 'Hanzi'. These is the vocabulary you want to learn
    df = pd.read_excel(input_file)
    
    # Apply the functions to the hanzi to add the phonetics (here it's pinyin), the English translation
    # and if available an example sentence
    df['Pinyin'] = df['Hanzi'].apply(convert_to_pinyin)
    df['English'] = df['Hanzi'].apply(get_translation)
    df['Example'] = df['Hanzi'].apply(get_example)
    
    # Export the final table to a csv file. This is the format that the App 'Anki' uses for importing Flashcards
    df.to_csv(output_file, index=False, encoding='utf-8-sig')


def convert_to_pinyin(hanzi):
    """
    Function that generates the phonetics of Chinese characters (hanzi) in form of Pinyin
    :param hanzi: Chinese characters that we want the get the phonetics for
    :return: The pinyin for the input hanzi 
    """

    if hanzi in db:
        return db[hanzi][0]
    else:
        segments = jieba.cut([hanzi][0])
        output = ' '.join(segments)
        pinyined = pinyin.get(output)
        combined = list(itertools.chain.from_iterable(pinyined))
        return ''.join(combined)
        

def get_translation(hanzi):
    """
    Function that translates the Chinese characters (hanzi) to its English meaning
    :param hanzi: Chinese characters that we want the get the translation for
    :return: The English translation for the input hanzi 
    """

    if hanzi in db:
        return db[hanzi][1]

    else:
        translator = Translator('zh', 'en')

        simplified_hanzi = HanziConv.toSimplified(hanzi)
        try:
            translated_expression = translator.translate(simplified_hanzi)
            return translated_expression
        except:
            pass
            return
        

def get_example(hanzi):
    """
    Function that retrieves the example sentence from the db, if the hanzi is available in the db
    :param hanzi: Chinese characters that we want the get the example for
    :return: The example sentence for the input hanzi. If the hanzi is not in the db, then we return an empty string
    """
    if hanzi in db:
        return db[hanzi][2]
    else:
        return ''


if __name__ == "__main__":
    # Execute the script
    input_file = 'hanzi_list.xlsx'
    output_file = 'chinese_vocabulary.csv'

    create_anki_csv(input_file, output_file)