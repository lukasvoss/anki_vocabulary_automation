# Anki Chinese Vocabulary Flashcard Creation Automation Tool

## A tool written in Python3 enabling Chinese learners to speed up their Anki flashcard creation

### Introduction

This code is meant to optimize the way Chinese learners can create their flashcards in Anki. Anki is a digital flashcard application that is based on the "spaced-repitition" for human memory. 
This Python tool makes use of Anki allowing for the import of csv files and directly creates corresponding flashcards out of it.

### How the tool works

* **Input**: An Excel file (hanzi_list.xlsx) that has one column with the header "Hanzi". This column then contains the Chinese characters (simplified or traditional) you want to create your flashcards for.
* **Output**: An Excel file (chinese_vocabulary.xlsx) that has the characters, its phonetics (pinyin), english translation and an in some cases also an example sentence: <br>  

### What the code does
According to each Chinese character (Hanzi) its pinyin and the English translation get added to the dataframe as generated from the input Excel file. This will then exported to a csv which can be directly imported by Anki.


### How to use this tool

* Clone this repository / Copy all the code
* Make sure to install all the required packages to your Python interpreter
* Create an Excel file "hanzi_list.xlsx" that has one column called "Hanzi" and Chinese characters in its rows
* Run the script
* Import the csv file to an existing Anki deck of yours. Ensure that the order of the fields on your flashcard correspond to the order of the csv file that shall be imported. A guide on the csv import process to do so can be found [here](https://www.youtube.com/watch?v=BwGNP3GXmxg) starting from 4:33.


### Found a bug?
If you found an issue or would like to submit and idea for improving this tool, please feel free to do so and submit an issue using the issue tab above. If you would like to submit a PR with a fix, please reference the issue that you created.

### Known issues
For **option 1**, the translation from Chinese to English is sometimes poor. That's why I added the **Option 2**. Feel free to reach out in case you know how to improve the translation quality consistently!
