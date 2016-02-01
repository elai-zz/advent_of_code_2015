import random

class Player():
	def __init__(self, list_of_spells, mana, hp):
		self.mana = mana
		self.hp = hp
		self.in_effect = []
		self.list_of_spells = list_of_spells

	def is_dead(self):
		return self.hp <= 0

	def apply_active_spell_effects(self):
		damage = 0
		armor = 0
		new_in_effect = []
		for spell in self.in_effect:
			self.mana += spell.recharge
			self.hp += spell.heal
			armor += spell.armor
			damage += spell.damage
			spell.current_turns -= 1
			if spell.current_turns > 0:
				new_in_effect.append(spell)

		self.in_effect = new_in_effect
		return (damage, armor)

	def is_in_effect(self, chosen_spell):
		for i in self.in_effect:
			if i.name == chosen_spell.name:
				return True
		return False

	def choose_spell(self):
		candidates = []
		for candidate_spell in self.list_of_spells:
			if (not self.is_in_effect(candidate_spell)) and candidate_spell.cost <= self.mana:
				candidates.append(candidate_spell)

		if candidates == []:
			return None

		chosen_spell = random.choice(candidates)

		spell = Spell(
			chosen_spell.name, 
			chosen_spell.turns, 
			chosen_spell.cost, 
			chosen_spell.damage, 
			chosen_spell.heal, 
			chosen_spell.armor, 
			chosen_spell.recharge, 
			chosen_spell.is_active)

		return spell

	def cast(self, spell):
		self.hp += spell.heal
		return spell.damage

class Boss():
	def __init__(self, hp, attack):
		self.hp = hp
		self.attack = attack

	def is_dead(self):
		return self.hp <= 0

	def get_effective_damage(self, armor):
		if armor >= self.attack:
			return 1
		else:
			return self.attack - armor

class Spell():
	def __init__(self, name, turns, cost, damage, heal, armor, recharge, is_active):
		self.name = name
		self.is_active = is_active
		self.turns = turns
		self.cost = cost
		self.damage = damage
		self.heal = heal
		self.recharge = recharge
		self.current_turns = turns
		self.armor = armor

def sim(list_of_spells):
	player_turn = True
	curr_mana = 0
	player = Player(list_of_spells, 500, 50)
	boss = Boss(51, 9)
	moves = []

	while True:

		if boss.is_dead():
			return (curr_mana, moves)
		if player.is_dead():
			return (100000, [])

		(damage, armor) = player.apply_active_spell_effects()
		boss.hp -= damage 
		if boss.is_dead():
			return (curr_mana, moves)

		if player_turn:
			player_turn = False

			if player.mana < 53:
				return (100000, [])

			chosen_spell = player.choose_spell()
			if chosen_spell == None:
				return (100000, [])

			curr_mana += chosen_spell.cost
			player.mana -= chosen_spell.cost
			moves.append(chosen_spell.name)

			damage_this_turn = 0

			if chosen_spell.is_active:
				damage_this_turn = player.cast(chosen_spell)
			else:
				#chosen_spell.current_turns -= 1
				player.in_effect.append(chosen_spell)

			boss.hp -= damage_this_turn 
		else:
			boss_damage = boss.get_effective_damage(armor)
			player.hp -= boss_damage
			player_turn = True

if __name__ == "__main__":
	missile = Spell("magic_missile", 1, 53, 4, 0, 0, 0, True)
	drain = Spell("drain", 1, 73, 2, 2, 0, 0, True)
	shield = Spell("shield", 6, 113, 0, 0, 7, 0, False)
	poison = Spell("poison", 6, 173, 3, 0, 0, 0, False)
	recharge = Spell("recharge", 5, 229, 0, 0, 0, 101, False)
	list_of_spells = [missile, drain, shield, poison, recharge]

	list_of_moves = []
	lowest_mana_cost = 100000

	for i in range(0, 100000):
		(sim_cost, moves) = sim(list_of_spells)

		if sim_cost < lowest_mana_cost:
			lowest_mana_cost = sim_cost
			list_of_moves = moves

	print lowest_mana_cost
	print list_of_moves


