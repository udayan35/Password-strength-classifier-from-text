import pandas as pd
import math
from collections import Counter
import string

# Read file into DataFrame
df = pd.read_csv('rockyou.txt', header=None, names=['password'], encoding='utf-8', on_bad_lines='skip')

# Convert all entries to strings using comprehension
df['password'] = [str(p).strip() for p in df['password']]

def calculate_entropy(s):
    # Count frequency of each character
    counter = Counter(s)
    length = len(s)
    if length == 0:
        return 0

    # Calculate entropy
    entropy = -sum((count / length) * math.log2(count / length) for count in counter.values())
    return entropy

def num_char_types(s):
    sum=0
    has_upper = any(c.isupper() for c in s)
    has_lower = any(c.islower() for c in s)
    has_digit = any(c.isdigit() for c in s)
    has_special = any(c in string.punctuation for c in s)
    if(has_upper):
        sum+=1
    if(has_lower):
        sum+=1
    if(has_digit):
        sum+=1
    if(has_special):
        sum+=1
    return sum

from decimal import Decimal, getcontext, InvalidOperation
import string

# Set high precision
getcontext().prec = 100

def estimate_brute_force_time(password, guesses_per_second=1e9):
    try:
        length = int(len(password))
        charset_size = 0

        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in string.punctuation for c in password):
            charset_size += len(string.punctuation)

        # Ensure these are integers before using Decimal
        charset_size = int(charset_size)

        total_combinations = Decimal(charset_size) ** Decimal(length)
        average_guesses = total_combinations / Decimal(2)
        seconds = average_guesses / Decimal(str(guesses_per_second))  # wrap as string to avoid float imprecision

        return float(seconds)

    except (InvalidOperation, ValueError, ZeroDivisionError) as e:
        return float('inf')  # or handle/log the error as needed

import math

def classify_password(password):
    length = len(password)
    entropy = calculate_entropy(password)
    char_types = num_char_types(password)

    # Estimate brute-force time in seconds
    bft = estimate_brute_force_time(password)
    log_bft = math.log10(bft + 1) if bft > 0 else 0

    # Scoring
    score = 0
    score += 2 if length >= 12 else 1 if length >= 8 else 0
    score += 2 if entropy >= 60 else 1 if entropy >= 40 else 0
    score += max(char_types - 1, 0)  # from 0 to 3
    score += 2 if log_bft >= 12 else 1 if log_bft >= 6 else 0

    # Classification
    if score >= 7:
        return 'hard'
    elif score >= 5:
        return 'medium'
    elif score >= 3:
        return 'easy'
    else:
        return 'very easy'



l=[len(x) for x in df['password']]
df.insert(1,'Length',l,True)

l=[calculate_entropy(x) for x in df['password']]
df.insert(2,'Entropy',l,True)

l=[num_char_types(x) for x in df['password']]
df.insert(3,'Variety',l,True)

l=[estimate_brute_force_time(x) for x in df['password']]
df.insert(4,'Break_Time',l,True)

l=[classify_password(x) for x in df['password']]
df.insert(5,'Strength',l,True)

#df['strength'] = df.apply(classify_password, axis=1)
df = df.dropna(subset=['password']) 
df.to_csv("final.csv")
# Optional: verify 
print(df.head())
print(df.dtypes)