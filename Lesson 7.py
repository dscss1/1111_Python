import datetime
import os
import shutil


# d1 = datetime.datetime.now()
# dt = datetime.datetime(2024, 11, 12,16,45)
# print(type(dt))
# print(dt)
# print(dt.date())
# print(dt.time())
# print(datetime.datetime.now())
# print(datetime.datetime.today())
#
# d = datetime.date(2024, 5, 12)
# t = datetime.time(4,6,8,34345)
# dt1 = datetime.datetime.combine(d, t)
# print(t)
# print(dt1)
#
# dt = dt.replace(day=5)
# print(dt)
#
# d2 = datetime.datetime.now()
# print(d1)
# print(d2)
# print(d2-d1)
#
# print(d.weekday())
# print(d.isoweekday())
#
# tst = d2.timestamp()
# print(tst)
# print(datetime.datetime.fromtimestamp(tst))
#
# path = "C:\\Users\\gololobov\\Downloads\\P33\\Lesson 2\\styles.css"
# ts = os.path.getatime(path)
# df = datetime.datetime.fromtimestamp(ts)
# print(df)
# st = d2.strftime('%d %B %Y %H:%M, %A')
# print(st)


def spy2(path, res_path):
    path = os.path.normpath(path)
    res_path = os.path.normpath(res_path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_date = os.path.getmtime(f"{dirpath}\\{file}")
            norm_date = datetime.datetime.fromtimestamp(file_date)
            str_date = norm_date.strftime("%d.%m.%Y")

            if os.path.isdir(f"{res_path}\\{str_date}"):
                shutil.copy(f"{dirpath}\\{file}", f"{res_path}\\{str_date}\\{file}")
            else:
                os.mkdir(f"{res_path}\\{str_date}")
                shutil.copy(f"{dirpath}\\{file}", f"{res_path}\\{str_date}\\{file}")

path = "C:\\Users\\gololobov\\Downloads\\P33\\Lesson 4"
res_path = "C:\\555"
spy2(path, res_path)

