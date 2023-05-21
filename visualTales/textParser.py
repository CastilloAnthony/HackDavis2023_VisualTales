def parseStopWords(stopWordsFile, inputString): # Returns an array of all the words excluding the stop words
  punctuations = ['.', '!', '?', ',', ';', ':', '', ' ']
  if not (isinstance(inputString, str)): # If the input is not a string then return False
    return False
  
  stopWords, outputWords, tempWord, count = [], [], '', 0
  with open(stopWordsFile, 'r') as file: # Reading stop words from a file
    for line in file:
      for c in line:
        if c == '\n':
          break
        tempWord += c
      stopWords.append(tempWord) # Appending all stopwords to a list
      tempWord = ''

  count = 0
  while (count <= (len(inputString)-1)): # Iterate through the input string and remove stop words
    if (count == len(inputString)-1): # If we are at the very last character
      if inputString[count] not in punctuations:#!= '.':
        tempWord += inputString[count]
      outputWords.append(tempWord)
      break      
    if (inputString[count] in punctuations):#== ' ') or (inputString[count] == '.'): # Checks if inputString[count] is an empty space
      if (tempWord.lower() in stopWords) or (tempWord.lower() in punctuations):# or (tempWord == '') or (tempWord == ' ') or (tempWord == '.'): # Don't add stopwords or empty strings to the output
        tempWord = ''
      else: # Everythng else can be added back into the output
        outputWords.append(tempWord) # Appending all non-stop words to a list
        tempWord = ''
    else:
      tempWord += inputString[count]
    count += 1
  return outputWords
# end parseStopWords

def countPuncts(inputString, minSentences=3, maxSentences=7): # Returns false if input is not a string
  # Count non consectutive punctuations
  if not isinstance(inputString, str):
    return 'Please enter a sentence.'
  punctuations = ['.', '?', '!']
  tooMany = 'Paragraphs should be no more than seven sentences.'
  tooFew = 'There should be at least three sentence in your paragraph.'
  count, sentenceCount = 0, 0
  while (count <= len(inputString)-1): # Iterate through each character searching for punctuation
    if count == len(inputString)-1: # For the last character
      if inputString[count] in punctuations: # If the character is a punctuation
        sentenceCount += 1
      break
    if inputString[count] in punctuations:
      while inputString[count] in punctuations: # Check for consecutive Punctuations
        count += 1
      sentenceCount += 1
    if sentenceCount > maxSentences:
      return tooMany
    count += 1
  if sentenceCount > maxSentences:
    return tooMany
  elif sentenceCount < minSentences:
    return tooFew
  else:
    return True