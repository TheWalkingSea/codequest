from typing import Union, List, Optional, Iterable, Callable, Tuple
import sys
import datetime


def getLines(lines: Optional[int]=0) -> Union[str, List[str]]:
    if lines == 0: return sys.stdin.readline().rstrip()
    ret = list()
    for _i in range(lines):
        ret.append(getLines())
    return ret

def getNthDay(month: int, day: int, nthDay: int, yearDelta: Optional[int]=0) -> Callable[[int], datetime.date]: # Day is mon = 1, sun = 7
    def e(year: int) -> datetime.date:
        year += yearDelta
        dt = datetime.date(year, month, 1)
        for _i in range(nthDay):
            while dt.weekday() != day-1:
                dt += datetime.timedelta(days=1)
        return dt
    return e


def getNthLastDay(month: int, day: int, nthLastDay: int) -> Callable[[int], datetime.date]: # Day is mon = 1, sun = 7
    def e(year: int) -> datetime.date:
        dt = datetime.date(year, month, 31)
        for _i in range(nthLastDay):
            while dt.weekday() != day-1:
                dt -= datetime.timedelta(days=1)
        return dt
    return e

TABLE = {
    "Smith": {
        "tz": -7
    },
    "Sprey": {
        "tz": -5,
        "DSTstart": (getNthDay(3, 7, 2), datetime.time(hour=2)),
        "DSTend": (getNthDay(11, 7, 1), datetime.time(hour=2))
    },
    "Anderson": {
        "tz": 0,
        "DSTstart": (getNthLastDay(3, 7, 1), datetime.time(hour=1)),
        "DSTend": (getNthLastDay(10, 7, 1), datetime.time(hour=2)),
    },
    "Bolade": {
        "tz": 1
    },
    "Hassan": {
        "tz": 2
    },
    "Agarwal": {
        "tz": 5.5
    },
    "Sato": {
        "tz": 9
    },
    "Thomas": {
        "tz": 10,
        "DSTstart": (getNthDay(10, 7, 1, yearDelta=-1), datetime.time(hour=2)),
        "DSTend": (getNthDay(4, 7, 1), datetime.time(hour=3))
    }
}


def inDST(lastName: str, date: datetime.date, time: datetime.time) -> bool:
    if "DSTstart" not in TABLE[lastName].keys():
        return False
    time1 = datetime.datetime.combine(date, time)
    timeStart = datetime.datetime.combine(TABLE[lastName]["DSTstart"][0](date.year), TABLE[lastName]["DSTstart"][1])
    timeEnd = datetime.datetime.combine(TABLE[lastName]["DSTend"][0](date.year), TABLE[lastName]["DSTend"][1])
    # if lastName == "Thomas":
        # print(time1, timeStart, timeEnd, time1 >= timeStart, time1 < timeEnd, sep=" || ")
    if time1 >= timeStart and time1 < timeEnd:
        return True
    return False



def convertTz(lastName: str, date: datetime.date, time: datetime.time) -> Tuple[datetime.date, datetime.time]: # Converts to UTC time
    dt = datetime.datetime.combine(date, time)
    td = datetime.timedelta(hours=TABLE[lastName]["tz"])
    dt -= td # UTC TIME
    if inDST(lastName, dt.date(), dt.time()):
        dt -= datetime.timedelta(hours=1)
    return (dt.date(), dt.time())

# def addTime(time: datetime.time, dt: datetime.timedelta) -> datetime.time:
#     return (datetime.datetime.combine(datetime.datetime.today(), time) + dt).time()


def toTz(lastName: str, date: datetime.date, time: datetime.time) -> Tuple[datetime.date, datetime.time]: # Converts to UTC time
    dt = datetime.datetime.combine(date, time)
    td = datetime.timedelta(hours=TABLE[lastName]["tz"])
    dt += td # UTC TIME
    # print(lastName, inDST(lastName, dt.date(), dt.time()), sep=" !!!!!! ")
    if inDST(lastName, dt.date(), dt.time()):
        dt += datetime.timedelta(hours=1)
    return (dt.date(), dt.time())

def convertDt(dt: datetime.datetime) -> str:
    return dt.strftime('%Y-%m-%d %H:%M')


def main(cin: str) -> Iterable[str]:
    lastName, date, time, *names = cin.split(" ")
    names.append(lastName)
    names.sort()
    # print(names)
    date = datetime.date(*map(int, date.split("-")))
    time = datetime.time(*map(int, time.split(":")))
    yield f"{lastName}'s Meeting:"
    date, time = convertTz(lastName, date, time) # UTC TIME FOR MEETING
    # print("AAAA", date, time, sep=" ---- ")
    for name in names:
        d2date, d2time = toTz(name, date, time) # Convert to local time
        yield f"{name} {convertDt(datetime.datetime.combine(d2date, d2time))}"



if __name__ == "__main__":
    testCases = int(getLines())
    with open("out.txt", "a") as f:
        for _i in range(testCases):
            for out in main(getLines()):
                f.writelines(out + "\n")
                print(out)