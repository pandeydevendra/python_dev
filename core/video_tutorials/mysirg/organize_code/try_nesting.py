# without exception
try:
    print("Line1")
    print("Line2")

    try:
        print("Line3")
        print("Line4")

    finally:
        print("Finally1")

finally:
    print("Finally2")

print("\nWith Exception>>\n")
# with exception
try:
    print("Line1")
    print("Line2")

    try:
        print("Line3")
        3 / 0
        print("Line4")
    except ZeroDivisionError:
        print("Except1")

    finally:
        print("Finally1")

finally:
    print("Finally2")

print("\nWith Exception 2 >>\n")

# with exception handling
try:
    print("Line1")
    print("Line2")

    try:
        print("Line3")
        3 + "5"
        print("Line4")
    except ZeroDivisionError:
        print("Except1")

    finally:
        print("Finally1")
    print("Line5")

except TypeError:
    print("Except2")
finally:
    print("Finally2")
