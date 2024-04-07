import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder
# Load the model from the file
max_length = 6
model = joblib.load('rf_morse_model1.pkl')
label_encoder = joblib.load('morse_label_encoder1.pkl')

# Example Morse code for "E" (dot)

morse_sequence = "./.-//.----"
morse_code_mapping = {".": 0, "-": 1, "/": -1, "//": -2}
morse_sequence = morse_sequence.replace('//', '/ /')  # Add space between words
morse_parts = morse_sequence.split('/')
morse_encoded = []
for part in morse_parts:
    word_parts = part.split('/')
    for word_part in word_parts:
        word_encoded = []
        for char in word_part:
            if char == ' ':
                word_encoded.append(2)  # Add space between characters
            else:
                word_encoded.extend([morse_code_mapping[char] for char in char])
        # morse_encoded.append(word_encoded)
        if word_encoded:
            morse_encoded.append(word_encoded)
            word_encoded = []
# for part in morse_parts:
#     if part == ' ':
#         morse_encoded.append(2)  # Add space between words
#     else:
#         morse_encoded.extend([morse_code_mapping[char] for char in part])
# Convert Morse code sequence to its numerical representation
#morse_encoded = [morse_code_mapping[char] for char in morse_sequence]
#morse_encoded += [2] * (max_length - len(morse_encoded))
# if len(morse_encoded) > max_length:
#     morse_encoded = morse_encoded[:max_length]  # Truncate if more than 6 features
# elif len(morse_encoded) < max_length:
#     morse_encoded += [2] * (max_length - len(morse_encoded))  # Pad with 2s if less than 6 features
for i in range(len(morse_encoded)):
    if len(morse_encoded[i]) > max_length:
        morse_encoded[i] = morse_encoded[i][:max_length]  # Truncate if more than 6 features
    elif len(morse_encoded[i]) < max_length:
        morse_encoded[i] += [2] * (max_length - len(morse_encoded[i]))  # Pad with 2s if less than 6 features
# Predict
morse_encoded_flat = np.array([np.array(word).flatten() for word in morse_encoded])
#predicted_text_encoded = model.predict([morse_encoded])
predicted_text_encoded = model.predict(morse_encoded_flat)
predicted_text = label_encoder.inverse_transform(predicted_text_encoded)  # Assuming label_encoder is loaded

print(morse_encoded)
print("Predicted Class:", predicted_text_encoded)
print(label_encoder.classes_)
# Combine the predicted characters into words
predicted_text = ''.join(predicted_text)

# Split the predicted text into separate words based on spaces
predicted_words = predicted_text.split(' ')

# Print the predicted words
print("Predicted Words:", predicted_words)
# print("Predicted Text:", predicted_text)

# Assuming y_test contains your true labels
