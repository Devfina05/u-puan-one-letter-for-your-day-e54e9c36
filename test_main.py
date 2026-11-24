"""Tests for the One Letter for Your Day entry (main.py).

Run with: python3 test_main.py
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import main


class TestEntry(unittest.TestCase):
    def test_choose_letter_is_single_uppercase(self):
        letter = main.choose_letter()
        self.assertEqual(len(letter), 1)
        self.assertTrue("A" <= letter <= "Z")
        self.assertEqual(letter, "Z")

    def test_word_matches_letter(self):
        self.assertTrue(main.WORD.startswith(main.LETTER.lower()))

    def test_write_entry_is_exactly_one_byte(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "entry.txt")
            letter = main.write_entry(path)
            with open(path, "rb") as handle:
                raw = handle.read()
            self.assertEqual(raw, b"Z")
            self.assertEqual(len(raw), 1)
            self.assertEqual(letter, "Z")

    def test_write_entry_creates_missing_dirs(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "nested", "dir", "entry.txt")
            main.write_entry(path)
            with open(path, "r", encoding="utf-8") as handle:
                self.assertEqual(handle.read(), "Z")

    def test_output_is_valid_utf8_single_char(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "entry.txt")
            main.write_entry(path)
            with open(path, "r", encoding="utf-8") as handle:
                text = handle.read()
            self.assertEqual(len(text), 1)
            self.assertFalse(text.isspace())


if __name__ == "__main__":
    unittest.main(verbosity=2)
