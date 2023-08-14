import yfinance as yf
import csv
import pandas as pd
from datetime import datetime, date, timedelta

# #NOTE: Imports SPY Index----------------------------------------------------------------------------------------------------------------------------

# Define the ticker symbol
ticker = "^NDX"

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Download the data
data = yf.download(ticker, start="1993-01-29", end=current_date) 

# Save the data as a CSV file
data.to_csv("NDX.csv")


#NOTE: Creates interest rate file----------------------------------------------------------------------------------------------------------------

# Start and end dates
start_date = date(1993, 1, 29)
end_date = date.today()

# List to store the dates
dates = []

# Generate dates from start to end
current_date = start_date
while current_date <= end_date:
    dates.append(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)

# Add ", 0", ", 3", or ", 1" after the date for specific date ranges
formatted_dates = [
    #2023
    date + ", 0" if date >= "2023-12-01" else
    date + ", 0" if date >= "2023-11-01" else
    date + ", 0" if date >= "2023-10-01" else
    date + ", 5.33" if date >= "2023-09-01" else
    date + ", 5.33" if date >= "2023-08-01" else
    date + ", 5.08" if date >= "2023-07-01" else
    date + ", 5.08" if date >= "2023-06-01" else
    date + ", 5.08" if date >= "2023-05-01" else
    date + ", 4.83" if date >= "2023-04-01" else
    date + ", 4.58" if date >= "2023-03-01" else
    date + ", 4.58" if date >= "2023-02-01" else
    date + ", 4.33" if date >= "2023-01-01" else
    #2022
    date + ", 4.33" if date >= "2022-12-01" else
    date + ", 3.83" if date >= "2022-11-01" else
    date + ", 3.08" if date >= "2022-10-01" else
    date + ", 2.33" if date >= "2022-09-01" else
    date + ", 2.33" if date >= "2022-08-01" else
    date + ", 1.58" if date >= "2022-07-01" else
    date + ", 1.58" if date >= "2022-06-01" else
    date + ", 0.83" if date >= "2022-05-01" else
    date + ", 0.33" if date >= "2022-04-01" else
    date + ", 0.09" if date >= "2022-03-01" else
    date + ", 0.09" if date >= "2022-02-01" else
    date + ", 0.09" if date >= "2022-01-01" else
    #2021
    date + ", 0.09" if date >= "2021-12-01" else
    date + ", 0.09" if date >= "2021-11-01" else
    date + ", 0.09" if date >= "2021-10-01" else
    date + ", 0.09" if date >= "2021-09-01" else
    date + ", 0.09" if date >= "2021-08-01" else
    date + ", 0.09" if date >= "2021-07-01" else
    date + ", 0.09" if date >= "2021-06-01" else
    date + ", 0.09" if date >= "2021-05-01" else
    date + ", 0.09" if date >= "2021-04-01" else
    date + ", 0.09" if date >= "2021-03-01" else
    date + ", 0.09" if date >= "2021-02-01" else
    date + ", 0.09" if date >= "2021-01-01" else
    #2020
    date + ", 0.09" if date >= "2020-12-01" else
    date + ", 0.09" if date >= "2020-11-01" else
    date + ", 0.09" if date >= "2020-10-01" else
    date + ", 0.09" if date >= "2020-09-01" else
    date + ", 0.09" if date >= "2020-08-01" else
    date + ", 0.09" if date >= "2020-07-01" else
    date + ", 0.09" if date >= "2020-06-01" else
    date + ", 0.09" if date >= "2020-05-01" else
    date + ", 0.09" if date >= "2020-04-01" else
    date + ", 0.25" if date >= "2020-03-01" else
    date + ", 1.55" if date >= "2020-02-01" else
    date + ", 1.55" if date >= "2020-01-01" else
    #2019
    date + ", 1.55" if date >= "2019-12-01" else
    date + ", 1.55" if date >= "2019-11-01" else
    date + ", 1.83" if date >= "2019-10-01" else
    date + ", 2.12" if date >= "2019-09-01" else
    date + ", 2.12" if date >= "2019-08-01" else
    date + ", 2.40" if date >= "2019-07-01" else
    date + ", 2.40" if date >= "2019-06-01" else
    date + ", 2.40" if date >= "2019-05-01" else
    date + ", 2.40" if date >= "2019-04-01" else
    date + ", 2.40" if date >= "2019-03-01" else
    date + ", 2.40" if date >= "2019-02-01" else
    date + ", 2.40" if date >= "2019-01-01" else
    #2018
    date + ", 2.20" if date >= "2018-12-01" else
    date + ", 2.20" if date >= "2018-11-01" else
    date + ", 2.18" if date >= "2018-10-01" else
    date + ", 1.92" if date >= "2018-09-01" else
    date + ", 1.92" if date >= "2018-08-01" else
    date + ", 1.91" if date >= "2018-07-01" else
    date + ", 1.92" if date >= "2018-06-01" else
    date + ", 1.70" if date >= "2018-05-01" else
    date + ", 1.67" if date >= "2018-04-01" else
    date + ", 1.42" if date >= "2018-03-01" else
    date + ", 1.42" if date >= "2018-02-01" else
    date + ", 1.42" if date >= "2018-01-01" else
    #2017
    date + ", 1.17" if date >= "2017-12-01" else
    date + ", 1.17" if date >= "2017-11-01" else
    date + ", 1.17" if date >= "2017-10-01" else
    date + ", 1.17" if date >= "2017-09-01" else
    date + ", 1.17" if date >= "2017-08-01" else
    date + ", 1.17" if date >= "2017-07-01" else
    date + ", 0.91" if date >= "2017-06-01" else
    date + ", 0.91" if date >= "2017-05-01" else
    date + ", 0.91" if date >= "2017-04-01" else
    date + ", 0.66" if date >= "2017-03-01" else
    date + ", 0.66" if date >= "2017-02-01" else
    date + ", 0.66" if date >= "2017-01-01" else
    #2016
    date + ", 0.66" if date >= "2016-12-01" else
    date + ", 0.41" if date >= "2016-11-01" else
    date + ", 0.41" if date >= "2016-10-01" else
    date + ", 0.41" if date >= "2016-09-01" else
    date + ", 0.41" if date >= "2016-08-01" else
    date + ", 0.41" if date >= "2016-07-01" else
    date + ", 0.41" if date >= "2016-06-01" else
    date + ", 0.41" if date >= "2016-05-01" else
    date + ", 0.41" if date >= "2016-04-01" else
    date + ", 0.41" if date >= "2016-03-01" else
    date + ", 0.41" if date >= "2016-02-01" else
    date + ", 0.41" if date >= "2016-01-01" else
    #2015
    date + ", 0.13" if date >= "2015-12-01" else
    date + ", 0.13" if date >= "2015-11-01" else
    date + ", 0.13" if date >= "2015-10-01" else
    date + ", 0.13" if date >= "2015-09-01" else
    date + ", 0.13" if date >= "2015-08-01" else
    date + ", 0.13" if date >= "2015-07-01" else
    date + ", 0.13" if date >= "2015-06-01" else
    date + ", 0.13" if date >= "2015-05-01" else
    date + ", 0.13" if date >= "2015-04-01" else
    date + ", 0.13" if date >= "2015-03-01" else
    date + ", 0.13" if date >= "2015-02-01" else
    date + ", 0.13" if date >= "2015-01-01" else
    #2014
    date + ", 0.13" if date >= "2014-12-01" else
    date + ", 0.13" if date >= "2014-11-01" else
    date + ", 0.13" if date >= "2014-10-01" else
    date + ", 0.13" if date >= "2014-09-01" else
    date + ", 0.13" if date >= "2014-08-01" else
    date + ", 0.13" if date >= "2014-07-01" else
    date + ", 0.13" if date >= "2014-06-01" else
    date + ", 0.13" if date >= "2014-05-01" else
    date + ", 0.13" if date >= "2014-04-01" else
    date + ", 0.13" if date >= "2014-03-01" else
    date + ", 0.13" if date >= "2014-02-01" else
    date + ", 0.13" if date >= "2014-01-01" else
    #2013
    date + ", 0.13" if date >= "2013-12-01" else
    date + ", 0.13" if date >= "2013-11-01" else
    date + ", 0.13" if date >= "2013-10-01" else
    date + ", 0.13" if date >= "2013-09-01" else
    date + ", 0.13" if date >= "2013-08-01" else
    date + ", 0.13" if date >= "2013-07-01" else
    date + ", 0.13" if date >= "2013-06-01" else
    date + ", 0.13" if date >= "2013-05-01" else
    date + ", 0.13" if date >= "2013-04-01" else
    date + ", 0.13" if date >= "2013-03-01" else
    date + ", 0.13" if date >= "2013-02-01" else
    date + ", 0.13" if date >= "2013-01-01" else
    #2012
    date + ", 0.13" if date >= "2012-12-01" else
    date + ", 0.13" if date >= "2012-11-01" else
    date + ", 0.13" if date >= "2012-10-01" else
    date + ", 0.13" if date >= "2012-09-01" else
    date + ", 0.13" if date >= "2012-08-01" else
    date + ", 0.13" if date >= "2012-07-01" else
    date + ", 0.13" if date >= "2012-06-01" else
    date + ", 0.13" if date >= "2012-05-01" else
    date + ", 0.13" if date >= "2012-04-01" else
    date + ", 0.13" if date >= "2012-03-01" else
    date + ", 0.13" if date >= "2012-02-01" else
    date + ", 0.13" if date >= "2012-01-01" else
    #2011
    date + ", 0.13" if date >= "2011-12-01" else
    date + ", 0.13" if date >= "2011-11-01" else
    date + ", 0.13" if date >= "2011-10-01" else
    date + ", 0.13" if date >= "2011-09-01" else
    date + ", 0.13" if date >= "2011-08-01" else
    date + ", 0.13" if date >= "2011-07-01" else
    date + ", 0.13" if date >= "2011-06-01" else
    date + ", 0.13" if date >= "2011-05-01" else
    date + ", 0.13" if date >= "2011-04-01" else
    date + ", 0.13" if date >= "2011-03-01" else
    date + ", 0.13" if date >= "2011-02-01" else
    date + ", 0.13" if date >= "2011-01-01" else
    #2010
    date + ", 0.13" if date >= "2010-12-01" else
    date + ", 0.13" if date >= "2010-11-01" else
    date + ", 0.13" if date >= "2010-10-01" else
    date + ", 0.13" if date >= "2010-09-01" else
    date + ", 0.13" if date >= "2010-08-01" else
    date + ", 0.13" if date >= "2010-07-01" else
    date + ", 0.13" if date >= "2010-06-01" else
    date + ", 0.13" if date >= "2010-05-01" else
    date + ", 0.13" if date >= "2010-04-01" else
    date + ", 0.13" if date >= "2010-03-01" else
    date + ", 0.13" if date >= "2010-02-01" else
    date + ", 0.13" if date >= "2010-01-01" else
    #2009
    date + ", 0.13" if date >= "2009-12-01" else
    date + ", 0.13" if date >= "2009-11-01" else
    date + ", 0.13" if date >= "2009-10-01" else
    date + ", 0.13" if date >= "2009-09-01" else
    date + ", 0.13" if date >= "2009-08-01" else
    date + ", 0.13" if date >= "2009-07-01" else
    date + ", 0.13" if date >= "2009-06-01" else
    date + ", 0.13" if date >= "2009-05-01" else
    date + ", 0.13" if date >= "2009-04-01" else
    date + ", 0.13" if date >= "2009-03-01" else
    date + ", 0.13" if date >= "2009-02-01" else
    date + ", 0.13" if date >= "2009-01-01" else
    #2008
    date + ", 0.52" if date >= "2008-12-01" else
    date + ", 0.23" if date >= "2008-11-01" else
    date + ", 2.97" if date >= "2008-10-01" else
    date + ", 1.96" if date >= "2008-09-01" else
    date + ", 1.98" if date >= "2008-08-01" else
    date + ", 1.95" if date >= "2008-07-01" else
    date + ", 1.94" if date >= "2008-06-01" else
    date + ", 2.05" if date >= "2008-08-01" else
    date + ", 2.28" if date >= "2008-04-01" else
    date + ", 2.09" if date >= "2008-03-01" else
    date + ", 3.12" if date >= "2008-02-01" else
    date + ", 4.18" if date >= "2008-01-01" else
    #2007
    date + ", 4.41" if date >= "2007-12-01" else
    date + ", 4.49" if date >= "2007-11-01" else
    date + ", 4.81" if date >= "2007-10-01" else
    date + ", 4.92" if date >= "2007-09-01" else
    date + ", 4.89" if date >= "2007-08-01" else
    date + ", 5.32" if date >= "2007-07-01" else
    date + ", 5.26" if date >= "2007-06-01" else
    date + ", 5.24" if date >= "2007-07-01" else
    date + ", 5.30" if date >= "2007-04-01" else
    date + ", 5.24" if date >= "2007-03-01" else
    date + ", 5.25" if date >= "2007-02-01" else
    date + ", 5.22" if date >= "2007-01-01" else
    #2006
    date + ", 5.27" if date >= "2006-12-01" else
    date + ", 5.20" if date >= "2006-11-01" else
    date + ", 5.24" if date >= "2006-10-01" else
    date + ", 5.30" if date >= "2006-09-01" else
    date + ", 5.37" if date >= "2006-08-01" else
    date + ", 5.25" if date >= "2006-07-01" else
    date + ", 4.99" if date >= "2006-06-01" else
    date + ", 4.99" if date >= "2006-05-01" else
    date + ", 4.82" if date >= "2006-04-01" else
    date + ", 4.60" if date >= "2006-03-01" else
    date + ", 4.48" if date >= "2006-02-01" else
    date + ", 4.24" if date >= "2006-01-01" else
    #2005
    date + ", 4.21" if date >= "2005-12-01" else
    date + ", 4.03" if date >= "2005-11-01" else
    date + ", 3.90" if date >= "2005-10-01" else
    date + ", 3.49" if date >= "2005-09-01" else
    date + ", 3.47" if date >= "2005-08-01" else
    date + ", 3.23" if date >= "2005-07-01" else
    date + ", 3.05" if date >= "2005-06-01" else
    date + ", 3.02" if date >= "2005-05-01" else
    date + ", 2.75" if date >= "2005-04-01" else
    date + ", 2.80" if date >= "2005-03-01" else
    date + ", 2.54" if date >= "2005-02-01" else
    date + ", 2.48" if date >= "2005-01-01" else
    #2004
    date + ", 1.98" if date >= "2004-12-01" else
    date + ", 1.76" if date >= "2004-11-01" else
    date + ", 1.71" if date >= "2004-10-01" else
    date + ", 1.51" if date >= "2004-09-01" else
    date + ", 1.21" if date >= "2004-08-01" else
    date + ", 1.25" if date >= "2004-07-01" else
    date + ", 1.0" if date >= "2004-06-01" else
    date + ", 1.0" if date >= "2004-05-01" else
    date + ", 1.0" if date >= "2004-04-01" else
    date + ", 1.0" if date >= "2004-03-01" else
    date + ", 1.0" if date >= "2004-02-01" else
    date + ", 1.0" if date >= "2004-01-01" else
    #2003
    date + ", 1.0" if date >= "2003-12-01" else
    date + ", 1.0" if date >= "2003-11-01" else
    date + ", 1.0" if date >= "2003-10-01" else
    date + ", 1.0" if date >= "2003-09-01" else
    date + ", 1.0" if date >= "2003-08-01" else
    date + ", 1.0" if date >= "2003-07-01" else
    date + ", 1.0" if date >= "2003-06-01" else
    date + ", 1.0" if date >= "2003-05-01" else
    date + ", 1.0" if date >= "2003-04-01" else
    date + ", 1.0" if date >= "2003-03-01" else
    date + ", 1.0" if date >= "2003-02-01" else
    date + ", 1.0" if date >= "2003-01-01" else
    #2002
    date + ", 1.2" if date >= "2002-12-01" else
    date + ", 1.2" if date >= "2002-11-01" else
    date + ", 1.6" if date >= "2002-10-01" else
    date + ", 1.6" if date >= "2002-09-01" else
    date + ", 1.6" if date >= "2002-08-01" else
    date + ", 1.6" if date >= "2002-07-01" else
    date + ", 1.6" if date >= "2002-06-01" else
    date + ", 1.6" if date >= "2002-05-01" else
    date + ", 1.6" if date >= "2002-04-01" else
    date + ", 1.6" if date >= "2002-03-01" else
    date + ", 1.6" if date >= "2002-02-01" else
    date + ", 1.6" if date >= "2002-01-01" else
    #2001
    date + ", 2.06" if date >= "2001-12-01" else
    date + ", 2.43" if date >= "2001-11-01" else
    date + ", 2.42" if date >= "2001-10-01" else
    date + ", 3.50" if date >= "2001-09-01" else
    date + ", 3.79" if date >= "2001-08-01" else
    date + ", 3.71" if date >= "2001-07-01" else
    date + ", 3.91" if date >= "2001-06-01" else
    date + ", 3.97" if date >= "2001-05-01" else
    date + ", 4.54" if date >= "2001-04-01" else
    date + ", 5.59" if date >= "2001-03-01" else
    date + ", 5.50" if date >= "2001-02-01" else
    date + ", 5.83" if date >= "2001-01-01" else
    #2000
    date + ", 6.47" if date >= "2000-12-01" else
    date + ", 6.48" if date >= "2000-11-01" else
    date + ", 6.46" if date >= "2000-10-01" else
    date + ", 6.55" if date >= "2000-09-01" else
    date + ", 6.48" if date >= "2000-08-01" else
    date + ", 6.52" if date >= "2000-07-01" else
    date + ", 6.56" if date >= "2000-06-01" else
    date + ", 6.71" if date >= "2000-05-01" else
    date + ", 6.08" if date >= "2000-04-01" else
    date + ", 5.79" if date >= "2000-03-01" else
    date + ", 5.79" if date >= "2000-02-01" else
    date + ", 5.56" if date >= "2000-01-01" else
    #1999
    date + ", 5.4" if date >= "1999-12-01" else
    date + ", 5.43" if date >= "1999-11-01" else
    date + ", 5.11" if date >= "1999-10-01" else
    date + ", 5.24" if date >= "1999-09-01" else
    date + ", 5.18" if date >= "1999-08-01" else
    date + ", 4.82" if date >= "1999-07-01" else
    date + ", 4.68" if date >= "1999-06-01" else
    date + ", 4.69" if date >= "1999-05-01" else
    date + ", 4.72" if date >= "1999-04-01" else
    date + ", 4.73" if date >= "1999-03-01" else
    date + ", 4.71" if date >= "1999-02-01" else
    date + ", 4.36" if date >= "1999-01-01" else
    #1998
    date + ", 4.27" if date >= "1998-12-01" else
    date + ", 4.84" if date >= "1998-11-01" else
    date + ", 5.40" if date >= "1998-10-01" else
    date + ", 5.40" if date >= "1998-09-01" else
    date + ", 5.40" if date >= "1998-08-01" else
    date + ", 5.40" if date >= "1998-07-01" else
    date + ", 5.40" if date >= "1998-06-01" else
    date + ", 5.40" if date >= "1998-05-01" else
    date + ", 5.40" if date >= "1998-04-01" else
    date + ", 5.40" if date >= "1998-03-01" else
    date + ", 5.40" if date >= "1998-02-01" else
    date + ", 5.40" if date >= "1998-01-01" else
    #1997
    date + ", 5.40" if date >= "1997-12-01" else
    date + ", 5.40" if date >= "1997-11-01" else
    date + ", 5.40" if date >= "1997-10-01" else
    date + ", 5.40" if date >= "1997-09-01" else
    date + ", 5.40" if date >= "1997-08-01" else
    date + ", 5.40" if date >= "1997-07-01" else
    date + ", 5.40" if date >= "1997-06-01" else
    date + ", 5.40" if date >= "1997-05-01" else
    date + ", 5.40" if date >= "1997-04-01" else
    date + ", 5.40" if date >= "1997-03-01" else
    date + ", 5.40" if date >= "1997-02-01" else
    date + ", 5.40" if date >= "1997-01-01" else
    #1996
    date + ", 5.40" if date >= "1996-12-01" else
    date + ", 5.40" if date >= "1996-11-01" else
    date + ", 5.40" if date >= "1996-10-01" else
    date + ", 5.40" if date >= "1996-09-01" else
    date + ", 5.40" if date >= "1996-08-01" else
    date + ", 5.40" if date >= "1996-07-01" else
    date + ", 5.40" if date >= "1996-06-01" else
    date + ", 5.40" if date >= "1996-05-01" else
    date + ", 5.40" if date >= "1996-04-01" else
    date + ", 5.40" if date >= "1996-03-01" else
    date + ", 5.40" if date >= "1996-02-01" else
    date + ", 5.40" if date >= "1996-01-01" else
    #1995
    date + ", 5.40" if date >= "1995-12-01" else
    date + ", 5.40" if date >= "1995-11-01" else
    date + ", 5.40" if date >= "1995-10-01" else
    date + ", 5.40" if date >= "1995-09-01" else
    date + ", 5.40" if date >= "1995-08-01" else
    date + ", 5.40" if date >= "1995-07-01" else
    date + ", 5.40" if date >= "1995-06-01" else
    date + ", 5.40" if date >= "1995-05-01" else
    date + ", 5.40" if date >= "1995-04-01" else
    date + ", 5.40" if date >= "1995-03-01" else
    date + ", 5.40" if date >= "1995-02-01" else
    date + ", 5.40" if date >= "1995-01-01" else
    #1994
    date + ", 5.49" if date >= "1994-12-01" else
    date + ", 4.66" if date >= "1994-11-01" else
    date + ", 4.57" if date >= "1994-10-01" else
    date + ", 4.68" if date >= "1994-09-01" else
    date + ", 4.22" if date >= "1994-08-01" else
    date + ", 4.22" if date >= "1994-07-01" else
    date + ", 4.17" if date >= "1994-06-01" else
    date + ", 4.28" if date >= "1994-05-01" else
    date + ", 3.42" if date >= "1994-04-01" else
    date + ", 3.45" if date >= "1994-03-01" else
    date + ", 3.31" if date >= "1994-02-01" else
    date + ", 3.08" if date >= "1994-01-01" else
    #1993
    date + ", 2.94" if date >= "1993-12-01" else
    date + ", 3.03" if date >= "1993-11-01" else
    date + ", 2.97" if date >= "1993-10-01" else
    date + ", 2.99" if date >= "1993-09-01" else
    date + ", 2.95" if date >= "1993-08-01" else
    date + ", 2.99" if date >= "1993-07-01" else
    date + ", 2.96" if date >= "1993-06-01" else
    date + ", 3.00" if date >= "1993-05-01" else
    date + ", 2.97" if date >= "1993-04-01" else
    date + ", 2.98" if date >= "1993-03-01" else
    date + ", 2.88" if date >= "1993-02-01" else
    date + ", 2.87" if date >= "1993-01-29" else
    date + ", 0"  
    for date in dates
]
# Create a DataFrame from the formatted dates
df = pd.DataFrame({"Date": formatted_dates})

