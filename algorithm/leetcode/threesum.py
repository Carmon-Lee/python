import random
import time
import datetime

if __name__ == '__main__':

    # print(datetime.date.year)
    product_codes = [1000 + i for i in range(100)]
    with open('sql', 'w') as f:
        for i in range(1000001,2000000):
            policy_no = 'P201811280' + str(i).rjust(10, '0')
            client_no = 'C' + str(i).rjust(9, '0')
            product_code = product_codes[random.randint(0, 99)]
            f.write("insert into mcc_policy values('{0}','{1}','{2}');\n".format(policy_no, client_no, product_code))
