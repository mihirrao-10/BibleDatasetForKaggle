# KING JAMES VERSION (KJV) BIBLE DATASET API

**Author(s): Mihir Rao, Siddhanth Agrawal**

**DATE: 4th September, 2023**

## Introduction

This dataset API was developed to make using the *King James Version (KJB) Bible* for any computational research easier.

## API

In order to learn how to use this dataset, please take a look at the following example:

1. Make sure all three files ("Bible.py", "BibleBookNames.py", "BibleKJV.txt") in the same directory as your code that will be using the dataset.

2. Import the Bible class from the Bible.py file and instantiate a Bible object:

```python
# Import the Bible class
from Bible import Bible
# Instantiate a Bible object
bible = Bible()
```

3. Now, simply use the Bible object to access the data. Before we take a look at a few examples, let's take a look at the structure of the data.

The ```get_bible()``` method from the ```Bible``` class returns a dictionary of the form:

```
{   
    "Genesis"   : d1,    # Book 1
    "Exodus"    : d2,    # Book 2
    ...
    "Revelation": d66    # Book 66
}
```

where, for example, d1 is a dict of the form

```
{
    1 : {    # Chapter 1
        1 : "In the beginning God created the heaven and the earth.",    # Chapter 1, Verse 1
        2 : "And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.",    # Chapter 1, Verse 2
        ...
        },
    2 : {    # Chapter 2
        1 : "Thus the heavens and the earth were finished, and all the host of them.",    # Chapter 2, Verse 1
        2 : "And on the seventh day God ended his work which he had made; and he rested on the seventh day from all his work which he had made.",    # Chapter 2, Verse 2
        ...
        },
    ...
}
```

4. A few examples of how to use the data:

```python
# Get all the book names of the Bible as a list
bible_books = bible.get_book_names()

# Get the entire book of Genesis as a dictionary
genesis_dict = bible_dict["Genesis"]

# Get the first chapter of the book of Genesis as a dictionary
genesis_chapter_1_dict = bible_dict["Genesis"][1]

# Get the first verse of the first chapter of the book of Genesis as a string
genesis_chapter_1_verse_1 = bible_dict["Genesis"][1][1]

# And so on...
```

5. That's it! You're all set to use the dataset!

## References

1. https://www.o-bible.com/download/kjv.txt (KJV Bible)
