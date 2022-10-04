#%%Functions

#Imports
import calendar
import numpy as np
import math as m

#Functions
def discharge_conv(rate):
    #Conver to L/day
    #Input rate in m3/s
    #Output in l/day
    out = rate * 86400 * 1000
    return out

def month_string_to_number(string):
    #Convert string names for months to numeric
    m = {
        'jan':1,
        'feb':2,
        'mar':3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12}
    s = string.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

def day_multiplier(Monthly_discharge, year):
    #Provide an average monthly output for discharge

    month = Monthly_discharge[0]
    rate = Monthly_discharge[1]

    if isinstance(rate, str) is True:
        return 0
    if isinstance(rate, (int, float)) is False:
        raise ValueError('Not a valid rate')

    else:
        try:
            month_num = month_string_to_number(month)
            days = calendar.monthrange(year,month_num)[1]

            day_out = discharge_conv(rate)

            month_out = days * day_out
            return month_out
        except:
            return print('None Value Entered')

def total_year_discharge(station):
    discharge = [day_multiplier(i) for i in station]
    return sum(discharge)

def dis_difference(year_A, year_B):
    #Calculate the difference in discharge between two streams
    if len(year_A) < 12:
        return ValueError('Not a full year')
    if len(year_B) < 12:
        return ValueError('Not a full year')
    if len(year_A) != len(year_B):
        return ValueError('Lists must be equal length')

    months = [i[0] for i in year_A]

    diff = [year_A[i][1] - year_B[i][1] for i in np.arange(0,12)]

    out = [(months[i],diff[i]) for i in np.arange(0,12)]

    return out

def month_dis_liters(discharge, year):
    #Calculate discharge for that month
    dis_month = [day_multiplier(i, year) for i in discharge]

    for i in np.arange(0,len(dis_month)):
        if float(dis_month[i]) < 0:
            dis_month[i] = 0
        else:
            pass
    return dis_month

def percent_treated_per_month(monthly_stream_discharge, treatment_capacity, year):
    #Calculate water treated per month based on max treatment capacity

    #Days in each month for a given year
    month_treatment_potential = []
    for i in np.arange(1,13):
        days_tupple = calendar.monthrange(year,i)
        treatment_p = days_tupple[1] * treatment_capacity
        month_treatment_potential.append(treatment_p)

    summary_results = []
    for i in np.arange(0,len(monthly_stream_discharge)):

        if monthly_stream_discharge[i] == 0:
            treated_percent = 0
            untreated = 0
            treated = 0

            summary_results.append((treated_percent,treated,untreated))

        else:
            untreated = monthly_stream_discharge[i] - month_treatment_potential[i]

            if untreated > 0:
                treated = month_treatment_potential[i]
            else:
                treated = month_treatment_potential[i] + untreated

            treated_percent = (treated/monthly_stream_discharge[i]) * 100
            treated_out = round(treated_percent,2)

            if treated < 0:
                treated = 0

            summary_results.append((treated_out,treated,round(untreated,2)))


    return summary_results

def percent_treated(stream_discharge, treatment_capacity, year):
    if calendar.isleap(year) is True:
        days = 366
    else:
        days = 365

    if isinstance(treatment_capacity, int) is False:
        return ValueError('Treatment_capacity must be integer value')

    t = treatment_capacity * days
    percent_t = (t/stream_discharge) * 100

    return round(percent_t,2)

def mm_to_dis(annual_yield, drainage_area, per_Sec = True):
    area = drainage_area * 1000000
    rate = annual_yield * 0.001

    if per_Sec is True:
        discharge = (area * rate)/365
        discharge = discharge/86400
    else:
        discharge = (area * rate)/365
    return discharge

def month_dis_to_instant(discharge,month, year):
    days = calendar.monthrange(year,month)[1]
    out = discharge * 0.001
    out = (out/days)/86400
    if out < 0:
        return 0
    else:
        return out

