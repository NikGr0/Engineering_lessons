list1 = [1, 2, 3, 4, 'hello!', 5, 6, 7]

def list_division(local_list: list):
    l_result = list()
    for one_element in local_list:
        try:
            l_result.append(100/(one_element-2))
        except ZeroDivisionError:
            print('na 0 delit nelza')
            print(one_element)
        except Exception as e:
            print(e)

            print(one_element)
    return l_result

print(list_division(list1))
