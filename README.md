# anki-flashcard-creator
Simple automated software for turning a list of example sentences into Cloze flashcards for Anki.

Usage instructions:
a) Fill the file 'exSents.txt' with example sentences, in the form '[LANGUAGE YOU'RE STUDYING]  [LANGUAGE YOU SPEAK]' separated by linebreaks (the space should be a tab.
b) Fill the file 'wordlist.txt' with the words you want to test yourself on. For example, I made a German flashcard conjugation tool (https://ankiweb.net/decks/share/1768148642497).
c) Run the program through your terminal. Your finished deck will appear as 'deck.txt'.
d) Make a new note type in Anki, with slots 'incompletesentence', 'fullsentence', 'translation', 'missingword' and maybe 'notes' if you want to provide context clues.
e) Import into Anki, using '|' as the field separator. Select the note type you've just created, put the right info in the right field, and enjoy! 

Unfortunately the way I've programmed this relies on spacing-based languages to track the word boundary, so there is no support for Chinese/Japanese or for multi-word vocab requests :( I'm sure somebody can think of a solution but I don't really plan on spending time working on this, so feel free to fork :P
