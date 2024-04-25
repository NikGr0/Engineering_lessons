

import datetime
import utils_human.human_class

dt_now = datetime.datetime.now()
current_time = dt_now.time()

#time_obj = datetime.datetime.strptime('01:00:00', '%X')

d = dt_now - datetime.timedelta(hours=1)
#print(time_obj)
print(current_time)
print(d.time())


o_ivan = utils_human.human_class.Human('Ivan', '05.10.1990')
o_kiril = utils_human.human_class.Human('Kiril', '22.07.1988')

two_rota = utils_human.human_class.Rota('2 rota')
five_polk = utils_human.human_class.Polk('5 polk')

two_rota.add_rota([o_kiril, o_ivan])
five_polk.add_rota_v_polk(two_rota)

two_rota.print_all_rota()
#print(o_ivan.print_all_inf())