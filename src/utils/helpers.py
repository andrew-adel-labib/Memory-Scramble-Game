def calculate_accuracy(matches, moves):
    if moves == 0:
        return 0

    return round(
        (matches / moves) * 100,
        2
    )



def center_position(container, item):
    return (container - item) // 2