def smimming_pool_conv(volume_of_water):
    out = round((volume_of_water/2500000),2)
    return print('%s Olympic Sized Swimming Pools' % out)


#%%Discharge Data

#Data

#2020 Data

LC_LCDSSLCC = [('January',0),
               ('February',0),
               ('March',0.44),
               ('April', 1.01),
               ('May', 4.88),
               ('June', 5.43),
               ('July',1.77),
               ('August',0.82),
               ('September',0.67),
               ('October', 0.60),
               ('November', 0.79),
               ('December',0.45)]

LC_WLC = [('January',0.03),
               ('February',0.03),
               ('March',0.03),
               ('April',0.03),
               ('May',0.08),
               ('June',0.17),
               ('July',0.09),
               ('August',0.05),
               ('September',0.04),
               ('October',0.04),
               ('November',0.04),
               ('December',0.04)]

LC_DC3 = [('January',0.02),
               ('February',0.02),
               ('March',0.02),
               ('April',0.16),
               ('May',0.35),
               ('June',0.31),
               ('July',0.11),
               ('August',0.05),
               ('September',0.07),
               ('October',0.02),
               ('November',0.02),
               ('December',0.02)]

#https://www.teck.com/media/Permit-107517-Annual-Water-Quality-Monitoring-Report,2017-(March-31,2018).pdf pg 152

LC_SLC_2017 = [('January',0.19),
               ('February', 0.19),
               ('March', 0.12),
               ('April', 0.17),
               ('May', 2.17),
               ('June', 1.87),
               ('July', 0.70),
               ('August', 0.26),
               ('September', 0.22),
               ('October', 0.15),
               ('November', 0.11),
               ('December', 0.09)]

LC_LCDSSLCC_2017 = [('January',0),
               ('February', 0),
               ('March', 0.58),
               ('April', 0.71),
               ('May', 5.66),
               ('June', 6.70),
               ('July', 2.52),
               ('August', 1.55),
               ('September', 1.31),
               ('October', 1.24),
               ('November', 1.33),
               ('December', 0)]

LC_SLC_2020 = [('January',0),
               ('February', 0.09),
               ('March', 0.09),
               ('April', 0),
               ('May', 3.59),
               ('June', 4.41),
               ('July', 1.28),
               ('August', 0.70),
               ('September', 0.52),
               ('October', 0.59),
               ('November', 0.61),
               ('December', 0)]

LC_LCDSSLCC_2020 = [('January',0),
               ('February', 0),
               ('March', 0.44),
               ('April', 1.01),
               ('May', 4.48),
               ('June', 5.43),
               ('July', 1.77),
               ('August', 0.82),
               ('September', 0.67),
               ('October', 0.60),
               ('November', 0.79),
               ('December', 0.45)]

LC_LCDSSLCC_2020_Summary_Chart = [('January',0),
               ('February', 0),
               ('March', 0.43),
               ('April', 1.01),
               ('May', 4.48),
               ('June', 10.1),
               ('July', 2.25),
               ('August', 0.82),
               ('September', 0.64),
               ('October', 0.60),
               ('November', 0.77),
               ('December', 0.41)]

#https://www.teck.com/media/LCO%202021%20Annual%20Water%20Report%20-%20PE%205353%20-%202022-03-31.pdf

LC_SLC_2021 = [('January',0),
               ('February',0),
               ('March',0),
               ('April',0.28),
               ('May',3.55),
               ('June',3.23),
               ('July',0.88),
               ('August',0.35),
               ('September',0.22),
               ('October',0.13),
               ('November',0.14),
               ('December',0.27)]


LC_LCDSSLCC_2021 = [('January', 0.503),
               ('February', 0.446),
               ('March', 0.655),
               ('April', 0.942),
               ('May', 2.916),
               ('June', 3.521),
               ('July', 1.737),
               ('August', 1.359),
               ('September', 0.978),
               ('October', 0.722),
               ('November', 1.018),
               ('December', 1.122)]

