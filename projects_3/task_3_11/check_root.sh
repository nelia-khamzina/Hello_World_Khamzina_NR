#!/bin/bash

check_root() {
	if [ $EUID -ne 0 ]; then
		echo "Ошибка: скрипт запущен не от имени суперпользователя"
		exit 1
	fi
}
check_root
