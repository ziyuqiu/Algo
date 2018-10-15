# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.
import sys
from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

for (name, HashTable) in [("chaining", HashTableChaining), ("linear probing", HashTableProbing)]:
    print("============= Test for %s =============" % name)
    table = HashTable()
    data = [("key "+str(i), "value "+str(i)) for i in range(3000)]
    flag = True
    print("------------ Start inserting: --------------")
    for d in data:
        table.insert(d[0], d[1])
        sys.stdout.write('.')
        sys.stdout.flush()

    print("\n\n* Data inserted, current table has %d items and %d size." % (table.item_count, table.array_size))

    print("------------ Start reading: --------------")
    for d in data:
        if table.get(d[0]) != d[1]:
            flag = False
            print("  !!! ERROR: %s hash table did not return %s => %s !!!" % (name, d[0], d[1]))
        else:
            sys.stdout.write('.')
            sys.stdout.flush()
            # print("%s hash table RETURNED %s => %s" % (name, d[0], d[1]))
    if flag:
        print("\n\n-- Finished, ALL GOOD --")

    # Test overwrite
    table.insert('name', 'Max')
    table.insert('name', 'Luffy')
    table.insert('name', 'Ran')
    table.insert('name', 'Fangfang')
    table.insert('name', 'Andrea')
    for n in ['Max', 'Luffy', 'Ran', 'Fangfang']:
        if table.get('name') == n:
            print("!!! ERROR: overwritting the same key is not implemented! %s" % n)
    if table.get('name') == 'Andrea':
        print('Yes same key is overwritten.')

    try:
        table.insert(None, '1')
    except:
        print("When key is None, the exception is correctly raised")

    try:
        table.insert('xxx', None)
    except:
        print("When value is None, the exception is correctly raised")
