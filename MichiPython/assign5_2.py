largest = None
smallest = None

while True:
    raw_num = raw_input("Enter a number:")
    if raw_num == "done":
        break
    try:
        num = int(raw_num)
    except:
        print "Invalid Number"

    if smallest is None and largest is None:
        smallest = num
        largest = num

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print "Maximum", largest
print "Minimum", smallest
