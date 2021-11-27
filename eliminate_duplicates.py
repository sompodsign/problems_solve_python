def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


print(list(dedupe([int(x) for x in list("23423423534643564573453434234325")])))