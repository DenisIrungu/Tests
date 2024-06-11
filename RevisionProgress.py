# #Revision Progress Tracker Algorithm - www.101computing.net/revision-progress-tracker-algorithm

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~                                 ~")
print("~   Computer Science Revision     ~")
print("~        Progress Tracker         ~")
print("~                                 ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

revised_topics = ["System Architecture",
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

no_of_topics_rev=0
total_topics=len(revised_topics)

for revised_topic in revised_topics:
    response = input(f"Have you revised {revised_topic}? ")
    if response =='Yes':
        no_of_topics_rev+= 1
        print ("Good")
        continue
    elif response=='No':
        print("You need to revise this topic")
        continue
    else:
        print("Invalid input. Enter yes or no to continue")
        break
def prog_score():
    prog_scores=((no_of_topics_rev)/(total_topics))*100
    y=int(prog_scores)

    print(f"Your score is {y}")
    if y >60:
        print(f"Your score is {y}. You qualify to seat for exams")
    else:
         print(f"Your score is:{y}. You don't qualify to saet for Exams ")
    
prog_score()
        
