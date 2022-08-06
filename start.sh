if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PachGit/cbautofilter.git /cbautofilter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /cbautofilter
fi
cd /cbautofilter
pip3 install -U -r requirements.txt
echo "Starting....🔥"
python3 bot.py
