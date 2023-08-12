# Copyright 2022 Thinh Vu @ GitHub

from datetime import datetime, date
from datetime import timedelta
import pandas as pd

def date_from_today(days_delta, format='%Y-%m-%d', backward = True):
    """
    Return a DateTime value using today's DateTime as the base.
    Args:
        days_delta (:obj:`int`, required): How many days to add or subtract from today's
        format (:obj:`str`, required): Datetime format of the output. Ex: "%Y-%m-%d". Concatnate the output string with 'T00:00:00Z' or 'T23:59:59Z' if you need.
        format (:obj:`boolean`, optional): True to get dates in the past, False to get the future ones
    """
    today_val = datetime.now()
    if backward == True:
        target = (today_val - timedelta(days_delta)).strftime(format)
    elif backward == False:
        target = (today_val + timedelta(days_delta)).strftime(format)
    else:
        pass
    return target


def date_start_end(periods, freq, format='%Y-%m-%d'):
    """
    Return a DateTime value using today's DateTime as the base.
    Args:
        format (:obj:`str`, required): Datetime format of the output. Ex: "%Y-%m-%d"
        periods (:obj:`int`, required): How many periods from today
        freq (:obj:`str`, required): datetime frequency code. Ex: 'MS' for Month Start and 'M' for Month End. See more at: 
    """
    today = datetime.now().strftime('%Y-%m-%d')
    target = pd.date_range(end=today, periods=periods, freq=freq)[0]\
                .strftime(format)
    return target


# generate week value
def weeknum_intel(datetime_now):
    """ Generate weeknum for the report, consider the lag time of ICT and PST timezone
    """
    if datetime_now.strftime('%a') == 'Mon':
        this_week = int(datetime_now.strftime('%U'))-1
        last_week = this_week - 1
    else:
        this_week = int(datetime_now.strftime('%U'))
        last_week = this_week - 1
    return this_week, last_week


def month_intel(datetime_now, end_date):
  "Input value should be assigned with datetime.now() value"
  if datetime_now.day == 1 and datetime_now.month < 2: # month = 1
      this_month = 'Dec'
      last_month = 'Nov'
      return this_month, last_month
  elif datetime_now.day > 1 and datetime_now.month < 2 : # month = 1
      this_month = 'Jan'
      last_month = 'Dec'
      return this_month, last_month
  if datetime_now.day == 1 and datetime_now.month == 2:
      this_month = 'Jan'
      last_month = 'Dec'
      return this_month, last_month
  elif datetime_now.day == 1 and datetime_now.month > 2:
      this_month = datetime(datetime_now.year, int(datetime.strptime(end_date, '%Y-%m-%d').strftime('%m')), 1).strftime('%b')
      last_month = datetime(datetime_now.year, int(datetime.strptime(end_date, '%Y-%m-%d').strftime('%m'))-1, 1).strftime('%b')
      return this_month, last_month
  else:
      this_month = datetime_now.strftime('%b')
      last_month = datetime(datetime_now.year, int(datetime.strptime(end_date, '%Y-%m-%d').strftime('%m'))-1, 1).strftime('%b')
      return this_month, last_month

def quarter_intel(datetime_now):
  """ Return this quarter, last quarter base on the datetime value of today"""
  if datetime_now.day == 1 and datetime_now.month in [1, 2, 3, 4]:
      this_quarter = 'Q1'
      last_quarter = 'Q4'
      return this_quarter, last_quarter
  elif datetime_now.day > 1 and datetime_now.month in [1, 2, 3]:
      this_quarter = 'Q1'
      last_quarter = 'Q4'
      return this_quarter, last_quarter
  elif datetime_now.day ==  1 and datetime_now.month in [7, 10]:
      this_quarter = f'Q{(datetime_now.month-1)//3}'
      last_quarter = f'Q{(datetime_now.month-1)//3-1}'
      return this_quarter, last_quarter
  else:
      this_quarter = f'Q{(datetime_now.month-1)//3+1}'
      last_quarter = f'Q{(datetime_now.month-1)//3}'
      return this_quarter, last_quarter

def last_quarter_date (current_quarter):
    """Return the last date of a specific quarter"""
    if current_quarter == 1:
        last_qdate = '03-31'
    elif current_quarter == 2:
        last_qdate = '06-30'
    elif current_quarter == 3:
        last_qdate = '09-30'
    elif current_quarter == 4:
        last_qdate = '12-31'
    return last_qdate

def weeknum_gen():
    if today_val.strftime('%a') == 'Mon':
        this_week = int(today_val.strftime('%U'))-1
        last_week = this_week - 1
    else:
        this_week = int(today_val.strftime('%U'))
        last_week = this_week - 1
    return this_week, last_week