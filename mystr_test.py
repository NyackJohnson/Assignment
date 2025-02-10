import unittest
from mystr import slice,contains,replace,trim

class TestMyStr(unittest.Testcase):

def test_slice(self): #type:ignore
    self.assertEqual(slice("hello world", 2, 5), "llo")
    self.assertEqual(slice("hello world ", 5, 2), "")
    self.assertEqual(slice("hello world ",2, 20), "llo world")
    
def test_contains(self):
    self.assertEqual(contains("hello world", "world"), 6)
    self.assertEqual(contains("hello world", "python"), None)
    self.assertEqual(contains("hello hello world", "hello"), 0)

def test_replace(self):
    self.assertequal(replace("hello world","world","python"), "hello python")
    self.assertEqual(replace("hello world", "python", "java"), "hello world")
    self.assertEqual(replace("hello hello world", "hello", "hi"), "hi hello world")
    
    

def test_trim(self):
    self.assertequal(trim("hello world","world","python"), "hello python")
    self.assertEqual(trim("\t\n  aa  a\ta\", " aa a\ta")) #type:ignore
    self.assertEqual(trim("  "), "")
    #type:ignore