def make_ticket():
    seq = 0
    def next_ticket():
        nonlocal seq
        seq = seq + 1
        return f"T{seq}"
    return next_ticket

ticket = make_ticket()
t1 = ticket()
