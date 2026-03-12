#!/bin/bash

read  -p "Введите массу (в кг): " WEIGHT

read -p "Введите рост (в м): " HEIGHT

BMI=$(echo "scale=2; $WEIGHT / ($HEIGHT * $HEIGHT)" | bc)

echo "Ваш ИМТ: $BMI"
