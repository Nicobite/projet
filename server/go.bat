node server.js
pause


print("[OLD]")
while 1:
	n=int(input("Number of messages: "))
	for i in range(0, n):
		print("msg #{} sent".format(i))