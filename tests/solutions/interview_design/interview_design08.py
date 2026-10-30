def retry_delays(fail_times, max_attempts):
    delays = []
    for i in range(min(fail_times, max_attempts)):
        delays.append(2 ** i)
    return delays
