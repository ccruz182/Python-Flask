my_list  = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

odds = [n for n in range(10) if n % 2 == 0]
print("Odds", odds)

people_you_know = ["Rolf", "AnnA", "GREG"]
normalised_people = [person.lower() for person in people_you_know]
print("Normalised:", normalised_people)
