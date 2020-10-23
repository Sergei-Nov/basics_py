class Car:
    staff_type = "vehicle"
    car_counter = 0
    __secret_data = "secret"
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.motor_status = "not_running"
        Car.car_counter += 1

    def start_me(self):
        if self.motor_status == "running":
            print("Машина уже запущена")
            return
        print("Раздался рёв запускающегося мотора")
        self.motor_status = "running"

    def stop_me(self):
        if self.motor_status == "not_running":
            print("Машина уже выключена")
            return
        print("*звук выключающегося мотора*")
        self.motor_status = "not_running"

    @staticmethod
    def secret_func():
        return Car.__secret_data

    def __func(self):
        return self.staff_type



#car_list = [Car(model = 'Tesla-X', color = 'red') for x in range(100)]
new_car = Car("Tesla-x", "red")
new_car.start_me()



c=1
