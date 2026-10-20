#!/bin/sh
# Mazda Universal HUD Bridge — read-only diagnostic, v0.3
# Run manually from an existing authorized CMU shell. No autorun, no root remount.
set -u
OUT="${1:-/tmp/mazda-hud-diagnostic.txt}"
case "$OUT" in /tmp/*|/mnt/*) ;; *) echo "Output must be under /tmp or /mnt" >&2; exit 2;; esac
umask 077
{
  echo "Mazda Universal HUD Bridge — sanitized inspection"
  echo "No configuration contents, IDs or navigation traces are copied."
  echo "firmware_family:"
  if [ -r /jci/version.ini ]; then
    sed -n 's/^JCI_SW_VER=.*\(74\.00\.324\).*/\1/p' /jci/version.ini | head -n 1
  else
    echo "not-readable"
  fi
  echo "service_manifests:"
  for f in /jci/sm/sm.conf /jci/sm/sm_WCP.conf; do
    if [ -r "$f" ]; then
      echo "$(basename "$f"): present"
      for svc in jciAAPA aap_service jciCARPLAY jcinavi; do
        if grep -q "name=\"$svc\"" "$f"; then echo "  $svc: present"; else echo "  $svc: absent"; fi
      done
      for mod in libpatch-blmjciaapa libpatch-aap_service libpatch-svcjcinavi libpatch-blmjcicarplay; do
        if grep -q "$mod" "$f"; then echo "  $mod: referenced"; else echo "  $mod: not-referenced"; fi
      done
      if grep -q 'LD_PRELOAD' "$f"; then echo "  some_preload_entries: yes"; else echo "  some_preload_entries: no"; fi
    else
      echo "$(basename "$f"): not-readable-or-absent"
    fi
  done
  echo "installed_components:"
  for f in /data_persist/oem-aa-mod/libpatch-blmjciaapa.so /data_persist/oem-aa-mod/libpatch-aap_service.so /data_persist/oem-aa-mod/libpatch-svcjcinavi.so; do
    if [ -f "$f" ]; then echo "$(basename "$f"): present"; else echo "$(basename "$f"): absent"; fi
  done
  echo "processes:"
  for p in aap_service jciAAPA jciCARPLAY; do
    if ps 2>/dev/null | grep "$p" | grep -v grep >/dev/null; then echo "$p: running"; else echo "$p: not-seen"; fi
  done
  echo "nav_sd_service:"
  if [ -e /jci/navi/svcjcinavi.so ]; then echo "present"; else echo "absent"; fi
  echo "Note: presence does not prove Android Auto nav-event delivery or HUD compatibility."
} > "$OUT" || exit 1
echo "Wrote: $OUT"
echo "Review locally before sharing. This script did not alter system configuration."
