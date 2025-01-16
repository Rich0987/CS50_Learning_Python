def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# dont have main at the bottom "main()"
# do this:
if __name__ == "__main__":       # __name__ special variable
    main()

### open new .py file
### from sayings_custom_module import hello

