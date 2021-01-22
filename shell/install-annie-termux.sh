echo ""
echo ""
echo "[*]This Script Will Install Annie On Termux"
echo ""
echo ""
pkg in ffmpeg wget -y
wget https://github.com/iawia002/annie/releases/download/0.10.3/annie_0.10.3_Linux_ARM64.tar.gz
tar -zxvf annie_0.10.3_Linux_ARM64.tar.gz
cp annie ~/../usr/bin/
echo ""
echo ""
echo "[!]Succeeded Installing Annie.Start With Annie"
rm annie annie_0.10.3_Linux_ARM64.tar.gz