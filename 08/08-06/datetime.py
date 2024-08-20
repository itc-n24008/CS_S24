from datetime import datetime
t_str = '20180105120130'
dt = datetime.strptime(t_str, "%Y%m%d%H%M%S")
print(dt)
print(dt.strftime("%Y%m%d%H%M%S"))
