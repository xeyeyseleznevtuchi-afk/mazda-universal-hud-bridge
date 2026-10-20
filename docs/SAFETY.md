# Vehicle safety and data handling

No scripts in this repository write to a head unit. Do not run third-party USB installers until the actual configuration and working rollback are understood.

## Before any future firmware modification

1. Work with vehicle safely parked, parking brake engaged, reliable power supply.
2. Take **read-only** snapshots of `/jci/sm/sm.conf`, `/jci/sm/sm_WCP.conf`, `/etc/aap_system_attributes.xml`, `/etc/aap_system_attributes_UCP.xml` where present.
3. Identify all existing `LD_PRELOAD` entries and distinguish old Android Auto Headunit App tweaks from OEM Android Auto.
4. Treat existing `/etc/*.orig` backups as potentially **modified**, not necessarily factory original.
5. Any future installer should patch only owned XML nodes; restore only its own edits; verify firmware and target services; abort on unknown state.
6. Never ship an auto-run script that calls `mount -o rw,remount /` and blindly rewrites `sm.conf`.
7. Do not upload Wi-Fi/Bluetooth credentials, serial numbers, MAC addresses, VIN, personal navigation traces or exact location logs.
8. Allow an independent recovery path before testing injection on a vehicle.

**Risk:** overwriting `sm.conf` may break the installed wireless AA/CarPlay module or prevent services from starting. A rootfs `LD_PRELOAD` failure can cause infotainment crashes. Even if a developer claims a tweak cannot brick a unit, treat that as unverified.
