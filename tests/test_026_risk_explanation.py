import unittest

from claims_risk_ledger.models import Record
from claims_risk_ledger.scoring import score_record


class DepthCheck26(unittest.TestCase):
    def test_026_risk_explanation(self):
        record = Record(id="claim-026", exposure=79800, signal=0.514, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
