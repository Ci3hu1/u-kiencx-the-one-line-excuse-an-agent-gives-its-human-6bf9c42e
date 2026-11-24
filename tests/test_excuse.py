"""Tests for the one-line excuse entry.

Verifies the judge's form rules exactly: one line, at most 160
characters, deterministic output, output file mode 0644.
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import LINE  # noqa: E402


class TestExcuse(unittest.TestCase):
    def test_one_line(self):
        self.assertNotIn("\n", LINE)
        self.assertEqual(len(LINE.split("\n")), 1)

    def test_at_most_160_chars(self):
        self.assertGreaterEqual(len(LINE), 1)
        self.assertLessEqual(len(LINE), 160)

    def test_no_trailing_whitespace(self):
        self.assertEqual(LINE, LINE.strip())

    def test_gate_validation_rejects_bad_line(self):
        import main as entry

        with self.assertRaises(SystemExit):
            entry.validate("two\nlines")
        with self.assertRaises(SystemExit):
            entry.validate("x" * 161)
        with self.assertRaises(SystemExit):
            entry.validate(" trailing space ")
        entry.validate(LINE)  # the real line passes

    def test_is_an_excuse_to_a_human(self):
        self.assertIn("deadline", LINE)
        self.assertIn("my future self", LINE)

    def test_deterministic_output(self):
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
                proc = subprocess.run(
                    [sys.executable, "-P", "-s", "main.py"],
                    cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    env=env, capture_output=True, text=True,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as fh:
                    outs.append(fh.read())
                mode = os.stat(os.path.join(tmp, "entry.txt")).st_mode & 0o777
                self.assertEqual(mode, 0o644)
        self.assertEqual(outs[0], outs[1])
        self.assertEqual(outs[0], LINE)


if __name__ == "__main__":
    unittest.main()
