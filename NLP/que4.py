import pandas as pd
import nltk
import re

def remove_special_characters(df, column):
    nltk.download('punkt')

    
    def remove_special_chars(text):
      
        words = nltk.word_tokenize(text)

        #used regex
        clean_words = [re.sub(r'[^a-zA-Z0-9\s]', '', w) for w in words]
        clean_text = ' '.join(clean_words)

        return clean_text
    df[column] = df[column].apply(remove_special_chars)

    return df

# Example usage:
data = {'text_column': ['This is a sample text with special characters: $%@#^&']}
df = pd.DataFrame(data)
cleaned_df = remove_special_characters(df, 'text_column')
print(cleaned_df)
