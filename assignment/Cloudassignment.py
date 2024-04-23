# importing dependecies
import nltk
import logging
nltk.download('stopwords')
nltk.download('punkt')
from typing import List
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# reading the text file
def read_file(path: str = "paragraphs.txt" ) -> str:
    try:
        with open(path, 'r', encoding= 'utf-8') as file:
            content = file.read()
    except FileNotFoundError as e:
        logger.error(f"File not found, check the path: {e}")
        raise
    except Exception as e:
        logger.error(f"Error occurred while reading the file: {e}")
        raise
    return content
 
def filter_text(text: str)-> List[str]:
    #making a set of stop words to filter it later
    stop_words = set(stopwords.words('english'))
    #splitting words from the text file
    try:
        word_tokens = word_tokenize(text)
    except UnicodeDecodeError as e:
        logger.error(f"Invalid characters, check your text: {e}")
        raise
    except Exception as e:
        logger.error(f'Error occurred while filtering the text {e}')
        raise
    #filter words that is not a stop word
    filtered_content = [w for w in word_tokens if w.lower() not in stop_words]
    return filtered_content

#calculate freq of each word
def freq(filteredContent: List[str]):
    try:
        freq = Counter(filteredContent)
    except ValueError as e:
        logger.error(f'this method takes list of words, please check your input: {e}')
        raise
    except Exception as e:
        logger.error(f"Error occured while calculating frequency: {e}")
        raise
    return freq.items()


try:
    content = read_file()
    filtered_content = filter_text(content)
    print(freq(filtered_content))
except Exception as e:
    logger.error(f'An unexpected error occurred : {e}')