# KING JAMES VERSION (KJV) BIBLE DATASET

**Author(s): Mihir Rao, Siddhanth Agrawal**
**DATE: 3rd September, 2023**

## Introduction

This data (and supporting code) was developed in an effort to make the process of using the *King James Version (KJB) Bible* for any kind of computational research easier.

## API

In order to learn how to use this dataset, please take a look at the following example:

1. Make sure all three files ("Bible.py", "BibleBookNames.py", "BibleKJV.txt") in the same directory as your code that will be using the dataset.

2. Import the Bible class from the Bible.py file and instantiate a Bible object:

```python
# Import the Bible class
from Bible import Bible
# Instantiate a Bible object
bible_dict = bible.get_bible()
```

3. Now, simply use the Bible object to access the data. Before we take a look at a few examples, let's take a look at the structure of the data.

The ```get_bible()``` method from the ```Bible``` class returns a dictionary of the form:

```
{   
    "Genesis"   : d1,
    "Exodus"    : d2,
    ...
    "Revelation": d66
}
```

where d1 is a dict of the form:

```
{
    1 : {
        1 : "In the beginning God created the heaven and the earth.",
        2 : "And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.",
        ...
        31: "And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day."
        },
    2 : {
        1 : "Thus the heavens and the earth were finished, and all the host of them.",
        2 : "And on the seventh day God ended his work which he had made; and he rested on the seventh day from all his work which he had made.",
        ...
        25: "And they were both naked, the man and his wife, and were not ashamed."
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