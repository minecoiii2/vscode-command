# run ./setup.sh to run this

# make code.py executable
chmod +x ./code.py
# create a symlink at in local bin for code cmd
sudo ln -s "$(pwd)/code.py" /usr/local/bin/code

echo "[TIP]: Run 'code' to get started"