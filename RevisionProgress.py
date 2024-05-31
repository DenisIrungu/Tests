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
        
# def display_message (name):
#     print(f"You are learning python {name}")
# display_message("Toh")

# def favourite_book(title):
#     print(f"\n,One of my favourite book is {title} ")
# favourite_book ("Alice in Wonderland")

# def make_shirts (size, message):
#     print(f"The size of the shirt is {size}, printed {message} at the back")
# make_shirts ("medium", "i love python") 

# def make_shirts (size, message):
#     print(f"\n The size of the shirt is {size}, printed '{message}' at the back")
# make_shirts (message= "i love python", size = "small")

# def make_shirts (message, size= "large"):
#     print(f"\nThe size of the shirt is {size}, printed {message} at the back")
# make_shirts ("I love python")
# make_shirts (size= "Medium", message= "Ilove python")
# make_shirts ( message= "I love Toh", size= "small")

# def describe_city (city, country = "Kenya"):
#     print (f"{city} is in {country}")
# describe_city ("Nakuru")
# describe_city ("Nairobi")
# describe_city ("Kisumu")
# describe_city (city= "Kampala", country= "Uganda")


# def make_album (name, title,song_number= None):
#     artist = {'Artist_name': name, 'Album_Title': title }
#     if song_number:
#         artist['song_number']= song_number
#     return artist
# while True:
#     print("\nTell me the album information")
#     print("Press 'q' to Exit")

#     artist_name = input("Enter the Artist_Name: ")
#     if artist_name.lower()== 'q':
#         break
#     album_name = input("Enter  the album_name: ")
#     if album_name.lower() == 'q':
#          break
    
#     musician = make_album (artist_name, album_name)
#     musician2 = make_album (artist_name, album_name)
# print(f"The album information is: {musician}")
# print(f"The album information is: {musician2}")




