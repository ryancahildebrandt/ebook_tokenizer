#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:12:24 2021

@author: ryan
"""
import re
import sys

from sudachipy import dictionary
from sudachipy import tokenizer

tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C

with open(sys.argv[1], encoding='shift_jis') as file:
    contents = file.read()
    intro = re.sub("(\n-*\n)(.*\n)*", "", contents)
    body = re.sub("(.*\n)*-{3,}\n(\u3000)*", "", contents)
    tokens = [m.surface() for m in tokenizer_obj.tokenize(body, mode)]
    tokenized = " ".join(tokens)
    out = intro + "\n + + + + + + + \n" + tokenized + "\n + + + + + + + \n"
    title = str(intro).replace("\n","_").replace(")","").replace("(","").replace(" ","_")
    filename = "./" + title + "_word_tokenized.txt"

with open(filename, "w") as out_file:
    print(out, file=out_file)