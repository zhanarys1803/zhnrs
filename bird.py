class Bird:
    def _init_(self, range_flight, flight_altitude, stomach_capacity):
        self.max_speed = max_speed
        self.range_flight = range_flight
        self.flight_altitude = flight_altitude
        self.stomach_capacity = stomach_capacity
        self.energy = show_energy

    def get_max_speed(self):
        #Показывает максимальную скорость птицы
        print(f"Максимальная скорость птицы: {self.max_speed} км/ч")

    def display_max_range(self):
        # Отображается макс дальность полета птицы.
        print(f"На данный момент максимальная дальность полета: {self.range_flight}")
        
    def set_max_range(self, range_flight):
        #устанавливаем макс дальность полета птицы
        self.range_flight = range_flight

    def set_max_flight_altitude(self, flight_altitude):
        #устанавливаем макс высоту полета птицы
        self.flight_altitude = flight_altitude

    def get_stomach_capacity(self, stomach_capacity):
        #установим обьем желудка
        self.stomach_capacity = stomach_capacity

    def show_stomach_capacity(self):
        #показывает объем желудка 
        print(f"Объем желудка птицы равен: {self.stomach_capacity}")

    def show_energy(self):
        #Показывает сколько энергий у птицы
         print(f"Энергия птицы: {self.show_energy}")

    def start_fly(self):
        # Расход энергий у птицы
        self.energy -= 1
        print("к взлету!")