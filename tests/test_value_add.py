import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from value_add import run_demo


class ValueAddDemoTest(unittest.TestCase):
    def test_value_add_demo_runs(self):
        result = run_demo()
        self.assertEqual(result["professor"], 'Andrew McCallum')
        self.assertEqual(result["project_family"], 'language')
        self.assertTrue(result["metrics"])

    def test_profile_is_professor_specific(self):
        profile = json.loads((ROOT / "data" / "advisor_profile.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["research_area"], 'ML, NLP, information extraction (CRFs), structured prediction')
        self.assertTrue(profile["representative_paper"])


if __name__ == "__main__":
    unittest.main()
