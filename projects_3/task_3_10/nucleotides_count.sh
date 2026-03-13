#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
for file in *.fasta; do
    if [ ! -s "$file" ]; then
	continue
    fi
    SEQ=$(grep -v "^>" "$file" | tr -d '\n')
    NUM_A=$(grep -o "A" | wc -l)
    NUM_T=$(grep -o "T" | wc -l)
    NUM_G=$(grep -o "G" | wc -l)
    NUM_C=$(grep -o "C" | wc -l)
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$NUM_A" "$NUM_A" "$NUM_A" "$NUM_A"
done
