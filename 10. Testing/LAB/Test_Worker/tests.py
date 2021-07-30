from unittest import TestCase, main

from Test_Worker.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Worker", 100, 100)

    def test_attr_are_sett(self):
        self.assertEqual('Worker', self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(100, self.worker.energy)

    def test_worker_energy_below_zero_expect_raise(self):
        self.worker.energy = -10
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_with_enough_energy(self):
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_worker_work__when_energy_is_0_expect_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_rest_raise_energy(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_worker_work__when_energy_is_above_0_expect_energy_to_be_decremented(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_get_info_method(self):
        result = self.worker.get_info()
        self.assertEqual('Worker has saved 0 money.', result)

if __name__ == '__main__':
    main()