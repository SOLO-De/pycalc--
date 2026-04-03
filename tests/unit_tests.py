import unittest
import pycalc.pycalc as calculator

class PyCalcUnitTests(unittest.TestCase):
  def test_add(self):
    left = [5,7,365,0,0,0,-50,-12,-4,32,4,-16,7]
    right = [9,0,-2,445,0,-54,100,0,-49,-32,-6,16,5]
    expected = [14,7,363,445,0,-54,50,-12,53,0,-2,0,-2]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.add(l, r)
        self.assertEqual(got, e)
  
  def test_mult(self):
    left = [5,5,5,0,0,0,-5,-5,-5]
    right = [9,0,-9,9,0,-9,9,0,-9]
    expected = [45,0,-45,0,0,0,-45,0,-45]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.multiply(l, r)
        self.assertEqual(got, e)

  def test_sous(self):
    left = [5]
    right = [9]
    expected = [-4]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.subtract(l, r)
        self.assertEqual(got, e)

  def test_divi(self):
    left = [45]
    right = [9]
    expected = [5]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.devide(l, r)
        self.assertEqual(got, e)

if __name__ == '__main__':
  unittest.main()
