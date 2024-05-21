import stanza

# Download the French model
stanza.download('fr')  # 'fr' is the language code for French

# Set up the pipeline for French with necessary processors
nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma,depparse')

# Example French sentence
doc = nlp("Moscou a envoyé des troupes en Afghanistan.")
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"{word.text}\t{word.head}\t{word.deprel}")



doc = nlp("Ayant laissé le magasin sans surveillance, je suis sorti pour regarder le défilé.")
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"{word.text}\t{word.head}\t{word.deprel}")



doc = nlp("I am extremely short.")
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"{word.text}\t{word.head}\t{word.deprel}")



doc = nlp("Would you like brown rice or garlic naan?")
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"{word.text}\t{word.head}\t{word.deprel}")
