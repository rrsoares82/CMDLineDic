#!/bin/sh
echo "pos installation checking ..."
grep alias /etc/profile.d/00-rundict.sh
if [ $? ]; then
  echo alias rundict='"python3 /opt/CMDLineDic/rundict.py"' > /etc/profile.d/00-rundict.sh
fi
