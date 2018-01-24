import pandas as pd
import csv
from textblob import TextBlob

biblesCsv = pd.read_csv('/Users/manavdutta1/Downloads/NewBible/bibles.csv', encoding = "ISO-8859-1")
newDataFrame = pd.DataFrame(index=[i for i in range(len(biblesCsv))],columns=['Verse', 'Text', 'Subjectivity', 'Polarity'])
for index, row in biblesCsv.iterrows():
    rowName = row['Verse']
    text = row['English Revised Version']
    if (type(text) is str):
        newDataFrame = newDataFrame.set_value(index, 'Verse', rowName)
        newDataFrame =  newDataFrame.set_value(index, 'Text', text)
        newTextBlob = TextBlob(text)
        newDataFrame = newDataFrame.set_value(index, 'Subjectivity',newTextBlob.sentiment.subjectivity)
        newDataFrame = newDataFrame.set_value(index, 'Polarity', newTextBlob.sentiment.polarity)

newDataFrame.to_csv('/Users/manavdutta1/Downloads/NewBible/BibleSentiment.csv')   
rowName = "Revelation"
averageSentiment = 0.0
averagePolarity = 0.0
length = 0.0
for index, row in newDataFrame.iterrows():
    theName = row['Verse']
    nameArray = theName.split(' ')
    if (nameArray[0] == rowName):
        averageSentiment += row['Subjectivity']
        averagePolarity += row['Polarity']
        length += 1.0
    else:
        break     

print(averagePolarity/length) 
print(averageSentiment/length)        

