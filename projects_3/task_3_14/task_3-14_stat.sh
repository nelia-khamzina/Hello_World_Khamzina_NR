#!/bin/bash

awk '{sum += $2} END {print sum}' student.txt
awk '{sum += $2; n++} END {print sum/n}' student.txt
awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' student.txt
