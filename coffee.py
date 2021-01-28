
# assumes that 1/15 to 1/17 is a good range
# 1/15 = 66.67 gpL
# 1/16 = 62.50 gpL
# 1/17 = 58.82 gpL
_ratio = 16
_intensity_modifier = 0 # -1 to 1

# sure, why not
_tds = 1.4
_retention = 2.3


def solve_volume(dose):
	v = (_ratio - _intensity_modifier) * dose

	return v

def solve_dose(target_volume):
	p = _tds * 0.01
	v = target_volume + (target_volume * p) 
	# this is used in the original, but i cannot understand the arbitrary scaling factor
	# v = target_volume * 0.9765 * (1 - p)
	r = _ratio - _intensity_modifier - _retention
	d = v / r

	return d

def solve_extraction(target_volume, dose):
	e = _tds * target_volume / dose

	return e


print(solve_dose(100))
print(solve_volume(solve_dose(100)))
print(solve_extraction(100, solve_dose(100)))
