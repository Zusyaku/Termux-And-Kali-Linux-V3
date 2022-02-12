cd
cd
rm -rf AllHackingTools
echo "Restoring AllHackingTools backup..."
cd /sdcard/ && cp -r AllHackingTools /data/data/com.termux/files/home/
cd && bash AllHackingTools/.settings/RestoreAllHackingToolsBackup.sh
echo "successfully restored backup in: sdcard..."
sleep 1
echo "If the backup did not restore AllHackingTools then the backup was not found!"
sleep 1
echo "Because the backup is not in: sdcard then we cannot restore AllHackingTools. Or there was no backup"
cd
cd
cd AutoUpdateMyTools
cd logs
cp restoring-log /data/data/com.termux/files/home/AllHackingTools/.logs/
cp restoring-log-wifi /data/data/com.termux/files/home/AllHackingTools/.logs/
 
