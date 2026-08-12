import unittest

from claims_risk_ledger.models import Record
from claims_risk_ledger.scoring import score_record


class DepthCheck14(unittest.TestCase):
    def test_014_scenario_analysis(self):
        record = Record(id="claim-014", exposure=39371, signal=0.890, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
