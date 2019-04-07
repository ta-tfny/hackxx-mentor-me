import json

class similarityObject:
    mentor = None
    mentee_list = []
    useless_words_array = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
    punctuation_array = [".", "!", "?", " ", ","]

    def __init__(self, mentor, mentee):
        self.mentor = mentor
        self.mentee = mentee

    def similarity_algorithm(self):
        mentor_bio_array = []
        mentee_bio_array = []
        similarity_index = 0
        self.parsing(self.mentee.bio, mentee_bio_array)
        self.parsing(self.mentor.bio, mentor_bio_array)
        for word in mentor_bio_array:
            if word in mentee_bio_array:
                similarity_index = similarity_index + 1
        print(mentor_bio_array)
        print(mentee_bio_array)
        return similarity_index

    def parsing(self, description, description_array):
        parse_string = ""
        for char in description:
            if char not in self.punctuation_array:
                parse_string = parse_string + char
            else:
                if len(parse_string) > 0 and parse_string.lower() not in self.useless_words_array:
                    description_array.append(parse_string.lower())
                parse_string = ""

class Mentee:
    name = ""
    bio = ""
    top_3_companies = []

    def __init__(self, name, bio, top_3_companies):
        self.name = name
        self.bio = bio
        self.top_3_companies = top_3_companies

    def __repr__(self):
        return self.name

class Mentor:
    name = ""
    bio = ""
    email = ""

    def __init__(self, name, bio, email):
        self.name = name
        self.bio = bio
        self.email = email

    def __repr__(self):
        return "Name: " + self.name + "<br /> Short bio: " + self.bio + "<br /> Email: " + self.email

def find_best_mentor():
    array_of_mentors = {}

    # reads mentors json file
    with open('mentors.json') as mentors:
        data = json.load(mentors)
        array_of_mentors = data["mentors"]

        # for item in data["mentors"]:
        #     print(item["name"])
        #     print(item["bio"])
        #     print(item["email"])

    # make a new mentee using the current user data
    mentee_obj = None

    # reads user json file
    with open('user.json') as user:
        data = json.load(user)
        mentee_obj = Mentee(data["name"], data["bio"], data["companies"])

    # go through each mentor and use the algorithm and find the one with the highest similarity
    best_mentor = None
    highest_sim_index = -1
    for item in array_of_mentors:
        # use the keys to get the values of the mentor
        temp_mentor = Mentor(item["name"], item["bio"], item["email"])

        # call on the similarity algorithm that you (huy) wrote
        # use it on the mentee_obj variable and the temp_mentor
        # it looks you're probably going to have to make a (similarityObject)

        similar = similarityObject(temp_mentor, mentee_obj)
        similarity_index = similar.similarity_algorithm()

        # if the similarity index is higher than highest_sim_index
        # then update that variable as well as best_mentor
        if similarity_index > highest_sim_index:
            best_mentor = temp_mentor
            highest_sim_index = similarity_index

    # return a string representation of the best mentor that can displayed on site
    return best_mentor.__repr__()
