count = 0
def increment():
    global count
    count +=1
    print(f"count inside the function {count}    !")

increment()
increment()

print(f"outside the function {count}!")

