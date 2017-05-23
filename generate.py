import random as r
import csv
from datetime import date, timedelta


def random_school_name():
    locations = ["North", "South", "East", "West", "Central", "Outer"]
    names = ["Bucks", "Washington", "Jefferson", "Lincoln", "Truman", "Roosevelt", "King", "Arthur", "York"]
    types = ["H.S.", "M.S.", "High"]

    name = r.choice(locations) + " " + r.choice(names) + " " + r.choice(types)
    return name


def generate_set(nschools):
    r.seed(2128559118 + nschools)

    schools = set()
    while(len(schools) < nschools):
        schools.add(random_school_name())
    schools = list(schools)

    enrollment = dict()
    attendance = dict()
    for sc in schools:
        enrollment[sc] = r.randint(120, 500)
        attendance[sc] = r.uniform(0.7, 0.95)

    # ToDo: I should put in holiday math here better.
    s = date(2015, 9, 3)
    t = timedelta(days=1)
    days = []
    while(len(days) < 180):
        if(s.weekday() < 5):
            days.append(s)
        s = s + t

    with open("datasets/lunch_{}.csv".format(nschools), 'w', newline='') as csvfile:
        cw = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        cw.writerow(["Date", "School", "Enrollment", "Attendance", "Hamburger", "Pizza", "HotDog", "Skipped"])
        for d in days:
            for s in schools:
                e = enrollment[s]
                p = int(e * r.uniform(attendance[s], 1.0))
                hmp = r.uniform(0, 0.6)
                pzp = r.uniform(0, min(1 - hmp, 0.5))
                hdp = r.uniform(0, 1 - hmp - pzp)

                hm = (int)(hmp * p)
                pz = (int)(pzp * p)
                hd = (int)(hdp * p)
                sk = p - hm - pz - hd

                cw.writerow([d, s, e, p, hm, pz, hd, sk])

    return True


if __name__ == "__main__":
    generate_set(4)
    generate_set(10)
    generate_set(17)
