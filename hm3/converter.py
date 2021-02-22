while True:
	choice = int(input('''
Выберите что будете переводить: 
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты
0. Выйти из программы 
'''))

	if choice == 0:
		print("До свидания")
		break

	number = float(input("Введите значение: "))

	def dm_v_sm ():
		print (number/2.54)

	def sm_v_dm ():
		print (number*2.54)

	def mil_v_km ():
		print (number*1,609)

	def km_v_mil ():
		print (number/1,609)

	def ft_v_kg ():
		print (number/2.205)

	def kg_v_ft ():
		print (number*2.205)

	def unc_v_grm ():
		print (number/28.35)

	def grm_v_unc ():
		print (number*28.35)

	def gal_v_lit ():
		print (number*3.785)

	def lit_v_gal ():
		print (number/3.785)

	def pin_v_lit ():
		print (number/2.113)

	def lit_v_pin ():
		print (number*2.113)


	if choice == 1:
		dm_v_sm ()
	elif choice == 2:
		sm_v_dm ()
	elif choice == 3:
		mil_v_km ()
	elif choice == 4:
		km_v_mil ()
	elif choice == 5:
		ft_v_kg ()
	elif choice == 6:
		kg_v_ft ()
	elif choice == 7:
		unc_v_grm ()
	elif choice == 8:
		grm_v_unc ()
	elif choice == 9:
		gal_v_lit ()
	elif choice == 10:
		lit_v_gal ()
	elif choice == 11:
		pin_v_lit ()
	elif choice == 12:
		lit_v_pin ()













