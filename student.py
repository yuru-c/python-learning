class Student:
    # methods /  __init__ 初始化來自類別的物件內容
    def __init__(self, name, house):
        # if not name:
        #     raise ValueError("Missing name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid house")
        # 建立新屬性=實例變數
        self.name = name
        self.house = house
        # self.patronus = patronus


    def __str__(self):
        return f"{self.name} from {self.house}"


    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russel terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    # name, house = get_student()    
    # print(f"{name} from {house}")

    student = get_student()

    '''if student[0] == "padma":
        student[1] = "Ravenclaw"'''
    '''if student["name"] == "padma":
        student["house"] = "Ravenclaw"'''

    # student.house = 呼叫了setter
    # student.house = "Number Four, Privet Drive"
    # ._house 不會導致 ValueError("Invalid house")
    student._house = "Number Four, Privet Drive"
    
    # print(f"{student[0]} from {student[1]}")
    # 字典 print(f"{student['name']} from {student['house']}")
    # print(f"{student.name} from {student.house}")
    # __str__
    print(student)
    '''print("Expecto Patronum!")
    print(student.charm())'''


def get_student():
    '''name = input("Name: ")
    house = input("House: ")
    # return name, house
    # tuple() 像list[]但不能改變value
    return (name, house)'''
    # 字典
    '''student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student'''

    name = input("Name: ")
    house = input("House: ")
    # patronus = input("patronus: ")
    
    # 字典簡化
    # return {"name": name, "house": house}

    # object
    return Student(name, house)

if __name__ == "__main__":
    main()

    