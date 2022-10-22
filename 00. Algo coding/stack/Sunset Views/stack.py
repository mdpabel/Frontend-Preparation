def sunsetViews(buildings, direction):
    stack = []
    n = len(buildings)

    idx = 0 if direction == "EAST" else n - 1
    step = 1 if direction == "EAST" else -1

    while idx >= 0 and idx < n:
        current_building_height = buildings[idx]

        while len(stack) > 0 and buildings[stack[-1]] <= current_building_height:
            stack.pop()

        stack.append(idx)
        idx += step

    return stack if direction == "EAST" else stack[::-1]
