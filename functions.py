from pinyin import pinyin
from gtts import gTTS
import jieba, itertools, openpyxl
from translate import Translator
from hanziconv import HanziConv
import os


# Add Pinyin
def to_pinyin(sentence):
    segments = jieba.cut(sentence)
    output = " ".join(segments)
    pinyined = pinyin.get(output)
    combined = list(itertools.chain.from_iterable(pinyined))
    return ''.join(combined)


def generate_audio_files(sheet):
    # Loop all lines
    row_end = len(sheet)
    row = 0
    while row < row_end:
        hanzi = sheet.loc[row]["Hanzi"]
        do_TTS(hanzi)
        row = row + 1


# Generate Audio for each chinese expression
def do_TTS(hanzi):
    tts = gTTS(text=hanzi, lang='zh-TW')
    # Filename
    filename = hanzi[0:10] + '.mp3'
    # checking if the directory audio exist or not
    if not os.path.exists("audio"):
        # if the demo_folder directory is not present
        # then create it.
        os.makedirs("audio")

    # Save the audio files in the local AND the Anki media.collection folder
    audio_path = 'audio/' + filename
    tts.save(audio_path)
    # Saving the audio in the Anki media.collection folder
    anki_media_collection_path = '/Users/voss/Library/Application Support/Anki2/MAIN/collection.media/' + filename
    tts.save(anki_media_collection_path)


def translation(hanzi="", from_language="zh", to_language="zh"):
    # Adds the translation to the Excel data frame
    translator = Translator(from_lang=from_language, to_lang=to_language)
    simplified_hanzi = HanziConv.toSimplified(hanzi)
    try:
        translated_expression = translator.translate(simplified_hanzi)
    except:
        pass
        return

    return translated_expression


# Add a link to the audio file within an Excel cell
def add_audio_link(audio_link, excel_file, cell, hanzi):
    # Open the Excel file
    wb = openpyxl.load_workbook(excel_file)
    worksheet = wb.active

    filename = hanzi[0:10] + '.mp3'
    worksheet[cell].value = "[sound:" + filename + "]"

    # Save the changes to the Excel file
    wb.save(excel_file)


def add_audio_header_in_excel(sheet, excel_file):
    number_of_audio_column = list(sheet.columns).index("Audio") + 1
    # Open the Excel file
    wb = openpyxl.load_workbook(excel_file)
    worksheet = wb.active
    cell = str(chr(ord('@') + number_of_audio_column)) + "1"
    # Add the hyperlink to the specified cell
    worksheet[cell].value = "Audio"
    # Save the changes to the Excel file
    wb.save(excel_file)


def save_audio(sheet, excel_file):
    for ind, row in sheet.iterrows():
        hanzi = sheet.iloc[ind]["Hanzi"]
        audio_link = "audio/" + hanzi + ".mp3"
        number_of_audio_column = list(sheet.columns).index("Audio") + 1
        cell = chr(ord('@') + number_of_audio_column) + str(ind + 2)
        add_audio_link(audio_link, excel_file, cell, hanzi)
        if ind == len(sheet) - 1:
            add_audio_header_in_excel(sheet, excel_file)