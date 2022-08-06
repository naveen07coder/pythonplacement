def func(start, end):
    S_hour = int(start[-2:])
    S_date = int(start[-5:-3])
    S_month = int(start[-7:-5])
    S_year = int(start[0:4])

    E_hour = int(end[-2:])
    E_date = int(end[-5:-3])
    E_month = int(end[-7:-5])
    E_year = int(end[0:4])

    for y in range(S_year, E_year):
        for m in range(S_month, E_month):
            for d in range(S_date, E_date):
                for hr in range(S_hour, E_hour):

start = "20170317 22"
end = "20170318 02"
func(start, end)