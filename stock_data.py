import numpy as np
import pandas as pd
import math
import stock_data_helpers as helper
from stock_data_helpers import HistoricalData

prefix = "stock_data."

def print_command(c):
	print(c.format(prefix))

def print_commands():
	print_command("data = {}helper.load_historical_data('dal')")
	print_command("returns = {}helper.calculate_returns(data)")
	print_command("dates = {}helper.get_dates(data)")
	print_command("vol_dates = {}helper.get_vol_dates(dates, n)")
	print_command("volatility = {}helper.calculate_historical_volatility(returns,n)")
	print_command("{}plt.close('all')")
	print_command("vols = {}pd.Series(volatility, index=vol_dates)")
	print_command("vols.plot()")
	print_command("{}plt.show()")

def do_run():
	n = 10
	hd = HistoricalData()
	hd.Load('dal')
	hd.CalculateReturns()
	dates = hd.GetDatesForReturns()
	vol_dates = hd.GetDatesForVolatility(n)
	volatility = hd.CalculateHistoricalVolatility(n)
	periods = [10,20,30,60,90,120,150,180]
	#hd.ClosePlots()
	#hd.PlotVolatilities(*periods)
	#hd.ShowPlots()
	hd.ShowCurrentHistoricalVolatilities(*periods)
	
if __name__ == "__main__":
	do_run()
