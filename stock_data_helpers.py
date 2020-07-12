import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

class HistoricalData:
	def __init__(self):
		self.date_column = 'Date'
		self.close_price_column  = ' Close/Last'
		pass

	def Load(self,symbol):
		self.Clean()
		path = "~/data/prices/"+symbol+"/data.csv"
		print("Loading historical data for {} from {}...".format(symbol,path))
		self.data = pd.read_csv(path)
		self.data = self.data.iloc[::-1]

	def Clean(self):
		#clear data frame
		self.returns = []
		#self.volatilities.Clear() # we should  create a Volatilities container for the vols
		
	def GetReturns(self):
		return self.returns

	def GetData(self):
		return self.data

	def GetDates(self):
		return self.data['Date']

	def GetDatesForReturns(self):
		return self.GetDates()[1:]

	def GetDatesForVolatility(self,n):
		return self.GetDatesForReturns()[n:]

	def CalculateHistoricalVolatility(self,n):
		vols = []
		size = len(self.returns)
		for i in range(0, size-n):
			period = pd.Series(self.returns[i:i+n-1])
			description = period.describe()
			vols.append(description['std'])
		return vols

	def CalculateReturns(self):
		size = self.data['Date'].size
		self.returns = []
		for i in range(1, size):
			dfrom = self.data[self.date_column][i-1] #t1
			dto = self.data[self.date_column][i] #t2
			prices = self.data[self.close_price_column]
			daily_return = math.log(prices[i-1]/prices[i])
			self.returns.append(daily_return)
		self.returns.reverse()

	def ClosePlots(self):
		plt.close('all')
	
	def ShowPlots(self):
		plt.show()
	
	def PlotVolatilities(self,*periods):
		for period in periods:
			self.PlotVolatility(period)
	
	def PlotVolatility(self,n):
		volatility = self.CalculateHistoricalVolatility(n)
		vols = pd.Series(volatility, index=self.GetDatesForVolatility(n))
		vols.plot()
	
	def ShowCurrentHistoricalVolatilities(self,*periods):
		# print:
		#	Period 	| Volatility
		#	period1 | volatility_for_period1
		#	period2 | volatility_for_period2
		#	period3 | volatility_for_period3
		# 	...
	
		vols = {}
		for period in periods:
			vols[period] = self.GetHistoricalVolatility(period)
		print("Period | Volatility ")
		print("______________________________")
		for [p,v] in vols.items():
			print("   {}  | {} ".format(p,v))
		
	def GetHistoricalVolatility(self,n):
		volatility = self.CalculateHistoricalVolatility(n)
		return volatility[-1]
	
