from datetime import datetime, date, timedelta


def convert_date_2_str(date, divide_str='-'):
    return date.strftime(f"%d{divide_str}%m{divide_str}%Y")

def get_current_date_str(divide_str='_'):
    today = datetime.today()
    return convert_date_2_str(today, divide_str=divide_str)

def get_k_previous_date(k=0):
    today = datetime.date(datetime.now())
    result_time = today - timedelta(k)
    return result_time
