#!/bin/bash

for i in {1..10}; do
        touch "test$i.txt"
done
NUM=10
while [ $NUM -gt 0 ]; do
        rm "test$NUM.txt"
        let "NUM--"
done
