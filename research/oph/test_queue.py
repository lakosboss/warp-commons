"""Run with python3 -m unittest discover -s research/oph -p 'test_*.py'."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from queue_ops import Queue


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        parent = Path(__file__).resolve().parent
        for name in ("queue.json", "README.md"):
            shutil.copyfile(parent/name, self.root/name)
        for name in ("plans", "results"):
            (self.root/name).mkdir()
        self.key = "OPH-006"
        self.result = dict(outcome="conditional", summary="fixture only", limits="test",
                           reproduce="python placeholder.py", plan_changes="none",
                           evidence=["README.md"])

    def queue(self):
        return Queue(self.root)

    def start(self):
        self.queue().start(self.key, ["fixed fixture"], "mismatch", "calculate")

    def test_full_handoff(self):
        self.assertEqual(self.queue().next(), self.key)
        self.start()
        self.assertIn("existing plan", self.queue().prompt(self.key))
        self.queue().finish(self.key, self.result)
        self.assertEqual(self.queue().next(), "OPH-007")
        self.assertEqual(self.queue().results[self.key]["outcome"], "conditional")
        with self.assertRaises(ValueError):
            self.queue().finish(self.key, self.result)

    def test_preflight_required(self):
        with self.assertRaises(ValueError):
            self.queue().finish(self.key, self.result)

    def test_duplicate_preflight(self):
        self.start()
        with self.assertRaises(FileExistsError):
            self.start()

    def test_evidence_cannot_escape(self):
        self.start()
        with self.assertRaises(ValueError):
            self.queue().finish(self.key, dict(self.result, evidence=["/etc/hosts"]))

    def test_joint_check_waits(self):
        with self.assertRaises(ValueError):
            self.queue().next("OPH-010")
        for i in range(6,10):
            self.key = f"OPH-00{i}"
            self.start()
            self.queue().finish(self.key, self.result)
        self.assertEqual(self.queue().next(), "OPH-010")

    def test_rejects_invalid_dependency(self):
        file = self.root/"queue.json"
        data = json.loads(file.read_text())
        data["checks"][0]["depends_on"] = ["OPH-010"]
        file.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            self.queue()
