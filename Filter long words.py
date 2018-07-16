
# coding: utf-8

# In[1]:


def filter_long_words(inputList,inputInteger):
 
    listOfWords = []
 
    for i in range(len(inputList)):
        if len(inputList[i]) > inputInteger:
            listOfWords.append(inputList[i])
 
    return listOfWords
 
inputListOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']
inputWordLength = 7
 
print (str(filter_long_words(inputListOfWords,inputWordLength)))

