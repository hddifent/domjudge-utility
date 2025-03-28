#!/bin/bash

usage() { echo "Usage: $0 -f <user_file> [-c <team_cat>] [-l <pass_len>] [-p <prefix>] [-o <team_offset>]"; exit 0; }

prefix="user"
teamcat="7"
teamoff="0"
plen="12"

while getopts ":hl:p:c:o:f:" option; do
    case $option in
        l) plen="${OPTARG}";;
        p) prefix="${OPTARG}";;
        c) teamcat="${OPTARG}";;
        o) teamoff="${OPTARG}";;
        f) ufile="${OPTARG}";;
        *) usage; exit 0;;
    esac
done

if [[ -r $ufile ]]; then
    echo "Using $ufile as original user list file..."
else
    >&2 echo "File $ufile does not exist."
    exit 1
fi

directory="usergen_`date +"%0Y%0m%d_%0H%0M%0S"`"

mkdir $directory

cp $ufile ./$directory
mv ./$directory/$ufile ./$directory/users.txt

cp passgen.py ./$directory
cp teamgen.py ./$directory

cd $directory

python ./passgen.py `grep '^..*$' users.txt | sed -n '$='` $plen
python ./teamgen.py $prefix $teamoff $teamcat

rm passgen.py teamgen.py

touch metadata.txt
echo "DOMjudge teams and accounts (`realpath $0`)" >> metadata.txt
echo "--------------------------------------------------" >> metadata.txt
echo "Files generated on `date +"%B %d, %Y at %0H:%0M:%0S %Z (UTC %:::z)"`" >> metadata.txt
echo "Original user list file: `realpath ../$ufile`" >> metadata.txt
echo "Password length: $plen" >> metadata.txt
echo "Username prefix: $prefix" >> metadata.txt
echo "Team category: $teamcat" >> metadata.txt
echo "Team ID offset: $teamoff" >> metadata.txt