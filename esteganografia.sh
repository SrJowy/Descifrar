#!/bin/bash

sudo apt-get install unzip
sudo apt-get install stegosuite

unzip imagen.zip
len=$(ls -l . | egrep -c '*.jpg')
h='e5ed313192776744b9b93b1320b5e268'
i=1
while [ $i -le $len ]
do
    t="imagen$i.jpg"
    ls | egrep $t > log.txt
    if [ $? == 0 ]
    then
        hash=$(md5sum $t | cut -f 1 -d ' ')
        if [ $hash = $h ]
        then 
            stegosuite $t
        fi
    fi
    let i=$i+1
done
rm log.txt
rm *.jpg