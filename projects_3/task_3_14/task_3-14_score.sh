#!/bin/bash

awk '$2 > 80 {print $0}' student.txt
awk '$2 < 70 {print $0}' student.txt
awk -F ","  'NR == 1' student.txt
