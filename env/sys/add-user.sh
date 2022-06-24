#!/bin/bash -xe

groupadd supersudo && echo "%supersudo ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/supersudo
adduser --disabled-password --gecos treeseverywhere treeseverywhere && usermod -a -G supersudo treeseverywhere && mkdir -p /home/treeseverywhere/.ssh
echo -e "Host github.com\n\tStrictHostKeyChecking no\n" > /home/treeseverywhere/.ssh/config
sudo chown -R treeseverywhere:treeseverywhere /home/treeseverywhere
sudo chmod 600 /home/treeseverywhere/.ssh/*