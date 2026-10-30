def make_tracker():
    history = []
    def record(place):
        history.append(place)
        return len(history)
    return record

track = make_tracker()
track("望京")
track("酒仙桥")
n = track("将台")
