import requests
import threading


url = 'http://luckypro12.com/PS5/includes/submit_order_limelight.php'

data = {
'cc_number' : '4007000000027',
'cc_expmonth' : '8',
'cc_expyear' : '21',
'cc_cvv' : '432'
}


while True:
    response = requests.post(url, data = data)
    print(response)
