import unittest
from Deal import Deal
import time

class TestCases(unittest.TestCase):
    def test_check_deal_live(self):
        deal_mock = Deal("test1", 20, 1.3, 50, '123', 1)
        self.assertEqual(deal_mock.is_deal_live(), True, "Should be True")

    # def test_check_deal_live(self):
    #     deal_mock = Deal("test1", 20, 1.3, 1, '123', 1)
    #     time.sleep(70)
    #     self.assertEqual(deal_mock.is_deal_live(), False, "Should be True")

    def test_create_deal_sucess(self):
        deal_mock = Deal("test1", 20, 1.3, 50, '123', 1)
        self.assertEqual(deal_mock.claim_deal("123", 1), True, "Should be True")

    # def test_create_deal_fail_count(self):
    #     deal_mock = Deal("test1", 20, 1.3, 50, '123', 1)
    #     self.assertRaises(deal_mock.claim_deal("123", 2), ValueError)
    #
    # def test_create_deal_fail_count(self):
    #     deal_mock = Deal("test1", 20, 1.3, 50, '123', 1)
    #     deal_mock.claim_deal("123", 1)
    #     self.assertRaises(deal_mock.claim_deal("123", 1), ValueError)

    def test_create_deal_fail_count_1(self):
        deal_mock = Deal("test1", 2, 1.3, 50, '123', 1)
        deal_mock.claim_deal("123", 1)
        deal_mock.claim_deal("1231", 1)
        self.assertRaises(deal_mock.claim_deal("12312", 1), ValueError)

if __name__ == '__main__':
    unittest.main()