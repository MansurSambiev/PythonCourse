import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_runner = Runner('walker')
        for _ in range(10):
            walk_runner.walk()
        self.assertEqual(walk_runner.distance, 50)

    def test_incorrect(self):
        walk_runner = Runner('walker')
        for _ in range(5):
            walk_runner.walk()
        self.assertEqual(walk_runner.distance, 5)

    def test_run(self):
        new_runner = Runner('runner')
        for _ in range(10):
            new_runner.run()
        self.assertEqual(new_runner.distance, 100)

    def test_challenge(self):
        challenger1 = Runner('challenger1')
        challenger2 = Runner('challenger2')
        for _ in range(10):
            challenger1.walk()
            challenger2.run()
        self.assertNotEqual(challenger1.distance, challenger2.distance)