# Save the DataFrame to a CSV file
df.to_csv("interest_rates.csv", index=False)


#NOTE: Merges SPY, interest rates with----------------------------------------------------------------------------------------------------------------


# Assuming you have the data in files named "SPY.csv" and "interest_rates.csv"
filename1 = "NDX.csv"
filename2 = "interest_rates.csv"

# Create a dictionary to store date-value pairs from interest_rates.csv
interest_rates_dict = {}

# Read data from interest_rates.csv and store in the dictionary
with open(filename2, 'r') as csvfile2:
    csvreader = csv.reader(csvfile2)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        date_value = row[0].split(",")
        date2 = date_value[0].strip()  # Remove any leading/trailing spaces from the date
        value = date_value[1].strip()  # Remove any leading/trailing spaces from the value
        interest_rates_dict[date2] = value

# Read data from SPY.csv and create a new list with appended values
updated_spy_data = []
with open(filename1, 'r') as csvfile1:
    csvreader = csv.reader(csvfile1)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        date1 = row[0].strip()  # Remove any leading/trailing spaces from the date

        # Check if the date exists in the interest_rates_dict
        if date1 in interest_rates_dict:
            interest_rate_value = interest_rates_dict[date1]
        else:
            interest_rate_value = "N/A"  # If there's no corresponding value, use "N/A" or any other placeholder

        row.append(interest_rate_value)  # Append the interest rate value to the row
        updated_spy_data.append(row)    # Append the updated row to the list

