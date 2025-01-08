import unittest
import tests_12_1
import tests_12_2

suite_test = unittest.TestSuite()
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(suite_test)