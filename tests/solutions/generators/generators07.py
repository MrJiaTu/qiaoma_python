lunch = ["盖饭", "面条"]
dinner = ["火锅", "烧烤"]

def all_dishes(a, b):
    yield from a
    yield from b

result = list(all_dishes(lunch, dinner))
