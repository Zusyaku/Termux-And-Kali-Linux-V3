echo "Menghapus YOUTUBE-DOWNLOADER yang lama.."
cd ..
rm -rf YOUTUBE-DOWNLOADER
sleep 2
echo "Menginstall YOUTUBE-DOWNLOADER yang baru.."
git clone https://github.com/Rizxyu/YOUTUBE-DOWNLOADER > ./.tmp-ytdl-install.txt
rm ./.tmp-ytdl-install.txt
sleep 1
cd YOUTUBE-DOWNLOADER
echo "Sukses!"
