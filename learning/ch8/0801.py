class Pair:
    def __init__(self, x, y):
        """
        :type y: object
        """
        self.x = x
        self.y = y

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)

class MosquitoKiller:
    def __init__(self,brand,price) -> None:
        self.price=price
        self.brand=brand

    def __repr__(self) -> str:
        return "MosquitoKiller({0.brand!r},{0.price!r})".format(self)

    def __str__(self) -> str:
        return 'm({0.brand!s},{0.price!s})'.format(self)


_formats={
    'ymd':'{d.year}-{d.month}-{d.day}',
    'mdy':'{d.month}/{d.day}/{d.year}'
}
class Date:

    def __init__(self,year,month,day) -> None:
        self.year=year
        self.month=month
        self.day=day

    def __format__(self, code) -> str:
        if code=='':
            code='ymd'
        return _formats[code].format(d=self)


p = Pair(3, 4)
d=Date(2018,9,31)
print(format(d,'mdy'))
print('The date of today is:{:ymd}'.format(d))
print('The date of today is:{:mdy}'.format(d))
# mk=MosquitoKiller('lanju',20)
# print(mk)
# with p as pp:
#     eval(repr(p))
#     print(p)
#     print(__name__)
