import threading
import time

# Fonction qui sera exécutée par le thread 1
def task1():
    print("Thread 1 : début de l'exécution")
    time.sleep(2)
    print("Thread 1 : fin de l'exécution")


# Fonction qui sera exécutée par le thread 2
def task2():
    print("Thread 2 : début de l'exécution")
    time.sleep(4)
    print("Thread 2 : fin de l'exécution")


# Fonction qui sera exécutée par le thread 3
def task3():
    print("Thread 3 : début de l'exécution")
    time.sleep(1)
    print("Thread 3 : fin de l'exécution")


# Création de trois threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread3 = threading.Thread(target=task3)

# Démarrage des trois threads
thread1.start()
thread2.start()
thread3.start()

# Attente que les trois threads aient terminé leur exécution
thread1.join()
thread2.join()
thread3.join()

print("Fin du programme")
