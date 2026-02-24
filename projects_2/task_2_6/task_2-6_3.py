type_don = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
type_rec = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()
if type_rec == type_don or type_don == "I":
    print("Переливание возможно")
elif type_rec != type_don or type_don != "I":
    print("Переливание запрещено")
else:
    print("Ошибка записи группы крови")