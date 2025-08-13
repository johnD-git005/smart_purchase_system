
print("\v Welcome To Smart Purchase System")

balance = 1000

while True:
	dial = input("\n Dial *555# to continue \n Type 'stop' to Terminate Program: ")

	if dial == "*555#":
		print("""
		Please Select an Option Below to Continue
		1. Buy Airtime
		2. By Data
		3. Borrow
		4. Check Balance
		5. Stop
		""")
		
		option = input("\n Please Select an Option: ")
		if option == "1":
			print("\n Only MTN Network is Available for Purchase")
			phone = int(input("\n Enter Phone Number: "))
			airtime = int(input("Input Amount: "))

			if airtime > balance:
				print("\n Insuficient Funds!")
			else:
				balance -= airtime
				print(f"\n Airtime Purchase of ₦{airtime} to Phone: {phone} was Successful!")

		elif option == "2":
			print("""
			Data Rates
			1. 500 MB - 7 days ₦400
			2. 1 GB - 30 days ₦600
			3. 2 GB - 30 days ₦800
			4. 3 GB - 30 days ₦1,000
			""")
			data = int(input("\n Enter Amount \n ₦400, ₦600, ₦800, ₦1,000: "))
			phone= int(input("\n Enter Phone Number: "))

			if data > balance:
				print("\n Insufficient Funds!")
			else:
				balance -= data
				print(f"\n Data Purchase of ₦{data} to Phone: {phone} was Successful!")

		elif option == "3":
			print("""
			Please select an option below to continue
			1. Data
			2. Airtime
			""")

			borrow = int(input("\n Input an Option: "))

			if borrow == 1:
				print("""
				Data Rates
				1. 500 MB - 7 days ₦400
				2. 1 GB - 30 days ₦600
				3. 2 GB - 30 days ₦800
				4. 3 GB - 30 days ₦1,000
				""")
				data = int(input("\n Enter Amount \n ₦400, ₦600, ₦800, ₦1,000: "))
				phone= int(input("\n Enter Phone Number: "))
				balance -= data
				print(f"\n Data Purchase of ₦{data} to Phone: {phone} was successful!")

			elif borrow == 2:
				airtime = int(input("\n Enter Amount \n ₦400, ₦600, ₦800, ₦1,000: "))
				phone= int(input("\n Enter Phone Number: "))
				balance -= airtime
				print(f"\n Airtime Purchase of ₦{airtime} to Phone: {phone} was successful!")

			else:
				print("\n Invalid Selection!")

		elif option == "4":
			print(f"\n Available Balance: ₦{balance}")


		elif option == "5":
			print("\n Terminating Program. Goodbye!!!")
			break

		else:
			print("\n Invalid Selection!")

	elif dial == "stop":
		print("\n Terminating Program. Goodbye!!!")
		break
	else:
		print("\n Invalid Selection!")
