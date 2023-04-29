from .constants import GLUCOSE_RANGE, OPTIMAL_GLUCOSE_LEVEL

def glevel_based_insulin_needed(glucose_level):
    if glucose_level >= GLUCOSE_RANGE[1] or glucose_level <= GLUCOSE_RANGE[0]:
        extra_units = (glucose_level - OPTIMAL_GLUCOSE_LEVEL) / 50
        print(f"extra units needed: {extra_units}")
        return extra_units
    else:
        print(f"sugar in range: {glucose_level}")
        extra_units = 0
        return extra_units