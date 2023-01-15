import numpy as np
import pandas as pd
from functions import to_pinyin, translation, save_audio, generate_audio_files


if __name__ == '__main__':
    # Read Excel file with the Hanzi (traditional) and create a dataframe out of it
    # This Excel file is solely used as a pure INPUT source for the Hanzi
    df = pd.read_excel(r"hanzi_list.xlsx")

    # Add pinyin
    df['Pinyin'] = df['Hanzi'].apply(to_pinyin)
    # Creates a new Excel file which now will be work in

    excel_output_name = 'vocabulary' + '.xlsx'
    df.to_excel(excel_output_name, index=False)

    # Import the Excel file
    sheet = pd.read_excel(excel_output_name)

    # Translate to English
    sheet["English"] = np.NAN
    translation_list = list(sheet["English"])
    translation_list = [translation(hanzi, "zh", "english") for hanzi in sheet["Hanzi"]]
    sheet["English"] = translation_list

    sheet.to_excel(excel_output_name, index=False)

    # Generates audio files for the hanzi and saves them in a local "audio" folder and in the media.collection folder Anki looks up the media references
    sheet["Audio"] = np.NAN
    generate_audio_files(sheet)

    save_audio(sheet, excel_output_name)