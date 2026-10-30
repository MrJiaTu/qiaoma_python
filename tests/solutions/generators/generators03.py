def installments(total, months):
    per = total / months
    for _ in range(months):
        yield per
