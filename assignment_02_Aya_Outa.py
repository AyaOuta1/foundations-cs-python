def countdigits(digit):
    if digit < 10:
      return 1
    else:
      return 1 + countdigits(digit // 10)

import sys

def findmax(list):
  if len(list) == 1:
    return list[0]
  else:
    maximum = findmax(list[1:])
    if list[0]> maximum:
      return list[0]
    else:
      return maximum

def count_tag_occurrences(html_code, tag):
    start_tag = f"<{tag}>"
    end_tag = f"</{tag}>"
    count = 0

    def count_tags_recursively(html_code):
        nonlocal count

        start_index = html_code.find(start_tag)
        if start_index == -1:
            return

        end_index = html_code.find(end_tag, start_index)
        if end_index == -1:
            return

        count += 1
        remaining_html = html_code[end_index + len(end_tag):]
        count_tags_recursively(remaining_html)

    count_tags_recursively(html_code)
    return count



def exit():
  return

def displaymenu():
  print("The Choices Are : \n\n" + "1- Count Digits \n" + "2- Find Max \n" + "3- Count Tags \n" + "4- Exit \n" "------------------------------------")
displaymenu()

def main():
  choice = int(input("Enter the number of your choice : "))
  if choice > 4:
    print("You can only choose 1 or 2 or 3 or 4")
  elif choice ==1 :
    digit = int(input("PLease enter a digit : "))   
    count = countdigits(digit)
    print ("The Number of Digits is : " , count)
  elif choice == 2 :
    list1 = input("Please enter a list of numbers separated by spaces : ").split()
    list = [int(num) for num in list1]
    max = findmax(list)
    print("The maximum number in the list is :", max)
  elif choice==3:
    html_code = input("Enter the HTML code: ")
    tag = input("Enter the tag to count occurrences: ")
    occurrences = count_tag_occurrences(html_code, tag)
    print(f"The tag '{tag}' occurs {occurrences} times in the HTML code.")
  else:
    sys.exit()

  
    

main()