import unittest

from claims_risk_ledger.models import Record
from claims_risk_ledger.scoring import score_record


class DepthCheck5(unittest.TestCase):
    def test_005_backlog_triage(self):
        record = Record(id="claim-005", exposure=84649, signal=0.321, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
