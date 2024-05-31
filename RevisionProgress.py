# #Revision Progress Tracker Algorithm - www.101computing.net/revision-progress-tracker-algorithm

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~                                 ~")
print("~   Computer Science Revision     ~")
print("~        Progress Tracker         ~")
print("~                                 ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

topics = ["System Architecture",
          "Memory and Storage",
          "Computer Networks",
          "Network Security",
          "Systems Software",
          "Ethical, Legal, Cultural & environmental Impacts of digital technology",
          "Algorithms",
          "Programming Fundamentals",
          "Producing Robust Programs",
          "Boolean Logic",
          "Programming Languages and IDEs"]
for topic in topics:
    response = input(f"Have you complited the revision topic: {topic}? ")
    if response.lower() == 'yes':
        print(f" Good job") 
        continue
    elif response.lower() == 'no':
        print(f" You need to revice this topic: {topic}")
        continue
    else:
        print("Invalid Input")
        break