LC_LCDSSLCC_2021_Summary_Chart = [('January',0.503),
               ('February',0.446),
               ('March', 0.654),
               ('April', 0.941),
               ('May', 2.974),
               ('June', 3.519),
               ('July', 1.723),
               ('August', 1.355),
               ('September', 0.967),
               ('October', 0.723),
               ('November', 1.016),
               ('December', 1.136)]


LC3_2020 = [('January', 0),
               ('February', 0.44),
               ('March', 0.62),
               ('April', 0.64),
               ('May', 2.02),
               ('June', 3.61),
               ('July', 1.76),
               ('August', 0.47),
               ('September', 0.28),
               ('October', 0.29),
               ('November', 0.32),
               ('December', 0.26)]

#page 474 in LCO 2020 Annual Water Report
WLC_2020 = [('January', 0.03),
               ('February', 0.03),
               ('March', 0.03),
               ('April', 0.03),
               ('May', 0.08),
               ('June', 0.17),
               ('July', 0.09),
               ('August', 0.05),
               ('September', 0.04),
               ('October', 0.04),
               ('November', 0.04),
               ('December', 0.04)]

#Influent versus effluent concentrations
#https://www.teck.com/media/EVWQP_2022_ImplementationPlanAdjustment_Main_Report.pdf
#pg 42

WLC_Influent_2020 = [('January',213),
               ('February',243),
               ('March', 229),
               ('April', 233),
               ('May', 319),
               ('June', 208),
               ('July', 262),
               ('August', 252),
               ('September', 265),
               ('October', 236),
               ('November', 230),
               ('December', 225)]
WLC_Effluent_2020 = [('January',17),
               ('February',16),
               ('March', 19),
               ('April', 19),
               ('May', 16),
               ('June', 5),
               ('July', 8),
               ('August', 9),
               ('September', 11),
               ('October', 16),
               ('November', 20),
               ('December', 18)]

LC_LCDSSLCC_2020_Se_Conc = [('January',),
               ('February',),
               ('March', ),
               ('April', ),
               ('May', ),
               ('June', ),
               ('July', ),
               ('August', ),
               ('September', ),
               ('October', ),
               ('November', ),
               ('December', )]

#Data from Model Outputs to calculate percent treated
LC_WLC_2020_RWQM = [('January', 0.02),
               ('February', 0.02),
               ('March', 0.02),
               ('April', 0.02),
               ('May', 0.05),
               ('June', 0.05),
               ('July', 0.05),
               ('August', 0.05),
               ('September', 0.05),
               ('October', 0.05),
               ('November', 0.05),
               ('December', 0.02)]

LC_LCUSWLC_2020_RWQM = [('January', 0.22),
               ('February',0.22),
               ('March', 0.22),
               ('April', 0.22),
               ('May', 1.29),
               ('June', 1.29),
               ('July', 1.29),
               ('August', 0.6),
               ('September',0.6),
               ('October', 0.6),
               ('November', 0.6),
               ('December', 0.22)]

#%% Calculations

#From model for WLC AWTF
#Treatment percent for LS_WLC total discharge
LC_WLC_2020_RWQM_Discharge = month_dis_liters(LC_WLC_2020_RWQM,2020)

#Percent treated per month
LC_WLC_2020_RWQM_Percent_Treated_Monthly = percent_treated_per_month(LC_WLC_2020_RWQM_Discharge,7500000,2020)

#Remaining treatment capacity
monthly_treatment_capacity_remaining = [i[2] for i in LC_WLC_2020_RWQM_Percent_Treated_Monthly]

#Monthly discahrge from model for LC_LCUSWLC
LC_LCUSWLC_2020_RWQM_Discharge = month_dis_liters(LC_LCUSWLC_2020_RWQM,2020)

