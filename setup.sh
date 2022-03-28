sudo chsh daviddet -s /bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y cmake libnuma-dev ninja-build libboost-program-options-dev
ssh-keygen
cat ~/id_rsa > ~/.ssh/id_rsa
cat ~/id_rsa.pub > ~/.ssh/id_rsa.pub
rm ~/id_rsa*
rm ~/setup.sh
