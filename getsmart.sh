#!/bin/bash

# Kiểm tra xem số lượng tham số truyền vào là đúng hay không
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <value>"
    exit 1
fi

# Lấy giá trị của tham số truyền vào
value="$1"

# Sử dụng giá trị đó trong lệnh

smartctl -a "/dev/$value"
