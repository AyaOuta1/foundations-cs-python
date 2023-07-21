import sys
def displaymenu():
  print("The Choices Are : \n\n" + "1- Sum Tuples \n" + "2- Export JSON \n" + "3- Import JSON \n" + "4- Exit \n" "------------------------------------")
displaymenu()
def add_tuples(tup1, tup2):
    if len(tup1) != len(tup2):
        raise ValueError("Input tuples must be of the same length")

    return tuple(x + y for x, y in zip(tup1, tup2))
def dict_to_json_string(data_dict):
    json_str = "{\n"
    for key, value in data_dict.items():
        json_str += f'    "{key}": '
        if isinstance(value, str):
            json_str += f'"{value}",\n'
        else:
            json_str += f'{value},\n'
    json_str = json_str.rstrip(',\n') + '\n}'
    return json_str

def write_dict_to_json(data_dict, filename):
    try:
        json_str = dict_to_json_string(data_dict)
        with open(filename, 'w') as file:
            file.write(json_str)
        print("Successfully wrote the dictionary to", filename)

    except Exception as e:
        print("Error:", e)
def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            json_text = file.read()
        objects_list = []
        current_object = {}
        inside_object = False
        key = ""
        value = ""

        for char in json_text:
            if char == '{':
                inside_object = True
                current_object = {}
            elif char == '}':
                inside_object = False
                objects_list.append(current_object)
                current_object = {}
            elif inside_object:
                if char == '"':
                    if not key:
                        key = ""
                    elif not value:
                        key = key.strip('"')
                    else:
                        value = value.strip('"')
                        current_object[key] = value
                        key = ""
                        value = ""
                elif char == ':':
                    pass
                elif char == ',':
                    if key and value:
                        current_object[key] = value
                    key = ""
                    value = ""
                else:
                    if not key:
                        key += char
                    else:
                        value += char

        return objects_list

    except Exception as e:
        print("Error:", e)


def exit():
  return
def main():
  choice = int(input("Enter the number of your choice : "))
  if choice > 4 :
    print("You can only choose 1 or 2 or 3 or 4")
  elif choice == 1 :
    tuple1_input = input("Enter the elements of the first tuple separated by spaces: ")
    tuple2_input = input("Enter the elements of the second tuple separated by spaces: ")
    tuple1 = tuple(map(int, tuple1_input.split()))
    tuple2 = tuple(map(int, tuple2_input.split()))
    result_tuple = add_tuples(tuple1, tuple2)
    print("Result:", result_tuple)
  elif choice == 2 :
    try:
        data_dict = {
            "name": "Aya Outa",
            "age": 22,
            "email": "aya.outa@gmail.com"
        }

        filename = "data.json"

        write_dict_to_json(data_dict, filename)

    except Exception as e:
        print("Error:", e)
  elif choice == 3:
    try:
        filename = "data.json"
        objects_list = read_json_file(filename)
        print(objects_list)

    except Exception as e:
        print("Error:", e)
  else:
    sys.exit()
    

if __name__ == "__main__":
    main()



"""
#big-Onotation
a- O(N^3)
b- O(N^3)
c- O(N!)
d- O(NlogN)
e- O(N)
f- O(N^2)
g- O(N^2)
h- O(N!)
"""