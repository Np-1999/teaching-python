def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print("In exception")
    finally:
        print("Divded!!!")
    


print(divide(10,2))
print(divide(10,3))