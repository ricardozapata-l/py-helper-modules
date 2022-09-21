# ====================================================================================================
# Set of functions to handle time operations
#
# Documentation:
#     - arrow : https://arrow.readthedocs.io/en/latest/
#
# Developed by @Zapata: rl-zapata.github.io
# ====================================================================================================
import arrow

class TimeFunctionsDouble:
    # ¡--- Set the timezone to use for the available functions ---!
    def __init__(self, timezone='local'):
        self.timezone = timezone

    # ¡--- Get the period start & end dates based on the beginning & end of a month ---!
    def setMonth(self, offset=0):
        period_dates = {
            'start' : arrow.now(tz=self.timezone).shift(months=offset).floor('month'),
            'end'   : arrow.now(tz=self.timezone).shift(months=offset).ceil('month')
        }

        return period_dates

    # ¡--- Get the period start & end based on today & an offset of days ---!
    def setOffsetDays(self, offset=0):
        period_dates = {
            'start' : arrow.now(tz=self.timezone).shift(days=offset) if offset <0 else arrow.now(),
            'end'   : arrow.now(tz=self.timezone).shift(days=offset) if offset >0 else arrow.now()
        }

        return period_dates

    # ¡--- Get the period start & end based on a custom date given & today ---!
    def setCustomHalf(self, custom_date):
        period_dates = {
            'start' : arrow.now(tz=self.timezone),
            'end'   : arrow.get(custom_date, tzinfo=self.timezone)
        }

        if period_dates['start'] > period_dates['end']:
            period_temp = period_dates['start']
            period_dates['start'] = period_dates['end']
            period_dates['end'] = period_temp

        return period_dates

    # ¡--- Get the period start & end based on a custom dates given ---!
    def setCustomFull(self, custom_start, custom_end):
        period_dates = {
            'start' : arrow.get(custom_start, tzinfo=self.timezone),
            'end'   : arrow.get(custom_end, tzinfo=self.timezone)
        }

        if period_dates['start'] > period_dates['end']:
            period_temp = period_dates['start']
            period_dates['start'] = period_dates['end']
            period_dates['end'] = period_temp

        return period_dates

    # ¡--- Convert the period dates by timezone & format ---!
    def convertDates(self, period_dates, convert_timezone=False, convert_format=False, date_timezone='utc', date_format='YYYY-MM-DD'):
        if convert_timezone == True:
            period_dates['start'] = period_dates['start'].to(date_timezone)
            period_dates['end'] = period_dates['end'].to(date_timezone)

        if convert_format == True:
            period_dates['start'] = period_dates['start'].format(date_format)
            period_dates['end'] = period_dates['end'].format(date_format)

        return period_dates

    # ¡--- Convert the period dates into timestamps ---!
    def convertTimestamps(self, period_dates):
        period_dates['start'] = period_dates['start'].timestamp()
        period_dates['end'] = period_dates['end'].timestamp()

        return period_dates

class  TimeFunctionsSingle:
    # ¡--- Set the base date to use ---!
    def __init__(self, time=None, timezone='local'):
        if time == None:
            self.date = arrow.now(tz=timezone)
        else:
            self.date = arrow.get(time, tzinfo=timezone)

    # ¡--- Convert the date to a new timezone ---!
    def convertTimezone(self, timezone):
        return self.date.to(timezone)

    #  ¡--- Change the format of the date ---!
    def convertFormat(self, format):
        return self.date.format(format)