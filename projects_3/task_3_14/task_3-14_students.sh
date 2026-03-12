#!bin/bash

awk '{print $1}' student.txt
awk '{print $2}' student.txt
awk '{print NR, $1}' student.txt
