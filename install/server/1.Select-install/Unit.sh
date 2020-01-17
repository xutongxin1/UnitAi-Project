sudo apt install -y git
git clone https://github.com/baidu/unit-dmkit.git
cd unit-dmkit/
sh deps.sh ubuntu
mkdir _build &&  cd _build && cmake .. && make