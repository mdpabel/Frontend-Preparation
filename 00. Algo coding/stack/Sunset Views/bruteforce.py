def sunsetViews(buildings, direction):
    buildingsWithSunsetViws = []
    n = len(buildings)
    startIdx = 0 if direction == "WEST" else n - 1
    step = 1 if direction == "WEST" else -1

    idx = startIdx
    max_height = 0

    while idx >= 0 and idx < n:
        current_building_height = buildings[idx]

        if current_building_height > max_height:
            buildingsWithSunsetViws.append(idx)

        max_height = max(max_height, current_building_height)
        idx += step

    return buildingsWithSunsetViws if direction == "WEST" else buildingsWithSunsetViws[::-1]
