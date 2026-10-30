import random

def split_red_packet(total, count):
    packets = []
    remaining = total
    for i in range(count):
        if i == count - 1:
            packets.append(remaining)
        else:
            max_take = remaining // (count - i) * 2
            amount = random.randint(1, max(1, max_take - 1))
            packets.append(amount)
            remaining -= amount
    return packets
