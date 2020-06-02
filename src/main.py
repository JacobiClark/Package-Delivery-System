from PHub import PHub
import csv
import datetime


def main():
	phub = PHub()
	user_input = int(input("Welcome to WGU package delivery service!\nTo view all package statuses at a given time, enter 1.\nTo simulate a day's delivery, please press 2.\n"))
	def get_stop_time():
		hour = int(input("Enter hour time to stop at between 0 and 24: "))
		minute = int(input("Enter minute time to stop at between 0 and 60: "))
		second = int(input("Enter second time to stop at between 0 and 60: "))
		return datetime.datetime(2020,3,15,hour,minute,second)
	if user_input == 1:
		phub.start(get_stop_time())
	else:
		phub.start(datetime.datetime(9999,3,15,0,0,0))



if __name__ == "__main__":
	main()
