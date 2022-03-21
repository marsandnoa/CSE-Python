import unittest
import triangles
import words
import diceroller
import fraction
import graph
class TestDemos(unittest.TestCase):
 def test_Triangle1(self):
   actual = triangles.triangles(1)
   expected = [0]
   self.assertEqual(actual, expected)
 def test_Triangle2(self):
   actual = triangles.triangles(5)
   expected = [0, 1, 3, 6, 10]
   self.assertEqual(actual, expected)
 def test_Triangle3(self):
   actual = triangles.triangles(10)
   expected = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
   self.assertEqual(actual, expected)
   
 def test_cTriangle1(self):
   actual = triangles.ctriangles(1)
   expected = [0]
   self.assertEqual(actual, expected)
 def test_cTriangle2(self):
   actual = triangles.ctriangles(5)
   expected = [0, 1, 3, 6, 10]
   self.assertEqual(actual, expected)
 def test_cTriangle3(self):
   actual = triangles.ctriangles(10)
   expected = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
   self.assertEqual(actual, expected)

 def test_pTriangle1(self):
   actual = triangles.pascal(1)
   expected = [[1.0]]
   self.assertEqual(actual, expected)
 def test_pTriangle2(self):
   actual = triangles.pascal(5)
   expected = [[1.0], [1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 3.0, 3.0, 1.0], [1.0, 4.0, 6.0, 4.0, 1.0]]
   self.assertEqual(actual, expected)
 def test_pTriangle3(self):
   actual = triangles.pascal(10)
   expected = [[1.0], [1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 3.0, 3.0, 1.0], [1.0, 4.0, 6.0, 4.0, 1.0], [1.0, 5.0, 10.0, 10.0, 5.0, 1.0], [1.0, 6.0, 15.0, 20.0, 15.0, 6.0, 1.0], [1.0, 7.0, 21.0, 35.0, 35.0, 21.0, 7.0, 1.0], [1.0, 8.0, 28.0, 56.0, 70.0, 56.0, 28.0, 8.0, 1.0], [1.0, 9.0, 36.0, 84.0, 126.0, 126.0, 84.0, 36.0, 9.0, 1.0]]
   self.assertEqual(actual, expected)


 def test_fraction1(self):
   actual = fraction.Fraction("15/20")
   expected = fraction.Fraction(3,4)
   self.assertEqual(actual, expected)
 def test_fraction3(self):
   actual = fraction.Fraction("0.1")
   expected = fraction.Fraction(1,10)
   self.assertEqual(actual, expected)
 def test_fraction4(self):
   actual = fraction.Fraction("0.2")
   expected = fraction.Fraction(2,10)
   self.assertEqual(actual, expected)
 def test_fraction5(self):
   actual = fraction.Fraction("0.3")
   expected = fraction.Fraction(3,10)
   self.assertEqual(actual, expected)
 def test_fraction6(self):
   actual = fraction.Fraction("0.45")
   expected = fraction.Fraction(9,20)
   self.assertEqual(actual, expected)
 def test_fraction7(self):
   actual = fraction.Fraction("45/20")
   expected = fraction.Fraction(45,20)
   self.assertEqual(actual, expected)
 def test_fraction8(self):
   actual = fraction.Fraction(1,1)
   expected = fraction.Fraction(1,1)
   self.assertEqual(actual, expected)
 def test_fraction9(self):
   actual = fraction.Fraction("45/20")
   expected = fraction.Fraction(45,20)
   self.assertEqual(actual, expected)
 def test_fraction10(self):
   actual = fraction.Fraction("21/20")
   expected = fraction.Fraction(21,20)
   self.assertEqual(actual, expected)
 def test_fraction11(self):
   actual = fraction.Fraction("23/20")
   expected = fraction.Fraction(23,20)
   self.assertEqual(actual, expected)
 def test_fraction12(self):
   actual = fraction.Fraction("0.4")
   expected = fraction.Fraction(2,5)
   self.assertEqual(actual, expected)
# i didnt know a good way to write these tests
 def test_graph1(self):
   matrix_g = graph.MatrixGraph([[False, True, False, True]
                              ,[True, False, True, False],
                              [False, True, False, True],
                              [True, False, True, False]])
   actual=matrix_g.breadth_first_search(0)
   expected = [1,3,0,2]
   self.assertEqual(actual, expected)

 def test_graph2(self):
  matrix_g = graph.MatrixGraph([[False, True, False, True],[True, False, True, False],[False, True, False, True],[True, False, True, False]])
  actual=matrix_g.depth_first_search(0)
  expected = [3,2,0,1]
  self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()