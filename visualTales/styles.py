from os.path import dirname, realpath # Used to get the absolute path for the currently running file
from .textParser import parseStopWords

class Prompt_Stylizer(): # Object handling the text prompts
  def __init__(self):
    self.__styles = ['realistic', 'oil_painting', 'pencil_drawing', 'concept_art', 'digital_art', 'cartoon', 'anime', 'manga', 'sketch', 'watercolor', 'absract', 'surrealism', 'pop_art', 'futurism']
    self.__arrayOfWords = []
    self.__stopWordsFile = dirname(realpath(__file__)) + '/' + 'stopWords.txt' #'visualTales/stopWords.txt'
    self.__inputStyle = ''
    self.__inputPrompt = ''
    self.__outputPrompt = ''
    #print('CURRENT WORKING DIRECTORY: ', os.path.dirname(os.path.realpath(__file__))) # Gets the current file's directory
    
  def setStopWordsFile(self, inputString): # Sets the name of the file for the stopWords.txt
    if isinstance(inputString, str):
      self.__stopWordsFile = inputString
      
  def setStyle(self, inputString): # DO NOT USE # Sets the input style to a new string
    if isinstance(inputString, str):
      self.__inputStyle = inputString # Input the Style into the generateOutputPrompt instead

  def setPrompt(self, inputString): # Sets the input prompt to a new string
    if isinstance(inputString, str):
      self.__inputPrompt = inputString

  def getStyles(self): # Returns a string of supported/suggested styles
    info = ''
    for i, v in enumerate(self.__styles):
      if v == len(self.__styles)-1:
        info += i
        break
      info += i + ','
    return info
    
  def generateArrayOfWords(self): # Calls parse words to parse the stop words out of the prompt and format it into a list
    self.__arrayOfWords = parseStopWords(self.__inputPrompt)
    
  def generateOutputPrompt(self, inputStyle, inputPrompt=None): # Returns a prompt based on the inputted style, returns False when style is not supported or when the inputPrompt is not a string
    if not (isinstance(inputStyle, str)):
      return False
    if inputPrompt != None:
      if not (isinstance(inputPrompt, str)):
        return False
    if inputStyle.lower() not in self.__styles:
      return False
      
    self.__outputPrompt = ''
    if inputStyle.lower() == 'realistic':
      self.__outputPrompt = 'realistic, '
    elif inputStyle.lower() == 'oil_painting':
      self.__outputPrompt = 'oil painting, '
    elif inputStyle.lower() == 'pencil_drawing':
      self.__outputPrompt = 'pencil drawing, '
    elif inputStyle.lower() == 'concept_art':
      self.__outputPrompt = 'concept art, '
    elif inputStyle.lower() == 'digital_art':
      self.__outputPrompt = 'digital art, '
    elif inputStyle.lower() == 'cartoon':
      self.__outputPrompt = 'cartoon, '
    elif inputStyle.lower() == 'anime':
      self.__outputPrompt = 'anime, '
    elif inputStyle.lower() == 'manga':
      self.__outputPrompt = 'manga, '
    elif inputStyle.lower() == 'sketch':
      self.__outputPrompt = 'sketch, '
    elif inputStyle.lower() == 'watercolor':
      self.__outputPrompt = 'watercolor, '
    elif inputStyle.lower() == 'abstract':
      self.__outputPrompt = 'abstract, '
    elif inputStyle.lower() == 'surrealism':
      self.__outputPrompt = 'surrealism, '
    elif inputStyle.lower() == 'pop_art':
      self.__outputPrompt = 'pop art, '
    elif inputStyle.lower() == 'futurism':
      self.__outputPrompt = 'futurism, '
    else: # This should never occur, but just incase
      return False

    if inputPrompt != None: # When the function is given a new prompt, we must parse that prompt first
      self.__arrayOfWords = parseStopWords(self.__stopWordsFile, inputPrompt) # Parse the prompt for stopwords
      for i, v in enumerate(self.__arrayOfWords):
        if i != (len(self.__arrayOfWords)-1):
          self.__outputPrompt += v + ', '
        else:
          self.__outputPrompt += v 
    else: # If no new prompt was given then we assume that the prompt was given earlier
      for i, v in enumerate(self.__arrayOfWords):
        if i != (len(self.__arrayOfWords)-1):
          self.__outputPrompt += v + ', '
        else:
          self.__outputPrompt += v 
    return self.__outputPrompt
# end Styles