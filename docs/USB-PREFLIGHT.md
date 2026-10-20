# Universal USB preflight v0.1

`diagnostic/usb-preflight.sh` is a **read-only diagnostic**, not an installer.
It checks firmware family, existence of the four target services in both
service-manager configurations, presence of existing LD_PRELOAD values,
and known upstream HUD shim files. It outputs only coarse states, not private
service config contents.

Run offline tests:

```bash
python3 -m unittest discover -s tests -v
```

On a CMU with authorized shell access, run manually:

```sh
sh /path/to/usb-preflight.sh > /path/to/writable-usb/hud-preflight.txt
```

Redirecting output is the only write and must point to USB, not a CMU system
path. The script does not exploit USB boot entrypoints or auto-run. Do not
mistake its presence on a USB stick for a self-launching package.

A firmware-family match is **not approval to install**. It does not verify
board variant, green HUD support, wireless USB module, Yandex events, VBS
destination/ABI, or recovery availability.

Before offering automated USB installation, implement per-file snapshots and
hash verification, owned-change manifests, staged validation, transactional
rollback and tested recovery. Do not use upstream uninstall.sh wholesale.
