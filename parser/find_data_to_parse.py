import glob
import csv
import re
import glob
import nltk
from nltk.corpus import words

CORPUS_LOCATION = "/backups/contracts"

glob_files = glob.glob(CORPUS_LOCATION + "/*_text.txt")

pattern = ".{75}\$[0-9]+.{75}"

output = []


def is_english(token):
    if token in words.words():
        return True
    else:
        return False

def add_line(hit):
    with open('trainer.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([hit.replace("\\n", "")])

for f in glob_files:
    lines = "".join([l.replace("\\n", "") for l in open(f)]).replace("\\n", "")
    for hit in re.findall(pattern, lines):
        tokens = nltk.word_tokenize(hit)
        english_tokens = [t for t in tokens if is_english(t)]
        if float(len(english_tokens))/float(len(tokens)) > .5:   #if more than 50 % english...
            add_line(hit)