# Anki Chinese Vocabulary Flashcard Creation Automation Tool

## A tool written in Python3 enabling Chinese learners to speed up their Anki flashcard creation
## This tool comes with two different options of operation: 1 and 2

### Introduction

This code is meant to optimize the way Chinese learners can create their flashcards in Anki. Anki is a digital flashcard application that is based on the "spaced-repitition" for human memory. 
This Python tool makes use of Anki allowing for the import of csv files and directly creates corresponding flashcards out of it.

### How the tool works

* **Input**: An Excel file (hanzi_list.xlsx) that has one column with the header "Hanzi". This column then contains the Chinese characters (simplified or traditional) you want to create your flashcards for.
* **Output**: An Excel file (vocabulary.xlsx) that has the characters, its phonetics (pinyin), english translation and: <br>

Either
1. A reference to an audio file of the characters' pronounciation saved in Anki's media.collection folder on your computer
  **OR**
2. An example sentence/expression where the character is being used. Said example has then the Chinese, its pinyin and the English translation

For Option 1: Run the "main.py" file
For Option 2: Run the "create_xlsx.py" file
**Both** will need elements of the "functions.py" file.


  

### What the code does
**Option 1** <br>
The pinyin and the English translation get added to the dataframe as generated from the input Excel file. Furthermore, an audio recording of the characters gets saved in the folder "media.collection" (might be a different name for Windows or Linux, see [here](https://docs.ankiweb.net/files.html) for more details).
In order to have Anki refer to the correct audio file, we generate a column with "links" to those files using the required format: sound:<audio_file_name>.mp3 put in square brackets.

**Option 2** <br>
Reads the input Excel-file "hanzi_list.xlsx" and a pickle database "chinese_database.pickle" which serves as a sort of Chinese-English dictionary for the characters the user wants to study here. It adds the phonetics (pinyin), the English translation next to the Chinese characters and exports it as the csv-file "output_to_anki.csv". Up to this step there is no audio. One could use the functions "do_TTS", "generate_audio_files" and "add_audio_link" from the "functions.py" file, but the idea here is a different one.


### How to use this tool

* Clone this repository
* Make sure to install all the required packages to your Python interpreter
* Create an Excel file "hanzi_list.xlsx" that has one column called "Hanzi" and Chinese characters in its rows

**Option 1**
* Specify the path to you Anki "media.collection" directory within the "do_TTS" function in the functions.py file
* Create an Excel file "hanzi_list.xlsx" with the characters that you want to create Anki flashcards for
* Remove the first line (so the headers) in the output Excel file "vocabulary.xlsx" file and convert it to a UTF-8 encoded csv file. This step is not part of the code since this way you can make manual adjustments to some cells (if wished so).
* Import the csv file to an existing Anki deck of yours. Ensure that the order of the fields on your flashcard correspond to the order of the csv file that shall be imported. A guide on the csv import process to do so can be found [here](https://www.youtube.com/watch?v=BwGNP3GXmxg) starting from 4:33.

**Option 2**
* Run the file "create_xslx.py"
* Import the csv file to an existing Anki deck of yours. Ensure that the order of the fields on your flashcard correspond to the order of the csv file that shall be imported. A guide on the csv import process to do so can be found [here](https://www.youtube.com/watch?v=BwGNP3GXmxg) starting from 4:33.
* The audio generation will happen directly in Anki using the [Forvo-addin](https://ankiweb.net/shared/info/858591644). This can then be semi-automized with the file "forvo_adder.py" that imitates the user's mouse and keyboard inputs.
* Adjust the file "forvo_adder.py" in the relevant lines that govern where to click. At best, use a full screen mode of anki to avoid issues with open windows of other running applications on your machine.


### Found a bug?
If you found an issue or would like to submit and idea for improving this tool, please feel free to do so and submit an issue using the issue tab above. If you would like to submit a PR with a fix, please reference the issue that you created.

### Known issues
For **option 1**, the translation from Chinese to English is sometimes poor. That's why I added the **Option 2**. Feel free to reach out in case you know how to improve the translation quality consistently!
