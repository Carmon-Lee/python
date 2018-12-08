import re

data_format = {'string': "'{0}'",
               'timestamp': "to_date('{0}','yyyy-mm-dd hh24:mi:ss')"
               }

if __name__ == '__main__':
    sql_str = "select * from mccdata.mcc_call_event where call_event_id=? and created_date=?"
    params = '20180000(String) 2018-09-01 00:00:00(Timestamp)'

    params_parse = params.split(')')
    params_parse = [i.strip() for i in params_parse if i]
    # format
    for para in params_parse:
        data = para.split('(')[1]
        sql_str = sql_str.replace('?', data_format[data.lower()].format(para.split('(')[0]), 1)

    print(sql_str)
