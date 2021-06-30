import pandas

# Create a dictionary from csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[char] for char in word]
print(output_list)
