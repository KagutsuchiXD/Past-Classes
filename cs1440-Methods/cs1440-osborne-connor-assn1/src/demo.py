from Report import Report
r = Report()

r.all.count                   = 0

## Shouldn't these computed stats agree with the fips area US000?
r.all.total_pay               = 1
r.all.unique_pay              = 2
r.all.distinct_pay            = 3

r.all.total_estab             = 4
r.all.unique_estab            = 5
r.all.distinct_estab          = 6

r.all.total_empl              = 7
r.all.unique_empl             = 8
r.all.distinct_empl           = 9

r.all.per_capita_avg_wage     = 10 / 11

r.all.top_annual_wages        = [('Reagan', 12), ('Julian', 11), ('Ivan', 10), ('Shirley', 9), ('Reese', 8)]
r.all.cache_co_pay_rank       = 13

r.all.top_annual_avg_emplvl   = [('Declan', 14), ('Hailey', 13), ('Caleb', 12), ('Colton', 11), ('Savannah', 10)]
r.all.cache_co_empl_rank      = 15

r.all.top_annual_estab        = [('Daniela', 16), ('Kenneth', 15), ('Christine', 14), ('Charlotte', 13), ('Natalie', 12)]
r.all.cache_co_estab_rank     = 17




r.soft.count                  = 18

## Shouldn't these computed stats agree with the fips area US000?
r.soft.total_pay              = 19
r.soft.unique_pay             = 20
r.soft.distinct_pay           = 21

r.soft.total_estab            = 22
r.soft.unique_estab           = 23
r.soft.distinct_estab         = 24

r.soft.total_empl             = 25
r.soft.unique_empl            = 26
r.soft.distinct_empl          = 27

r.soft.per_capita_avg_wage    = 28 / 29

r.soft.top_annual_wages       = [('Harper', 30), ('Kylee', 29), ('Joshua', 28), ('Delaney', 27), ('Landon', 26)]
r.soft.cache_co_pay_rank      = 31

r.soft.top_annual_avg_emplvl  = [('Adrianna', 32), ('Alyssa', 31), ('Kayden', 30), ('Frank', 29), ('William', 28)]
r.soft.cache_co_empl_rank     = 33

r.soft.top_annual_estab       = [('Axel', 34), ('Ruth', 33), ('Erik', 32), ('Adam', 31), ('Brenda', 30)]
r.soft.cache_co_estab_rank    = 35

print(r)
