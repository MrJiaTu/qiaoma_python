class Snowflake:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.last_ts = -1
        self.seq = 0

    def next_id(self, ts):
        if ts == self.last_ts:
            self.seq += 1
        else:
            self.last_ts = ts
            self.seq = 0
        return ts * 10000 + self.machine_id * 100 + self.seq
