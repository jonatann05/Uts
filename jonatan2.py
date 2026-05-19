# Program Singly Linked List

# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert di awal
    def insert_awal(self, data):
        node_baru = Node(data)
        node_baru.next = self.head
        self.head = node_baru

    # Insert di akhir
    def insert_akhir(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node_baru

    # Traversal / tampilkan data
    def traversal(self):
        if self.head is None:
            print("Linked List kosong")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Searching data
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    # Delete node
    def delete(self, key):
        temp = self.head

        # Jika node pertama yang dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika data tidak ditemukan
        if temp is None:
            print("Data tidak ditemukan")
            return

        prev.next = temp.next
        temp = None


# Program Utama
ll = LinkedList()

# Insert data
ll.insert_akhir(10)
ll.insert_akhir(20)
ll.insert_akhir(30)
ll.insert_akhir(40)

print("Hasil Linked List:")
ll.traversal()

# Search data
cari = 30
print("\nCari data", cari)

if ll.search(cari):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

# Delete data
hapus = 20
print("\nHapus data", hapus)
ll.delete(hapus)

print("Linked List setelah dihapus:")
ll.traversal()