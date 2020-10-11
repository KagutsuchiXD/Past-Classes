#!/usr/bin/env python3

import sys
import csv
from Report import Report
rpt = Report()

alllstofwages = []
alllstofestabs = []
alllstofempls = []

softlstofwages = []
softlstofestabs = []
softlstofempls = []


def scanning(string):
    if string[0].isalpha() or int(string) % 1000 == 0:
        return False
    else:
        return True


# number of unique values
def uniqueinlist(lst):
    d = dict()
    numUnique = 0
    for item in lst:
        if item[1] not in d:
            d[item[1]] = 1
        else:
            d[item[1]] += 1
    for key in d:
        if d[key] == 1:
            numUnique += 1
    return numUnique


# number of distinct values
def numdistinct(lst):
    d2 = dict()
    distinct = 0
    for num in lst:
        d2[num[1]] = 1
    for key in d2:
        distinct += 1
    return distinct


# finding cache county's rank
def getelement1(lst):
    return lst[1]


def cachecorank(lst):
    lst.sort(key=getelement1, reverse=True)
    return findcacheco(lst) + 1


def findcacheco(lst):
    for item in range(len(lst)):
        if lst[item][0] == '49005':
            return item


# Top Rankings for a list
def top5ranks(lst):
    lst.sort(key=getelement1, reverse=True)
    tops = [lst[0], lst[1], lst[2], lst[3], lst[4]]
    return tops


with open(sys.argv[1] + r"/2017.annual.singlefile1.csv", "r") as fullFile:
    csvReader = csv.DictReader(fullFile)
    for row in csvReader:
        if not scanning(row["area_fips"]):
            continue
        else:
            if row["own_code"] == "0" and row["industry_code"] == "10":
                rpt.all.count += 1
                rpt.all.total_pay += int(row["total_annual_wages"])
                alllstofwages.append((row["area_fips"], int(row["total_annual_wages"])))

                rpt.all.total_estab += int(row["annual_avg_estabs"])
                alllstofestabs.append((row["area_fips"], int(row["annual_avg_estabs"])))

                rpt.all.total_empl += int(row["annual_avg_emplvl"])
                alllstofempls.append((row["area_fips"], int(row["annual_avg_emplvl"])))

            elif row["own_code"] == "5" and row["industry_code"] == "5112":
                rpt.soft.count += 1
                rpt.soft.total_pay += int(row["total_annual_wages"])
                softlstofwages.append((row["area_fips"], int(row["total_annual_wages"])))

                rpt.soft.total_estab += int(row["annual_avg_estabs"])
                softlstofestabs.append((row["area_fips"], int(row["annual_avg_estabs"])))

                rpt.soft.total_empl += int(row["annual_avg_emplvl"])
                softlstofempls.append((row["area_fips"], int(row["annual_avg_emplvl"])))
# store unique
rpt.all.unique_pay = uniqueinlist(alllstofwages)
rpt.all.unique_estab = uniqueinlist(alllstofestabs)
rpt.all.unique_empl = uniqueinlist(alllstofempls)

rpt.soft.unique_pay = uniqueinlist(softlstofwages)
rpt.soft.unique_estab = uniqueinlist(softlstofestabs)
rpt.soft.unique_empl = uniqueinlist(softlstofempls)
# store distinct
rpt.all.distinct_pay = numdistinct(alllstofwages)
rpt.all.distinct_estab = numdistinct(alllstofestabs)
rpt.all.distinct_empl = numdistinct(alllstofempls)

rpt.soft.distinct_pay = numdistinct(softlstofwages)
rpt.soft.distinct_estab = numdistinct(softlstofestabs)
rpt.soft.distinct_empl = numdistinct(softlstofempls)
# store per capita avg wage
rpt.all.per_capita_avg_wage = ((rpt.all.total_pay / rpt.all.count) / (rpt.all.total_empl / rpt.all.count))

rpt.soft.per_capita_avg_wage = ((rpt.soft.total_pay / rpt.soft.count) / (rpt.soft.total_empl / rpt.soft.count))
# store cache valley rank
rpt.all.cache_co_pay_rank = cachecorank(alllstofwages)
rpt.all.cache_co_estab_rank = cachecorank(alllstofestabs)
rpt.all.cache_co_empl_rank = cachecorank(alllstofempls)

rpt.soft.cache_co_pay_rank = cachecorank(softlstofwages)
rpt.soft.cache_co_estab_rank = cachecorank(softlstofestabs)
rpt.soft.cache_co_empl_rank = cachecorank(softlstofempls)
# store Top Rankers
rpt.all.top_annual_wages = top5ranks(alllstofwages)
rpt.all.top_annual_avg_emplvl = top5ranks(alllstofempls)
rpt.all.top_annual_estab = top5ranks(alllstofestabs)

rpt.soft.top_annual_wages = top5ranks(softlstofwages)
rpt.soft.top_annual_avg_emplvl = top5ranks(softlstofempls)
rpt.soft.top_annual_estab = top5ranks(softlstofestabs)

with open(sys.argv[1] + r"/area_titles.csv", "r") as areas:
    areaReader = csv.DictReader(areas)
    for row in areaReader:
        for i in range(len(rpt.all.top_annual_wages)):
            if row["area_fips"] == rpt.all.top_annual_wages[i][0]:
                rpt.all.top_annual_wages[i] = (row["area_title"], rpt.all.top_annual_wages[i][1])
        for i in range(len(rpt.all.top_annual_avg_emplvl)):
            if row["area_fips"] == rpt.all.top_annual_avg_emplvl[i][0]:
                rpt.all.top_annual_avg_emplvl[i] = (row["area_title"], rpt.all.top_annual_avg_emplvl[i][1])
        for i in range(len(rpt.all.top_annual_estab)):
            if row["area_fips"] == rpt.all.top_annual_estab[i][0]:
                rpt.all.top_annual_estab[i] = (row["area_title"], rpt.all.top_annual_estab[i][1])

        for i in range(len(rpt.soft.top_annual_wages)):
            if row["area_fips"] == rpt.soft.top_annual_wages[i][0]:
                rpt.soft.top_annual_wages[i] = (row["area_title"], rpt.soft.top_annual_wages[i][1])
        for i in range(len(rpt.soft.top_annual_avg_emplvl)):
            if row["area_fips"] == rpt.soft.top_annual_avg_emplvl[i][0]:
                rpt.soft.top_annual_avg_emplvl[i] = (row["area_title"], rpt.soft.top_annual_avg_emplvl[i][1])
        for i in range(len(rpt.soft.top_annual_estab)):
            if row["area_fips"] == rpt.soft.top_annual_estab[i][0]:
                rpt.soft.top_annual_estab[i] = (row["area_title"], rpt.soft.top_annual_estab[i][1])
print(rpt)
