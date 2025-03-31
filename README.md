# Japanese eBook Tokenizer for Kindle WordWise

---

---
[![Open in gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ryancahildebrandt/ebook_tokenizer)
[![This project contains 0% LLM-generated content](https://brainmade.org/88x31-dark.png)](https://brainmade.org/)

## *Purpose*
A quick and dirty command line function (built in python) to tokenize Japanese text and insert spaces between words. It's designed to work on eBooks (.txt files) taken from [Archive.org](https://archive.org/details/texts) or [Aozora Bunko](https://aozora.gr.jp) repositories. "But why the need for spaces when Japanese isn't usually written with spaces between words?" you may ask; the only reason I wanted spaces is so that my kindle will be able to separate words and allow me to look them up when I'm reading. For just about every other use it is admittedly not ultra useful! I've only used it on a few books taken from each of the above sources, so if you find it useful but not quite effective for some books, let me know.

---

## *Usage*

+ python3 archive_tokenize.py 'path_to_archive_org_txt_file'
+ python3 aozora_tokenize.py 'path_to_aozora_bunko_txt_file'
+ It will save the new text in the same directory as the script, and name it with meta info from the original file


