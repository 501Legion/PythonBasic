front = 0
end = 1

data_input = int(input("max_num = "))

while True:
    if front > data_input:
        break
    print(front, end = " ")
    tmp = front
    front = end
    end = tmp + end