# Write the updated data back to SPY.csv
with open(filename1, 'w', newline='') as csvfile1:
    csvwriter = csv.writer(csvfile1)
    csvwriter.writerow(header)  # Write the header row

    for row in updated_spy_data:
        csvwriter.writerow(row)




def append_interest_rate_to_first_row(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        rows = [row for row in csv_reader]  # Read all rows into a list

    # Check if the file is not empty before attempting to append 'Interest Rate'
    if rows:
        rows[0].append('Interest Rate')  # Append 'Interest Rate' to the first row

    # Write back the modified data to the CSV file
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)

# Replace 'SPY.csv' with the actual path to your CSV file
csv_file_path = 'NDX.csv'
append_interest_rate_to_first_row(csv_file_path)



#NOTE: Converts float values to integers, strips spaces----------------------------------------------------------------------------------

def write_formatted_csv(input_file):
    temp_data = []  # Temporary list to hold the formatted rows

    with open(input_file, 'r') as csv_in:
        reader = csv.reader(csv_in)
        header = next(reader)  # Save the header row

        for row in reader:
            formatted_row = [
                row[0],
                int(float(row[1])),
                int(float(row[2])),
                int(float(row[3])),
                int(float(row[4])),
                int(float(row[5])),
                row[6].strip(),
                row[7].strip()
            ]
            temp_data.append(formatted_row)

    # Write the formatted data back to the original file
    with open(input_file, 'w', newline='') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow(header)  # Write the header row

        for row in temp_data:
            writer.writerow(row)

if __name__ == "__main__":
    input_file = "NDX.csv"
    write_formatted_csv(input_file)
