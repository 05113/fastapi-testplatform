import request
import json
import re

class AssertCase():


    def get_actual_vaule(self,response , assert_key ):
        key_list = assert_key.split('.')
        if key_list[0] != 'response':
            actual_value = 'assert_case is error'
        elif key_list[1] == 'status_code':
            actual_value = response.status_code
        else:
            not_response_key_list = key_list[1:]
            response = json.loads(response.text)
            for item in not_response_key_list:
                if ('[' in item):
                    key_indexarr = item.split('[')
                    key = key_indexarr[0]
                    keyindex = int(key_indexarr[1][:-1])
                    # todo 后边加数组越界异常捕获
                    response = response[key][keyindex]
                else:
                    response = response[item]
            actual_value = response
        return actual_value

    def equal_comparison(self,actual_value , assert_value):
        if actual_value == assert_value:
            return True
        else:
            return False

assert_case_class = AssertCase()