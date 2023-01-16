# Anki Chinese Vocabulary Flashcard Creation Automation Tool

## A tool written in Python3 enabling Chinese learners to speed up their Anki flashcard creation

### Introduction

This code is meant to optimize the way Chinese learners can create their flashcards in Anki. Anki is a digital flashcard application that is based on the "spaced-repitition" for human memory. 
This Python tool makes use of Anki allowing for the import of csv files and directly creates corresponding flashcards out of it.

### How the tool works

* **Input**: An Excel file (hanzi_list.xlsx) that has one column with the header "Hanzi". This column then contains the Chinese characters (simplified or traditional) you want to create your flashcards for.
* **Output**: An Excel file (vocabulary.xlsx) that has the characters' pinyin, english translation and a "link" to an audio file of the characters' pronounciation.

### What the code does

The pinyin and the English translation get added to the dataframe as generated from the input Excel file. Furthermore, an audio recording of the characters gets saved in the folder "media.collection" (might be a different name for Windows or Linux, see [here](https://docs.ankiweb.net/files.html) for more details).
In order to have Anki refer to the correct audio file, we generate a column with "links" to those files using the required format: sound:<audio_file_name>.mp3 put in square brackets.

### How to use this tool

* Clone this repository
* Specify the path to you Anki "media.collection" directory within the "do_TTS" function in the functions.py file
* Make sure to install all the required packages to your Python interpreter
* Create an Excel file "hanzi_list.xlsx" with the characters that you want to create Anki flashcards for
* Remove the first line (so the headers) in the output Excel file "vocabulary.xlsx" file and convert it to a UTF-8 encoded csv file. This step is not part of the code since this way you can make manual adjustments to some cells (if wished so).
* Import the csv file to an existing Anki deck of yours. Ensure that the order of the fields on your flashcard correspond to the order of the csv file that shall be imported. A guide on the csv import process to do so can be found [here](https://www.youtube.com/watch?v=BwGNP3GXmxg) starting from 4:33.

### Found a bug?
If you found an issue or would like to submit and idea for improving this tool, please feel free to do so and submit an issue using the issue tab above. If you would like to submit a PR with a fix, please reference the issue that you created.

### Known issues
The translation from Chinese to English is sometimes poor. Feel free to reach out in case you know how to improve the translation quality!
