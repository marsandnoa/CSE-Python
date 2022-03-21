import triangles
import words
import diceroller
import fraction
import graph

#testing code from question 1

#triangles 1
print("Question1------------------------------------------------------")
print("Triangle number calculation")
print(triangles.triangles(1))
print(triangles.triangles(5))
print(triangles.triangles(10))
#print(triangles.triangles(100))
#print(triangles.triangles(10000))
print(triangles.ctriangles(1))
print(triangles.ctriangles(5))
print(triangles.ctriangles(10))
#print(triangles.triangles(100))
#print(triangles.triangles(10000))
print("Pascal number calculation")
print(triangles.pascal(1))
print(triangles.pascal(5))
print(triangles.pascal(10))

print("Question2------------------------------------------------------")
print("DiceRoller")
print(diceroller.diceroller(20,5000))
diceroller.print_bar_chart(diceroller.diceroller(20,5000))
diceroller.print_bar_chart(diceroller.diceroller(20,15))
diceroller.print_bar_chart(diceroller.diceroller(4,15))

print("Question3------------------------------------------------------")
# only 1 test bc of the need for a file
print(words.firstlines("ex.txt"))

print("Question4------------------------------------------------------")
print(fraction.Fraction.from_str(0,"15/20"))
print(fraction.Fraction.from_str(0,"22/20"))
print(fraction.Fraction.from_str(0,"0.1"))
print(fraction.Fraction.from_str(0,"0.2"))
print(fraction.Fraction.from_str(0,"0.3"))
print(fraction.Fraction.from_str(0,"0.45"))
print(fraction.Fraction.from_str(0,"45/20"))
print(fraction.Fraction(1,1))
print(fraction.Fraction("45/20"))
print(fraction.Fraction("21/20"))
print(fraction.Fraction("23/20"))
print(fraction.Fraction("0.4"))

print("Question5------------------------------------------------------")

vertices = {0, 1, 2, 3}
edges = {(0, 1)}

# not implemented
# try:
#     print("EdgelistGraph")
#     edge_g = graph.EdgelistGraph([(0, 1), (0, 2), (2, 1), (2, 3)])
#     print(f"{str(edge_g)  = }")
#     print(f"{repr(edge_g) = }")
#     print()
# except NotImplementedError as e:
#     print(f"Ignoring {repr(e)}")
matrix_g = graph.MatrixGraph([[False, True, False, True]
                              ,[True, False, True, False],
                              [False, True, False, True],
                              [True, False, True, False]])
set=matrix_g.breadth_first_search(0)
set2=matrix_g.depth_first_search(0)
for i in set:
  print(i)
for i in set2:
  print(i)