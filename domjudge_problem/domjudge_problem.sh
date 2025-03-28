#!/bin/bash

usage() {
    echo "Usage: $0 <problem_name> <mem_limit> <time_limit> <problem_text> [<short_name>]"
    exit 1
}

if [[ -r $4 ]]; then
    echo ""
else
    echo "$4 does not exist"
    exit 1
fi

sname="problem_`date +"%0Y%0m%d_%0H%0M%0S"`"

if (( $# == 5 )); then
    sname=$5
fi

mkdir $sname
mkdir $sname/data
mkdir $sname/data/sample
mkdir $sname/data/secret

cp $4 ./$sname
mv ./$sname/$4 ./$sname/problem.pdf

python problem_metadata_gen.py "$1" $2 $3
mv ./problem.yaml ./$sname
mv ./domjudge-problem.ini ./$sname
