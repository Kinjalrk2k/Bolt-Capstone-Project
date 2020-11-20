from boltiot import Bolt, Email
import json, time, math, statistics
import cred

def to_C(sensor):
    '''
        This function converts the passed sensor value to Celsius
    '''
    return (sensor * 100) / 1024

def send_mail(subject, body, ifprint = False):
    '''
        This function sends mail to the RECIPIENT_EMAIL as mentioned in cred.py
        subjects and body are self explanatory
        ifprint is default False. Setting it True, makes the fuction print all response texts
    '''
    mailer = Email(cred.MAILGUN_API_KEY, cred.SANDBOX_URL, cred.SENDER_EMAIL, cred.RECIPIENT_EMAIL)

    response = mailer.send_email(subject, body)
    response_text = json.loads(response.text)

    if(ifprint):
        print(response_text)
    if response_text['message'] == 'Queued. Thank you.':
        return True
    else:
        return False

threshold = (60, 120)   # As decided from Objective E
mybolt = Bolt(cred.api_key, cred.device_id)
pin = 'A0'

def get_sensor(pin):
    '''
        This function reads the data from the passed pin. Also handles certain exceptions
    '''
    try:
        data = json.loads(mybolt.analogRead(pin))
        if data['success'] != 1:
            print('Request Unsuccessful')
            print('Response data ->', data)
            return None
        sensor_value = int(data['value'])
        return sensor_value

    except Exception as e:
        print('An expection occured while returning the sensor value! Details below:')
        print(e)
        return None

FRAME_SIZE = 5
MUL_FACTOR = 3

history_data = []
saved_history = []

def compute_bounds(history_data, frame_size, factor):
    '''
        This function calculates Z-score on the basis of frame_zise and multiplicative factor
    '''
    if len(history_data) < frame_size:
        return None

    if len(history_data) > frame_size:
        del history_data[0 : (len(history_data) - frame_size)]
    
    Mn = statistics.mean(history_data)

    variance = 0
    for d in history_data:
        variance += math.pow((d - Mn), 2)

    Zn = factor * math.sqrt(variance / frame_size)
    high_bound = history_data[frame_size-1] + Zn
    low_bound = history_data[frame_size-1] - Zn

    return (high_bound, low_bound)



while True:
    sensor_value = get_sensor(pin)
    print(f'The sensor value is: {str(sensor_value)}\tTemperature is: {to_C(sensor_value)}\u00B0C')

    if sensor_value < threshold[0] or sensor_value > threshold[1]:
        print('Temperature beyond thresholds! Sending an email')
        send_mail('Warning! Temperature Alert!',
        f'Temperature is beyond set threshold values!\nTemperature: {to_C(sensor_value)}\u00B0C\nTimeStamp: {time.ctime(time.time())}')

    bound = compute_bounds(history_data, FRAME_SIZE, MUL_FACTOR)
    if not bound:
        print('Not enough data to compute Z-score. Need ' + str(FRAME_SIZE - len(history_data)) + ' more data points\n')
        history_data.append(sensor_value)
        saved_history.append(sensor_value)
        time.sleep(10)
        continue

    try:
        # print(bound)
        if sensor_value > bound[0]:
            print('Someone has opened the fridge door\n')
        elif sensor_value < bound[1]:
            print('Someone has closed the fridge door\n')

        history_data.append(sensor_value)
        saved_history.append(sensor_value)
    
    except Exception as e:
        print ('Error: ', e)

    time.sleep(10)    