#!/bin/bash

user=$(logname)
day=$(date +%d)
month=$(date +%m)
year=$(date +%y)
st=$day-$month-$year

mkdir /var/tmp/Backups/$st
ayer=$(date -d yesterday +%d-%m-%y)
dir=/var/tmp/Backups/$ayer

if [ -d "$dir" ]
then
    echo "Se realizará copia incremental"
    mysqldump --user root --password SGGSI > /home/$user/Escritorio/Seguridad/SGSSI.sql
    rsync -avhb --delete --compare-dest=$dir /home/$user/Escritorio/Seguridad/ /var/tmp/Backups/$st
else
    echo "Se realizará copia completa"
    mysqldump --user root --password SGGSI > /home/$user/Escritorio/Seguridad/SGSSI.sql
    rsync -av /home/$user/Escritorio/Seguridad/ /var/tmp/Backups/$st
fi