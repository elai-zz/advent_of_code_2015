# really bad python ensues

weapons = {
	"Dagger": [8, 4, 0],
	"Shortsword": [10, 5, 0],
	"Warhammer": [25, 6, 0], 
	"Longsword": [40, 7, 0],
	"Greataxe": [74, 8, 0]
}

armors = {
	"Leather":    [13, 0, 1],
	"Chainmail":  [31, 0, 2],
	"Splintmail": [53, 0, 3],
	"Bandedmail": [75, 0, 4],
	"Platemail": [102, 0, 5]
}

rings = {
	"Damage +1": [25, 1, 0],
	"Damage +2": [50, 2, 0],
	"Damage +3": [100, 3, 0],
	"Defense +1": [20, 0, 1],
	"Defense +2": [40, 0, 2],
	"Defense +3": [80, 0, 3]
}

def getDamage(dam, arm):
	if dam - arm < 0:
		return 1
	else:
		return dam - arm

def fight(hp, damage, armor):
	bossHP = 103
	bossDamage = 9
	bossArmor = 2
	playerTurn = True
	while (hp > 0 and bossHP > 0):
		if playerTurn:
			playerTurn = False
			bossHP -= getDamage(damage, bossArmor)

		else:
			playerTurn = True
			hp -= getDamage(bossDamage, armor)

	if hp > 0:
		return True
	else:
		return False

def getCombinationsNoRings():
	minCost = 1000
	for weapon, w_values in weapons.iteritems():
		for armor, a_values in armors.iteritems():
			cost = w_values[0] + a_values[0]
			if fight(100, w_values[1], a_values[2]) and cost < minCost:
				minCost = cost

	return minCost

def getCombinationsOneRing():
	minCost = 1000
	for weapon, w_values in weapons.iteritems():
		for armor, a_values in armors.iteritems():
			for ring, r_values in rings.iteritems():
				cost = w_values[0] + a_values[0] + r_values[0]
				if fight(100, w_values[1] + r_values[1], a_values[2] + r_values[2]) and cost < minCost:
					minCost = cost

	return minCost

def getCombinationsTwoRings():
	minCost = 1000
	for weapon, w_values in weapons.iteritems():
		for armor, a_values in armors.iteritems():
			for ring, r_values in rings.iteritems():
				for ring2, r2_values in rings.iteritems():
					if ring2 != ring:
						cost = w_values[0] + a_values[0] + r_values[0] + r2_values[0]
						tot_armor = a_values[2] + r_values[2] + r2_values[2]
						tot_attack = w_values[1] + r_values[1] + r2_values[1]
						if fight(100, tot_attack, tot_armor) and cost < minCost:
							minCost = cost

	return minCost

c1 = getCombinationsNoRings()
c2 = getCombinationsOneRing()
c3 = getCombinationsTwoRings()

print c1, c2, c3
print min([c1, c2, c3])

