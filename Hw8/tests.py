import hw8
from collections import namedtuple, deque, Counter
import unittest
class TestDemos(unittest.TestCase):
 def test_uniform0(self):
   actual = hw8.uniform(20,40)
   bol=actual<40
   if bol:
     if actual>=20:
      self.assertEqual(1,1)

 def test_randrang0(self):
   actual = hw8.randrange(20,40)
   bol=actual<40
   if bol:
     if actual>=20:
      self.assertEqual(1,1)
 def test_randrang1(self):
   actual = hw8.randrange(20,40)
   if(actual%1)==0:
    self.assertEqual(1,1)
     
 def test_choice(self):
   actual = hw8.choice(range(5))
   if actual in range(5):
     self.assertEqual(actual, expected)
 
 def test_card0(self):
   actual = card(4,13)
   expected=(4,13)
   self.assertEqual(actual, expected)
 def test_card1(self):
   actual = hw8.std_card_deck()
   print(actual)
 def test_card3(self):
   actual = hw8.mix_deck(hw8.std_card_deck())
   print(actual)
 def test_card4(self):
   actual = hw8.deal(hw8.std_card_deck(),6)
   if(len(actual)==6):
     if(len(actual[0])==12):
       self.assertEqual(1,1)
 def test_letterfreq(self):
   actual = hw8.popular_letter("SSSSOOOAAAMMN")
   expected="S"
   self.assertEqual(actual,expected)
   
if __name__ == '__main__':
    card = namedtuple("Card", "suit rank")
    unittest.main()