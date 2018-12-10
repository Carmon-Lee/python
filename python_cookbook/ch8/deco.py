def myfun1(fun):
    def wrapper():
        print("before decoratino")
        fun()
        print("after decoration")

    return wrapper


@myfun1
def fun1():
    print("this is the main function")


fun1()
fun1()
