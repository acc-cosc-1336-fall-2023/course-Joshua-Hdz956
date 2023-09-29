def get_hour(epoch_seconds):
    hours = (epoch_seconds//3600) % 24
    return hours

def get_minutes(epoch_seconds):
    minutes = (epoch_seconds//60) % 60
    return minutes

def get_seconds(epoch_seconds):
    seconds = (epoch_seconds % 3600) % 60
    return seconds

def get_time(epoch_seconds):
    h = str(get_hour(epoch_seconds)).zfill(2)
    m = str(get_minutes(epoch_seconds)).zfill(2)
    s = str(get_seconds(epoch_seconds)).zfill(2)
    
    print(f'{h}:{m}:{s}')