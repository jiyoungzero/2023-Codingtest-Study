def solution(amount, value, stomach):
    items = [(v, a) for v, a in zip(value, amount)]
    items.sort(reverse=True)

    best_meat_consumption = min(items[0][1] // len(stomach),
                                 min(stomach)) * len(stomach)
    total_stomach = sum(stomach) - best_meat_consumption
    result = best_meat_consumption * items[0][0]

    for v, a in items[1:]:
        consumption = min(total_stomach, a)
        result += v * consumption
        total_stomach -= consumption
        if total_stomach == 0:
            break
    
    return result