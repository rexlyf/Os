#!/usr/bin/env bash
iso_name="SupremeOS"
iso_label="SUPREME_OMEGA"
iso_publisher="Nemi <Supreme Exchange CEO>"
iso_application="Omniscient Sovereign OS"
iso_version="1.0-Omega"
install_dir="supreme"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito' 'uefi-ia32.grub.esp' 'uefi-x64.grub.esp')
arch="x86_64"
pacman_conf="pacman.conf"

file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root/supreme_core/main.py"]="0:0:755"
  ["/root/supreme_core/eyes.py"]="0:0:755"
  ["/root/supreme_core/brain.py"]="0:0:755"
  ["/root/supreme_core/hands.py"]="0:0:755"
  ["/root/supreme_core/auth.py"]="0:0:755"
  ["/root/supreme_core/genesis.py"]="0:0:755"
  ["/root/supreme_core/supreme_bot.py"]="0:0:755"
  ["/root/supreme_core/alpha_dev.py"]="0:0:755"
  ["/root/supreme_core/security_core.py"]="0:0:755"
  ["/etc/systemd/system/supreme.service"]="0:0:644"
)
