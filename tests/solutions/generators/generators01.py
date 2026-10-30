def page_numbers(total):
    page = 1
    while page <= total:
        yield page
        page += 1
