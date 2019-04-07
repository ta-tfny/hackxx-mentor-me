class similarityObject:
    mentor = None
    mentee_list = []
    similarity_dict = {}
    useless_words_array = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
    punctuation_array = [".", "!", "?", " ", ","]

    def __init__(self, mentor, mentee_list):
        self.mentor = mentor
        self.mentee_list = mentee_list
        for mentee in mentee_list:
            self.similarity_dict[mentee] = 0

    def similarity_parse(self):
        for mentee in self.mentee_list:
            self.similarity_dict[mentee] = self.similarity_algorithm(self.mentor, mentee)

    def similarity_algorithm(self, mentor, mentee):
        mentor_bio_array = []
        mentee_bio_array = []
        similarity_index = 0
        self.parsing(mentee.bio, mentee_bio_array)
        self.parsing(mentor.bio, mentor_bio_array)
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
    school = ""
    graduation_year = ""
    age = ""
    gender = ""
    top_3_companies = []

    def __init__(self, name, bio, school, graduation_year, age, gender, \
    top_3_companies):
        self.name = name
        self.bio = bio
        self.school = school
        self.graduation_year = graduation_year
        self.age = age
        self.gender = gender
        self.top_3_companies = top_3_companies

    def __repr__(self):
        return self.name

class Mentor:
    bio = ""
    school = ""
    graduation_year = ""
    name = ""
    age = ""
    gender = ""
    top_3_companies = []

    def __init__(self, name, bio, school, graduation_year, age, gender, \
    top_3_companies):
        self.name = name
        self.bio = bio
        self.school = school
        self.graduation_year = graduation_year
        self.age = age
        self.gender = gender
        self.top_3_companies = top_3_companies

    def __repr__(self):
        return self.name
