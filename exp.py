class SoyuzDocking:
    def __init__(self):
        self.distance = 500  # Расстояние до "Салют 7" в метрах
        self.speed = 50  # Скорость к "Салют 7" в м/с
        self.fuel = 100  # Количество топлива

    # Сжечь топливо для замедления корабля
    def perform_burn(self, burn_amount):
        self.speed = max(self.speed - burn_amount, 0)
        self.fuel = max(self.fuel - burn_amount, 0)

    # Обновить расстояние на основании текущей скорости
    def update_distance(self):
        self.distance = max(self.distance - self.speed, 0)

    # Проверить, состыковался-ли корабль к Салют-7
    def has_docked(self):
        return self.distance <= 0


# Создать последовательность стыковки
docking_sequence = SoyuzDocking()
# Показать инструкции к игре
print("Добро пожаловать в симуляцию стыковки Союз Т-6!")
print("Ваша миссия – стыковка со станцией Салют-7.")
print("Вы можете управлять скоростью космического корабля сжигая топливо.")
print("Каждая единица сожженного топлива замедляет космический корабль на 1 м/с.")
print("Удачи экипажу!\n")
# Главный игровой цикл
while not docking_sequence.has_docked():
    print(f"Расстояние до Салют-7: {docking_sequence.distance}метров")
    print(f"Скорость: {docking_sequence.speed} м/с")
    print(f"Топливо: {docking_sequence.fuel} кг")
    # Сообщение о провале миссии в случае если закончилось топливо
    if docking_sequence.fuel <= 0:
        print("Кончилось топливо!")
    break
    # Запрос на активацию автопилота если расстояние до станции менее 11 м
    if docking_sequence.distance < 11:
        autopilot = input(
            "До станции Салют-7 осталось менее 11 метров. Активировать режим автопилота для автоматической стыковки? (да/нет): ")
    if autopilot.lower() == 'да':
            print("Автопилот активирован.")
    break
    # Запрос и ввод количества топлива, которое нужно сжечь
    burn_amount = input("Сколько сжечь топлива для снижения скорости: ")
    burn_amount = int(burn_amount)
    # Сжигание топлива и обновление расстояния до космической станции
    docking_sequence.perform_burn(burn_amount)
    docking_sequence.update_distance()
    # Завершение процесса стыковки – проверить условия и вывести результат
    if docking_sequence.distance <= 11 and docking_sequence.speed <= docking_sequence.distance:
        print("Стыковка подтверждена. Поздравляем экипаж!")
    else:
        print("Миссия провалена. Союз Т-6 не смог состыковаться с Салют-7.")
