import os
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "diagnostic" / "usb-preflight.sh"

class UsbPreflightTests(unittest.TestCase):
    def run_with(self, version="MAZ_CMU-150_74.00.324A", preload=False):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for folder in ("jci/sm", "etc", "data_persist"):
                (root / folder).mkdir(parents=True, exist_ok=True)
            (root / "jci/version.ini").write_text(
                f'JCI_SW_VER="{version}"\nJCI_SW_FLAVOR="cmu150_EU"\n')
            body = "\n".join(f'<service name="{svc}"></service>'
                   for svc in ("jciCARPLAY", "jciAAPA", "jcinavi", "aap_service"))
            if preload:
                body += '\n<environ_var env_name="LD_PRELOAD" env_value="/other/mod.so"/>'
            (root / "jci/sm/sm.conf").write_text(body)
            before = {str(p.relative_to(root)): p.read_bytes()
                      for p in root.rglob("*") if p.is_file()}
            env = dict(os.environ, CMU_ROOT=d)
            output = subprocess.check_output(["sh", str(SCRIPT)], env=env, text=True)
            after = {str(p.relative_to(root)): p.read_bytes()
                     for p in root.rglob("*") if p.is_file()}
            self.assertEqual(before, after, "Preflight must not change CMU files")
            return output

    def test_supported_family_is_not_install_approval(self):
        output = self.run_with()
        self.assertIn("FW_FAMILY=match", output)
        self.assertIn("DECISION=NO_INSTALL_READ_ONLY_DIAGNOSTIC", output)

    def test_mismatch_is_unverified(self):
        self.assertIn("FW_FAMILY=unverified", self.run_with("70.00.100"))

    def test_existing_preload_flagged(self):
        self.assertIn("PRELOAD_sm.conf=present_manual_review",
                      self.run_with(preload=True))

if __name__ == "__main__":
    unittest.main()