#Untreated Discharge
untreated_discharge_from_model = [LC_LCUSWLC_2020_RWQM_Discharge[i] + monthly_treatment_capacity_remaining[i] for i in np.arange(0,12)]

#Untreated as discharge in m3/s
untreated_discharge_instant = [month_dis_to_instant(untreated_discharge_from_model[i], i+1, 2020) for i in np.arange(0,12)]

#Calculate from discharge data
#Treated from WLC 2020
LC_WLC_Discharge_20 = month_dis_liters(WLC_2020,2020)

#Percent treated per month
LC_WLC_2020_Percent_Treated_Monthly = percent_treated_per_month(LC_WLC_Discharge_20,7500000,2020)

#Remaining treatment capacity
monthly_treatment_capacity_remaining = [i[2] for i in LC_WLC_2020_Percent_Treated_Monthly]






#For 2021
#Subtract SLC contribution
LC_dis_21 = dis_difference(LC_LCDSSLCC_2021,LC_SLC_2021)

#Convert to liters per month
LC_LCDSSLCC_Discharge_21 = month_dis_liters(LC_dis_21,2021)

#Total discharge
LC_LCDSSLCC_Total_Discharge_21 = sum(LC_LCDSSLCC_Discharge_21)

#Percent treated
percent_treated(LC_LCDSSLCC_Total_Discharge_21,7500000,2021)

#Percent treated per month
LC_LCDSSLCC_Percent_Treated_Monthly = percent_treated_per_month(LC_LCDSSLCC_Discharge_21,7500000,2021)


#For 2020
#Subtract SLC contribution
LC_dis_20 = dis_difference(LC_LCDSSLCC_2020,LC_SLC_2020)

#Convert to liters per month
LC_LCDSSLCC_Discharge_20 = month_dis_liters(LC_dis_20,2020)

#Total discharge
LC_LCDSSLCC_Total_Discharge_20 = sum(LC_LCDSSLCC_Discharge_20)

#Percent treated
percent_treated(LC_LCDSSLCC_Total_Discharge_20,7500000,2020)

#Percent treated per month
LC_LCDSSLCC_Percent_Treated_Monthly = percent_treated_per_month(LC_LCDSSLCC_Discharge_20,7500000,2020)

#Treatment percent for LC_LC3 total discharge
LC_WLC_2020_RWQM_Discharge = month_dis_liters(LC_WLC_2020_RWQM,2020)

#Percent treated per month
LC_WLC_2020_RWQM_Percent_Treated_Monthly = percent_treated_per_month(LC_WLC_2020_RWQM_Discharge,7500000,2020)




####
(4.679 + 4.358 + 6.521 + 6.850 + 4.996 + 4.181 + 3.816 + 3.536 + 3.401 + 3.166 + 3.059 + 2.971 + 3.026 + 3.211 + 3.370 + 3.370 + 3.409 + 3.386 + 3.227 + 3.031 + 3.016 + 3.002 + 2.962 + 2.924 + 2.846 + 2.864 + 2.924 + 2.860 + 2.750 + 2.689 + 2.591)

w = 1681473*1000
s = 486*(1*m.pow(10,9))
s/w



#For 2020 LC_LC3
#Subtract SLC contribution

#Convert to liters per month
LC_LC3_Discharge_20 = month_dis_liters(LC3_2020,2020)

days_in_2020 = [31,28,31,30,31,30,31,31,30,31,30,31]

Discharge_Day_LC3_2020 = []
for i in np.arange(0,len(LC_LC3_Discharge_20)):
    t = (LC_LC3_Discharge_20[i]/days_in_2020[i])/1E6
    Discharge_Day_LC3_2020.append(t)

#Percent treated per month
LC_LC3_Percent_Treated_Monthly = percent_treated_per_month(LC_LC3_Discharge_20,75E5,2020) #Current Capacity

LC_LC3_Percent_Treated_Monthly_Full = percent_treated_per_month(LC_LC3_Discharge_20,75E5+125E5,2020) #Full Capacity
