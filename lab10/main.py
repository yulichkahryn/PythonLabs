from linked_list import DoublyLinkedList
from transistor import Transistor


lst = DoublyLinkedList()

lst.push_back(Transistor("p-n-p", "КТ120", 1, 1))
lst.push_back(Transistor("a", "AM400", -1, 1))
lst.push_back(Transistor("ddd", "TR101", 5, 1))
lst.push_back(Transistor("d", "MB350", 224, 1))
lst.push_back(Transistor("a", "КТ120", 3, 1))
lst.push_back(Transistor("d", "AM400", 11, 1))
lst.push_back(Transistor("ab", "КТ120", -1, 1))
lst.push_back(Transistor("p-n-p", "XZ606", 3, 1))
print("Starting list of transistors:")
lst.print_list()
print()
print("Transistors of mark КТ120:")
lst.print_by_mark("КТ120")
print()
lst.sort_by_selection()
print("Transistors sorted by type and Imax:")
lst.print_list()
