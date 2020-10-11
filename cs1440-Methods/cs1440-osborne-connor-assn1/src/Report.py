# DO NOT MODIFY THIS FILE!!!

class EmploymentDataSet():
    def __init__(self):
        self.count                   = 0

        self.total_pay               = 0
        self.unique_pay              = 0
        self.distinct_pay            = 0
        self.median_pay              = 0
        self.per_capita_avg_wage     = 0
        self.cache_co_pay_rank       = 0

        self.total_estab             = 0
        self.unique_estab            = 0
        self.distinct_estab          = 0
        self.median_estab            = 0
        self.cache_co_estab_rank     = 0

        self.total_empl              = 0
        self.unique_empl             = 0
        self.distinct_empl           = 0
        self.median_empl             = 0
        self.cache_co_empl_rank      = 0

        # These are lists of pairs (2-tuples): 0th element is a FIPS area name, 1th element is a numeric value
        self.top_annual_wages        = []
        self.top_annual_avg_emplvl   = []
        self.top_annual_estab        = []



class Report():
    def __init__(self):
        self.all  = EmploymentDataSet()
        self.soft = EmploymentDataSet()

    def enumList(self, l, rev=False, money=False):
        res = []
        if rev:
            i = len(l)
            for e in l:
                res.append(f"{i:>2}. {e[0]:<36} {'$' if money else ''}{e[1]:,}")
                i -= 1
        else:
            i = 0
            for e in l:
                res.append(f"{i+1:>2}. {e[0]:<36} {'$' if money else ''}{e[1]:,}")
                i += 1
        return "\n".join(res)


    def __str__(self):
        return f"""
[============]
[Final Report]
[============]

Statistics over all industries in 2017:
=========================================================
Count of FIPS areas in report        {self.all.count:,}

Gross annual wages                   ${self.all.total_pay:,}
Count of unique Annual Wages         {self.all.unique_pay:,}
Count of distinct Annual Wages       {self.all.distinct_pay:,}
Per capita average wage              ${self.all.per_capita_avg_wage:,.2f}
Cache County's Rank                  #{self.all.cache_co_pay_rank:,}

Gross number of establishments       {self.all.total_estab:,}
Count of unique num of establ.       {self.all.unique_estab:,}
Count of distinct num of establ.     {self.all.distinct_estab:,}
Cache County's Rank                  #{self.all.cache_co_estab_rank:,}

Gross annual employment level        {self.all.total_empl:,}
Count of unique employment levels    {self.all.unique_empl:,}
Count of distinct employment levels  {self.all.distinct_empl:,}
Cache County's Rank                  #{self.all.cache_co_empl_rank:,}

Top {len(self.all.top_annual_wages)} FIPS areas by Total Annual Wages
---------------------------------------------------------
{self.enumList(self.all.top_annual_wages, money=True)}

Top {len(self.all.top_annual_estab)} FIPS areas by Annual Average # of Establishments
---------------------------------------------------------
{self.enumList(self.all.top_annual_estab)}

Top {len(self.all.top_annual_avg_emplvl)} FIPS areas by Annual Average Employment Level
---------------------------------------------------------
{self.enumList(self.all.top_annual_avg_emplvl)}



Statistics over the software publishing industry in 2017:
=========================================================
Count of FIPS areas in report        {self.soft.count:,}

Gross annual wages                   ${self.soft.total_pay:,}
Count of unique Annual Wages         {self.soft.unique_pay:,}
Count of distinct Annual Wages       {self.soft.distinct_pay:,}
Per capita average wage              ${self.soft.per_capita_avg_wage:,.2f}
Cache County's Rank                  #{self.soft.cache_co_pay_rank:,}

Gross number of establishments       {self.soft.total_estab:,}
Count of unique num of establ.       {self.soft.unique_estab:,}
Count of distinct num of establ.     {self.soft.distinct_estab:,}
Cache County's Rank                  #{self.soft.cache_co_estab_rank:,}

Gross annual employment level        {self.soft.total_empl:,}
Count of unique employment levels    {self.soft.unique_empl:,}
Count of distinct employment levels  {self.soft.distinct_empl:,}
Cache County's Rank                  #{self.soft.cache_co_empl_rank:,}

Top {len(self.soft.top_annual_wages)} FIPS areas by Total Annual Wages
---------------------------------------------------------
{self.enumList(self.soft.top_annual_wages, money=True)}

Top {len(self.soft.top_annual_estab)} FIPS areas by Annual Average # of Establishments
---------------------------------------------------------
{self.enumList(self.soft.top_annual_estab)}

Top {len(self.soft.top_annual_avg_emplvl)} FIPS areas by Annual Average Employment Level
---------------------------------------------------------
{self.enumList(self.soft.top_annual_avg_emplvl)}
"""
