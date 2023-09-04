'''
NAME: Bible.py
PURPOSE: Extracts the bible text from a text file and stores it in a dictionary
'''

# Imports
from BibleBookNames import BibleBookNames
from typing import Dict, Optional
import os

# Class
class Bible():
    # Constructor
    def __init__(self, filename: str = "BibleKJV.txt"):
        self._BIBLE = self._load_bible(filename)
        
    
    # Methods
    def _load_bible(self, filename: str) -> Dict[str, Dict[int, Dict[int, str]]]:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Could not find file {filename}")

        BIBLE = {}

        with open(filename, "r") as f:
            for line in f:
                if line.startswith("Holy Bible, Authorized (King James) Version, Textfile 930105."):
                    continue
                book_name_and_chapter, verse_num_and_verse = line.split(":", 1)
                book_name = book_name_and_chapter.rstrip("0123456789")
                chapter_num = int(book_name_and_chapter[len(book_name):])
                verse_num = int(verse_num_and_verse.split(" ", 1)[0])
                verse_text = verse_num_and_verse[len(str(verse_num)) + 1:]

                if book_name in BIBLE:
                    if chapter_num in BIBLE[book_name]:
                        BIBLE[book_name][chapter_num][verse_num] = verse_text
                    else:
                        BIBLE[book_name][chapter_num] = {verse_num: verse_text}
                else:
                    BIBLE[book_name] = {chapter_num: {verse_num: verse_text}}

        books_to_update = []
        for book_name in BIBLE:
            if book_name in BibleBookNames.MAPPING:
                full_book_name = BibleBookNames.MAPPING[book_name]
                books_to_update.append((book_name, full_book_name))

        for old_name, new_name in books_to_update:
            BIBLE[new_name] = BIBLE.pop(old_name)

        return BIBLE
    
    # Getters
    def get_bible(self) -> Dict[str, Dict[int, Dict[int, str]]]:
        return self._BIBLE

    def get_book_names(self) -> list:
        return list(self._BIBLE.keys())

    def get_chapters(self, book_name: str) -> Optional[Dict[int, Dict[int, str]]]:
        return self._BIBLE.get(book_name)

    def get_verse(self, book_name: str, chapter: int, verse: int) -> Optional[str]:
        try:
            return self._BIBLE[book_name][chapter][verse]
        except KeyError:
            return None