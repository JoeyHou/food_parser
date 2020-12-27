# 1. Handle special cases (see below in 2.1.2 Special cases handling)

# 2. Function for removing all numbers and spaces
def handle_numbers(text):
    clean_text = text
    clean_text = re.sub('[0-9]+\.[0-9]+', '' , clean_text)
    clean_text = re.sub('[0-9]+', '' , clean_text)
    clean_text = re.sub('\s\s+', ' ', clean_text)
    return clean_text

# 3. Function for removing punctuation
def drop_punc(text):
    clean_text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    return clean_text

# 4. Function for making all text lowercase
def lower(text):
    clean_text = text.lower()
    return clean_text

# 5. Remove normal stopwords
def remove_stop(my_text):
    text_list = my_text.split()
    return ' '.join([word for word in text_list if word not in stop_words])

# 6. Remove customized stopwords (see below in 2.1.2 Special cases handling)

# 7. Function for stripping whitespace
def my_strip(text):
    try: return text.strip()
    except Exception as e: return None

# 0. Special Cases
def handle_special_cases(text):
    clean_text = text
    if re.search('5\s*guys', text):
        clean_text = re.sub('5\s*guys', 'five-guys', clean_text)
    if re.search('[hH]2[Oo]', text):
        clean_text = re.sub('[hH]2[Oo]', 'water', clean_text)
    return clean_text

# 5. A list of additional stop-words for this project
my_stop_words = ['oc', 'amp', 'homemade', 'food', 'foodporn', 'v', 'x', 'recipe', 'best', 'il', 'ever',
                'time', 'attempt', 'first', 'ate', 'made', 'home', 'today', 'make', 'friend', 'local',
                'new', 'day', 'birthday', 'like', 'amazing', 'de', 'happy', 'year', 'plate', 'video', 
                'cooked', 'dish', 'house', 'os', 'tried', 'super', 'perfect', 'way', 'delicious', 
                'night', 'last', 'eating', 'know', 
                 'mg', 'oz', 'and', 'w', 'x', 'n', 'ml'
                 'handful']
                 
def remove_my_stop(text):
    text_list = text.split()
    return ' '.join([word for word in text_list if word not in my_stop_words])

def finalized_clean(text):
    text = lower(text)
    return my_strip(remove_my_stop(remove_stop(handle_numbers(drop_punc(text)))))

def remove_my_stop(text):
    text_list = text.split()
    return ' '.join([word for word in text_list if word not in my_stop_words])

def basic_clean(text):
    text = text.lower()
    return my_strip(remove_my_stop(remove_stop(drop_punc(text))))