from langdetect import detect_langs

def identify_language(text):
    try:
        return detect_langs(text)
    except Exception as e:
        print(f"Error detecting language: {e}")
        return []

def identify_languages_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sentences = file.readlines()
            for sentence in sentences:
                langs = identify_language(sentence)
                print(f"Sentence: {sentence.strip()}")
                for lang in langs:
                    print(f" - Language: {lang.lang}, Probability: {lang.prob}")
                print("\n")
    except Exception as e:
        print(f"Error reading file: {e}")
def identify_languages_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sentences = file.readlines()
            print(f"Read {len(sentences)} sentences from {file_path}")
            for sentence in sentences:
                print(f"Processing: {sentence.strip()}")
                langs = identify_language(sentence)
                print(f"Detected languages: {langs}")
                for lang in langs:
                    print(f" - Language: {lang.lang}, Probability: {lang.prob}")
                print("\n")
    except Exception as e:
        print(f"Error reading file: {e}")

# Example usage
file_path = r'D:\pandas\pandas\NLP_advance\lang.txt'
identify_languages_in_file(file_path)


