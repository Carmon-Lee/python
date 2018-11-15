remap={
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\n'):' '
}
import time

s='python\tis\nwonderful\f'

if __name__ == '__main__':

    t1=time.time()
    s=['aaa']*10000000
    # print(s)
    # s0=''
    # for i in s:
    #     s0+=i
    s0=''.join(s)

    t2=time.time()
    print(t2-t1)
    vars()
