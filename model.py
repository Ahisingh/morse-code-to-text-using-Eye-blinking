import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from morse_code import from_morse
# Example Morse code dataset
# Morse code for "HELLO WORLD"
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----","¦",".-.-.-","--..--","..--..",".----.",".--.-.","-....-",".-..-.","---...","---...","-...-","-.-.--","-..-.","-.--.","-.--.-"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," ",".",",","?","'","@","-",'"',":",";","=","!","/","(",")"]

def decode_morse_code(morse_string):
    decoded_text = ""
    morse_sequence = morse_string.split('//') # Split by '//' for words
    for word_morse in morse_sequence:
        word_decoded = ""
        morse_letters = word_morse.split('/') # Split by '/' for letters within a word
    for morse_char in morse_letters:
        if morse_char:
            decoded_char = from_morse(morse_char)
            word_decoded += decoded_char
            decoded_text += word_decoded + " " # Add space between words
    return decoded_text.strip()
# Preprocessing: Convert Morse code to a simple numerical format
# For simplicity, let's convert "." to 0 and "-" to 1, and pad sequences to have equal length
# This is a very naive approach and might not work well for all Morse code sequences
max_length = max(len(code) for code in morse_code)
X = []
for code in morse_code:
    numeric_code = [0 if symbol == "." else 1 for symbol in code]  # Convert to 0s and 1s
    numeric_code += [2] * (max_length - len(code))  # Pad with 2s to ensure equal length
    X.append(numeric_code)

# Convert lists to numpy arrays for scikit-learn
X = np.array(X)
y = np.array(letters)

# Encoding the labels (text)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Training the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y_encoded)

# Saving the model and label encoder to files
joblib.dump(model, 'rf_morse_model1.pkl')
joblib.dump(label_encoder, 'morse_label_encoder1.pkl')

print("Model and label encoder have been saved.")