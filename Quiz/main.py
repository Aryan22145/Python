import subprocess

print("WELCOME")
print("""
1.Python
2.JavaScript
3.Java
4.C Language
5.C++ 
6.Kotlin
7.Rust
8.GO (GOLANG)
9.Swift
10.Typescript
""")

choice = int(input("Enter your choice: "))
try:
    if choice == 1:
        subprocess.run(['python', "py_implementation.py"])
    elif choice == 2:
        subprocess.run(['python', "js_implementation.py"])
    elif choice == 3:
        subprocess.run(['python', "java_implementation.py"])
    elif choice == 4:
        subprocess.run(['python', "c_implementation.py"])
    elif choice == 5:
        subprocess.run(['python', "cplusplus_implementation.py"])
    elif choice == 6:
        subprocess.run(['python', "kotlin_implementation.py"])
    elif choice == 7:
        subprocess.run(['python', "rust_implementation.py"])
    elif choice == 8:
        subprocess.run(['python', "go_implementation.py"])
    elif choice == 9:
        subprocess.run(['python', "swift_implementation.py"])
    elif choice == 10:
        subprocess.run(['python', "typescript_implementation.py"])
    else:
        print("Invalid input. Enter an appropriate input")
except:
    print("Error occurred. Please try again!!")
