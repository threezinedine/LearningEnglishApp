from datetime import datetime, date, timedelta


def convert_date_2_str(date, divide_str='_'):
    return date.strftime(f"%d{divide_str}%m{divide_str}%Y")

def get_k_previous_date(k=0, divide_str='_'):
    today = datetime.date(datetime.now())
    result_time = today - timedelta(k)
    return convert_date_2_str(result_time, divide_str=divide_str)
