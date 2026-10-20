#!/bin/sh
# Mazda Universal HUD Bridge - READ ONLY device preflight v0.1
# No install, remount, restart, LD_PRELOAD, or modification of CMU.
# Usage on CMU: sh usb-preflight.sh > /path/to/USB/hud-preflight.txt
set -u
ROOT="${CMU_ROOT:-}"
f() { printf '%s%s' "$ROOT" "$1"; }
echo "HUD BRIDGE PREFLIGHT 0.1"
echo "READ_ONLY=yes INSTALLABLE=no"
verfile=$(f /jci/version.ini)
if [ -r "$verfile" ]; then
  ver=$(sed -n 's/^JCI_SW_VER=["]*\([^"]*\)["]*/\1/p' "$verfile" | head -1)
  flavor=$(sed -n 's/^JCI_SW_FLAVOR=["]*\([^"]*\)["]*/\1/p' "$verfile" | head -1)
  echo "VERSION=${ver:-unknown}"
  echo "FLAVOR=${flavor:-unknown}"
  case "$ver" in *74.00.324*) echo "FW_FAMILY=match" ;; *) echo "FW_FAMILY=unverified" ;; esac
else
  echo "VERSION=unavailable"
  echo "FW_FAMILY=unverified"
fi
for entry in sm.conf sm_WCP.conf; do
  path=$(f "/jci/sm/$entry")
  if [ ! -r "$path" ]; then echo "CONFIG_$entry=missing"; continue; fi
  echo "CONFIG_$entry=present"
  for svc in jciCARPLAY jciAAPA jcinavi aap_service; do
    if grep -Fq "name=\"$svc\"" "$path"; then
      echo "SERVICE_$entry.$svc=present"
    else
      echo "SERVICE_$entry.$svc=missing"
    fi
  done
  if grep -q 'env_name="LD_PRELOAD"' "$path"; then
    echo "PRELOAD_$entry=present_manual_review"
  else
    echo "PRELOAD_$entry=absent"
  fi
done
for name in blmjcicarplay blmjciaapa svcjcinavi aap_service; do
  path=$(f "/data_persist/oem-aa-mod/libpatch-$name.so")
  if [ -f "$path" ]; then echo "SHIM_$name=present"; else echo "SHIM_$name=absent"; fi
done
for name in aap_system_attributes.xml aap_system_attributes_UCP.xml; do
  path=$(f "/etc/$name")
  if [ -r "$path" ]; then
    if grep -A2 -B2 -i 'subscribe' "$path" | grep -qi 'TRUE'; then
      echo "AA_SUBSCRIPTION_$name=possible_enabled_verify"
    else
      echo "AA_SUBSCRIPTION_$name=unknown_or_disabled"
    fi
  else
    echo "AA_SUBSCRIPTION_$name=unreadable"
  fi
done
echo "NAV_SD_FUNCTIONAL=not_tested"
echo "GREEN_HUD_COMPATIBLE=not_tested"
echo "YANDEX_AA_EVENTS=not_tested"
echo "VBS_ENDPOINT=not_tested"
echo "DECISION=NO_INSTALL_READ_ONLY_DIAGNOSTIC"
