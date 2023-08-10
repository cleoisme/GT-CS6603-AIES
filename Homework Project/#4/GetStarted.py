from gensim.models import Word2Vec
import gensim.models
# import nltk
newmodel = gensim.models.KeyedVectors.load_word2vec_format(
    "reducedvector.bin", binary=True)

# # Find the five nearest neighbors to the word man
# print("- Find the five nearest neighbors to the word man \n",
#       newmodel.most_similar('man', topn=5))

# # Compute a measure of similarity between woman and man
# print("- Compute a measure of similarity between woman and man \n",
#       newmodel.similarity('woman', 'man'))

# # To complete analogies like man is to woman as king is to ??
# print(newmodel.most_similar(
#     positive=['king', 'woman'], negative=['man'], topn=1))

# Section 1.1
# print("Man - wife\n",
#       newmodel.similarity('man', 'wife'))
# print("Man - husband\n",
#       newmodel.similarity('man', 'husband'))
# print("Man - child\n",
#       newmodel.similarity('man', 'child'))
# print("Man - queen \n",
#       newmodel.similarity('man', 'queen'))
# print("Man - king \n",
#       newmodel.similarity('man', 'king'))
# print("Man - man \n",
#       newmodel.similarity('man', 'man'))
# print("Man - woman \n",
#       newmodel.similarity('man', 'woman'))
# print("Man - birth\n",
#       newmodel.similarity('man', 'birth'))
# print("Man - doctor \n",
#       newmodel.similarity('man', 'doctor'))
# print("Man - nurse \n",
#       newmodel.similarity('man', 'nurse'))
# print("Man - teacher\n",
#       newmodel.similarity('man', 'teacher'))
# print("Man - professor \n",
#       newmodel.similarity('man', 'professor'))
# print("Man - engineer \n",
#       newmodel.similarity('man', 'engineer'))
# print("Man - scientist \n",
#       newmodel.similarity('man', 'scientist'))
# print("Man - president \n",
#       newmodel.similarity('man', 'president'))

# print("-----")
# print("Woman - wife\n",
#       newmodel.similarity('woman', 'wife'))
# print("Woman - husband\n",
#       newmodel.similarity('woman', 'husband'))
# print("Woman - child\n",
#       newmodel.similarity('woman', 'child'))
# print("Woman - queen \n",
#       newmodel.similarity('woman', 'queen'))
# print("Woman - king \n",
#       newmodel.similarity('woman', 'king'))
# print("Woman - man \n",
#       newmodel.similarity('woman', 'man'))
# print("Woman - woman \n",
#       newmodel.similarity('woman', 'woman'))
# print("Woman - birth\n",
#       newmodel.similarity('woman', 'birth'))
# print("Woman - doctor \n",
#       newmodel.similarity('woman', 'doctor'))
# print("Woman - nurse \n",
#       newmodel.similarity('woman', 'nurse'))
# print("Woman - teacher\n",
#       newmodel.similarity('woman', 'teacher'))
# print("Woman - professor \n",
#       newmodel.similarity('woman', 'professor'))
# print("Woman - engineer \n",
#       newmodel.similarity('woman', 'engineer'))
# print("Woman - scientist \n",
#       newmodel.similarity('woman', 'scientist'))
# print("Woman - president \n",
#       newmodel.similarity('woman', 'president'))

# Section 1.2.1
# print("-----")
# print("actor - actress \n",
#       newmodel.similarity('actor', 'actress'))
# # print("batman - batwoman \n",
# #       newmodel.similarity('batman', 'batwoman'))
# print("boar - sow \n",
#       newmodel.similarity('boar', 'sow'))
# print("boy - girl \n",
#       newmodel.similarity('boy', 'girl'))
# print("brother - sister \n",
#       newmodel.similarity('brother', 'sister'))

# print("-----")
# print("buck - doe \n",
#       newmodel.similarity('buck', 'doe'))
# print("bull - cow \n",
#       newmodel.similarity('bull', 'cow'))
# print("businessman - businesswoman \n",
#       newmodel.similarity('businessman', 'businesswoman'))
# # print("chairman - chairwoman \n",
# #       newmodel.similarity('chairman', 'chairwoman'))
# print("dad - mom \n",
#       newmodel.similarity('dad', 'mom'))

# print("-----")
# print("daddy - mommy \n",
#       newmodel.similarity('daddy', 'mommy'))
# print("duke - duchess \n",
#       newmodel.similarity('duke', 'duchess'))
# print("emperor - empress \n",
#       newmodel.similarity('emperor', 'empress'))
# print("father - mother \n",
#       newmodel.similarity('father', 'mother'))
# # print("fisherman - fisherwoman \n",
# #       newmodel.similarity('fisherman', 'fisherwoman'))

# print("-----")
# print("fox - vixen \n",
#       newmodel.similarity('fox', 'vixen'))
# print("gentleman - lady \n",
#       newmodel.similarity('gentleman', 'lady'))
# print("god - goddess \n",
#       newmodel.similarity('god', 'goddess'))
# print("grandfather - grandmother \n",
#       newmodel.similarity('grandfather', 'grandmother'))
# print("grandpa - grandma \n",
#       newmodel.similarity('grandpa', 'grandma'))

# print("-----")
# print("grandson - granddaughter \n",
#       newmodel.similarity('grandson', 'granddaughter'))
# print("groom - bride \n",
#       newmodel.similarity('groom', 'bride'))
# # print("headmaster - headmistress \n",
# #       newmodel.similarity('headmaster', 'headmistress'))
# print("heir - heiress \n",
#       newmodel.similarity('heir', 'heiress'))
# print("hero - heroine \n",
#       newmodel.similarity('hero', 'heroine'))

# print("-----")
# print("hound - bitch \n",
#       newmodel.similarity('hound', 'bitch'))
# print("husband - wife \n",
#       newmodel.similarity('husband', 'wife'))
# print("king - queen \n",
#       newmodel.similarity('king', 'queen'))
# # print("lion - lioness \n",
# #       newmodel.similarity('lion', 'lioness'))
# print("man - woman \n",
#       newmodel.similarity('man', 'woman'))

# print("-----")
# # print("manager - manageress \n",
# #       newmodel.similarity('manager', 'manageress'))
# print("mister - miss \n",
#       newmodel.similarity('mister', 'miss'))
# # print("murderer - murderess \n",
# #       newmodel.similarity('murderer', 'murderess'))
# print("nephew - niece \n",
#       newmodel.similarity('nephew', 'niece'))
# print("poet - poetess \n",
#       newmodel.similarity('poet', 'poetess'))

# print("-----")
# # print("policeman - policewoman \n",
# #       newmodel.similarity('policeman', 'policewoman'))
# print("prince - princess \n",
#       newmodel.similarity('prince', 'princess'))
# print("ram - ewe \n",
#       newmodel.similarity('ram', 'ewe'))
# print("rooster - hen \n",
#       newmodel.similarity('rooster', 'hen'))
# print("sculptor - sculptress \n",
#       newmodel.similarity('sculptor', 'sculptress'))

# print("-----")
# print("sir - madam \n",
#       newmodel.similarity('sir', 'madam'))
# print("son - daughter \n",
#       newmodel.similarity('son', 'daughter'))
# print("stallion - mare \n",
#       newmodel.similarity('stallion', 'mare'))
# print("stepfather - stepmother \n",
#       newmodel.similarity('stepfather', 'stepmother'))
# # print("superman - superwoman \n",
# #       newmodel.similarity('superman', 'superwoman'))

# print("-----")
# print("tiger - tigress \n",
#       newmodel.similarity('tiger', 'tigress'))
# print("uncle - aunt \n",
#       newmodel.similarity('uncle', 'aunt'))
# print("valet - maid \n",
#       newmodel.similarity('valet', 'maid'))
# print("waiter - waitress \n",
#       newmodel.similarity('waiter', 'waitress'))
# print("webmaster - webmistress \n",
#       newmodel.similarity('webmaster', 'webmistress'))

# Section 1.2.2
# print("-----")
# print("actor - White \n",
#       newmodel.similarity('actor', 'white'))
# print("actor - Black \n",
#       newmodel.similarity('actor', 'black'))
# print("actor - Asian \n",
#       newmodel.similarity('actor', 'asian'))

# print("batman - white \n",
#       newmodel.similarity('batman', 'white'))
# print("batman - black \n",
#       newmodel.similarity('batman', 'black'))
# print("batman - asian \n",
#       newmodel.similarity('batman', 'asian'))

# print("boar - white \n",
#       newmodel.similarity('boar', 'white'))
# print("boar - black \n",
#       newmodel.similarity('boar', 'black'))
# print("boar - asian \n",
#       newmodel.similarity('boar', 'asian'))

# print("boy - white \n",
#       newmodel.similarity('boy', 'white'))
# print("boy - black \n",
#       newmodel.similarity('boy', 'black'))
# print("boy - asian \n",
#       newmodel.similarity('boy', 'asian'))

# print("brother - white \n",
#       newmodel.similarity('brother', 'white'))
# print("brother - black \n",
#       newmodel.similarity('brother', 'black'))
# print("brother - asian \n",
#       newmodel.similarity('brother', 'asian'))

# print("buck - white \n",
#       newmodel.similarity('buck', 'white'))
# print("buck - black \n",
#       newmodel.similarity('buck', 'black'))
# print("buck - asian \n",
#       newmodel.similarity('buck', 'asian'))

# print("bull - white \n",
#       newmodel.similarity('bull', 'white'))
# print("bull - black \n",
#       newmodel.similarity('bull', 'black'))
# print("bull - asian \n",
#       newmodel.similarity('bull', 'asian'))

# print("businessman - white \n",
#       newmodel.similarity('businessman', 'white'))
# print("businessman - black \n",
#       newmodel.similarity('businessman', 'black'))
# print("businessman - asian \n",
#       newmodel.similarity('businessman', 'asian'))

# print("chairman - white \n",
#       newmodel.similarity('chairman', 'white'))
# print("chairman - black \n",
#       newmodel.similarity('chairman', 'black'))
# print("chairman - asian \n",
#       newmodel.similarity('chairman', 'asian'))
# print("dad - mom \n",
#       newmodel.similarity('dad', 'mom'))
# print("dad - white \n",
#       newmodel.similarity('dad', 'white'))
# print("dad - black \n",
#       newmodel.similarity('dad', 'black'))
# print("dad - asian \n",
#       newmodel.similarity('dad', 'asian'))

# print("daddy - white \n",
#       newmodel.similarity('daddy', 'white'))
# print("daddy - black \n",
#       newmodel.similarity('daddy', 'black'))
# print("daddy - asian \n",
#       newmodel.similarity('daddy', 'asian'))

# print("duke - white \n",
#       newmodel.similarity('duke', 'white'))
# print("duke - black \n",
#       newmodel.similarity('duke', 'black'))
# print("duke - asian \n",
#       newmodel.similarity('duke', 'asian'))

# print("emperor - white \n",
#       newmodel.similarity('emperor', 'white'))
# print("emperor - black \n",
#       newmodel.similarity('emperor', 'black'))
# print("emperor - asian \n",
#       newmodel.similarity('emperor', 'asian'))

# print("father - white \n",
#       newmodel.similarity('father', 'white'))
# print("father - black \n",
#       newmodel.similarity('father', 'black'))
# print("father - asian \n",
#       newmodel.similarity('father', 'asian'))

# print("fisherman - white \n",
#       newmodel.similarity('fisherman', 'white'))
# print("fisherman - black \n",
#       newmodel.similarity('fisherman', 'black'))
# print("fisherman - asian \n",
#       newmodel.similarity('fisherman', 'asian'))

# print("fox - white \n",
#       newmodel.similarity('fox', 'white'))
# print("fox - black \n",
#       newmodel.similarity('fox', 'black'))
# print("fox - asian \n",
#       newmodel.similarity('fox', 'asian'))

# print("gentleman - white \n",
#       newmodel.similarity('gentleman', 'white'))
# print("gentleman - black \n",
#       newmodel.similarity('gentleman', 'black'))
# print("gentleman - asian \n",
#       newmodel.similarity('gentleman', 'asian'))

# print("god - white \n",
#       newmodel.similarity('god', 'white'))
# print("god - black \n",
#       newmodel.similarity('god', 'black'))
# print("god - asian \n",
#       newmodel.similarity('god', 'asian'))

# print("grandfather - white \n",
#       newmodel.similarity('grandfather', 'white'))
# print("grandfather - black \n",
#       newmodel.similarity('grandfather', 'black'))
# print("grandfather - asian \n",
#       newmodel.similarity('grandfather', 'asian'))

# print("grandpa - white \n",
#       newmodel.similarity('grandpa', 'white'))
# print("grandpa - black \n",
#       newmodel.similarity('grandpa', 'black'))
# print("grandpa - asian \n",
#       newmodel.similarity('grandpa', 'asian'))

# print("grandson - white \n",
#       newmodel.similarity('grandson', 'white'))
# print("grandson - black \n",
#       newmodel.similarity('grandson', 'black'))
# print("grandson - asian \n",
#       newmodel.similarity('grandson', 'asian'))

# print("groom - white \n",
#       newmodel.similarity('groom', 'white'))
# print("groom - black \n",
#       newmodel.similarity('groom', 'black'))
# print("groom - asian \n",
#       newmodel.similarity('groom', 'asian'))

# print("headmaster - white \n",
#       newmodel.similarity('headmaster', 'white'))
# print("headmaster - black \n",
#       newmodel.similarity('headmaster', 'black'))
# print("headmaster - asian \n",
#       newmodel.similarity('headmaster', 'asian'))

# print("heir - white \n",
#       newmodel.similarity('heir', 'white'))
# print("heir - black \n",
#       newmodel.similarity('heir', 'black'))
# print("heir - asian \n",
#       newmodel.similarity('heir', 'asian'))

# print("hero - white \n",
#       newmodel.similarity('hero', 'white'))
# print("hero - black \n",
#       newmodel.similarity('hero', 'black'))
# print("hero - asian \n",
#       newmodel.similarity('hero', 'asian'))

# print("hound - white \n",
#       newmodel.similarity('hound', 'white'))
# print("hound - black \n",
#       newmodel.similarity('hound', 'black'))
# print("hound - asian \n",
#       newmodel.similarity('hound', 'asian'))

# print("husband - white \n",
#       newmodel.similarity('husband', 'white'))
# print("husband - black \n",
#       newmodel.similarity('husband', 'black'))
# print("husband - asian \n",
#       newmodel.similarity('husband', 'asian'))

# print("king - white \n",
#       newmodel.similarity('king', 'white'))
# print("king - black \n",
#       newmodel.similarity('king', 'black'))
# print("king - asian \n",
#       newmodel.similarity('king', 'asian'))

# print("lion - white \n",
#       newmodel.similarity('lion', 'white'))
# print("lion - black \n",
#       newmodel.similarity('lion', 'black'))
# print("lion - asian \n",
#       newmodel.similarity('lion', 'asian'))

# print("man - white \n",
#       newmodel.similarity('man', 'white'))
# print("man - black \n",
#       newmodel.similarity('man', 'black'))
# print("man - asian \n",
#       newmodel.similarity('man', 'asian'))

# print("manager - white \n",
#       newmodel.similarity('manager', 'white'))
# print("manager - black \n",
#       newmodel.similarity('manager', 'black'))
# print("manager - asian \n",
#       newmodel.similarity('manager', 'asian'))

# print("mister - white \n",
#       newmodel.similarity('mister', 'white'))
# print("mister - black \n",
#       newmodel.similarity('mister', 'black'))
# print("mister - asian \n",
#       newmodel.similarity('mister', 'asian'))

# print("murderer - white \n",
#       newmodel.similarity('murderer', 'white'))
# print("murderer - black \n",
#       newmodel.similarity('murderer', 'black'))
# print("murderer - asian \n",
#       newmodel.similarity('murderer', 'asian'))

# print("nephew - white \n",
#       newmodel.similarity('nephew', 'white'))
# print("nephew - black \n",
#       newmodel.similarity('nephew', 'black'))
# print("nephew - asian \n",
#       newmodel.similarity('nephew', 'asian'))

# print("poet - white \n",
#       newmodel.similarity('poet', 'white'))
# print("poet - black \n",
#       newmodel.similarity('poet', 'black'))
# print("poet - asian \n",
#       newmodel.similarity('poet', 'asian'))

# print("policeman - white \n",
#       newmodel.similarity('policeman', 'white'))
# print("policeman - black \n",
#       newmodel.similarity('policeman', 'black'))
# print("policeman - asian \n",
#       newmodel.similarity('policeman', 'asian'))

# print("prince - white \n",
#       newmodel.similarity('prince', 'white'))
# print("prince - black \n",
#       newmodel.similarity('prince', 'black'))
# print("prince - asian \n",
#       newmodel.similarity('prince', 'asian'))

# print("ram - white \n",
#       newmodel.similarity('ram', 'white'))
# print("ram - black \n",
#       newmodel.similarity('ram', 'black'))
# print("ram - asian \n",
#       newmodel.similarity('ram', 'asian'))

# print("rooster - white \n",
#       newmodel.similarity('rooster', 'white'))
# print("rooster - black \n",
#       newmodel.similarity('rooster', 'black'))
# print("rooster - asian \n",
#       newmodel.similarity('rooster', 'asian'))

# print("sculptor - white \n",
#       newmodel.similarity('sculptor', 'white'))
# print("sculptor - black \n",
#       newmodel.similarity('sculptor', 'black'))
# print("sculptor - asian \n",
#       newmodel.similarity('sculptor', 'asian'))

# print("sir - white \n",
#       newmodel.similarity('sir', 'white'))
# print("sir - black \n",
#       newmodel.similarity('sir', 'black'))
# print("sir - asian \n",
#       newmodel.similarity('sir', 'asian'))

# print("son - white \n",
#       newmodel.similarity('son', 'white'))
# print("son - black \n",
#       newmodel.similarity('son', 'black'))
# print("son - asian \n",
#       newmodel.similarity('son', 'asian'))

# print("stallion - white \n",
#       newmodel.similarity('stallion', 'white'))
# print("stallion - black \n",
#       newmodel.similarity('stallion', 'black'))
# print("stallion - asian \n",
#       newmodel.similarity('stallion', 'asian'))

# print("stepfather - white \n",
#       newmodel.similarity('stepfather', 'white'))
# print("stepfather - black \n",
#       newmodel.similarity('stepfather', 'black'))
# print("stepfather - asian \n",
#       newmodel.similarity('stepfather', 'asian'))

# print("superman - white \n",
#       newmodel.similarity('superman', 'white'))
# print("superman - black \n",
#       newmodel.similarity('superman', 'black'))
# print("superman - asian \n",
#       newmodel.similarity('superman', 'asian'))

# print("tiger - white \n",
#       newmodel.similarity('tiger', 'white'))
# print("tiger - black \n",
#       newmodel.similarity('tiger', 'black'))
# print("tiger - asian \n",
#       newmodel.similarity('tiger', 'asian'))

# print("uncle - white \n",
#       newmodel.similarity('uncle', 'white'))
# print("uncle - black \n",
#       newmodel.similarity('uncle', 'black'))
# print("uncle - asian \n",
#       newmodel.similarity('uncle', 'asian'))

# print("valet - white \n",
#       newmodel.similarity('valet', 'white'))
# print("valet - black \n",
#       newmodel.similarity('valet', 'black'))
# print("valet - asian \n",
#       newmodel.similarity('valet', 'asian'))

# print("waiter - white \n",
#       newmodel.similarity('waiter', 'white'))
# print("waiter - black \n",
#       newmodel.similarity('waiter', 'black'))
# print("waiter - asian \n",
#       newmodel.similarity('waiter', 'asian'))

# print("webmaster - white \n",
#       newmodel.similarity('webmaster', 'white'))
# print("webmaster - black \n",
#       newmodel.similarity('webmaster', 'black'))
# print("webmaster - asian \n",
#       newmodel.similarity('webmaster', 'asian'))

# Q2.2
# print(newmodel.most_similar(
#     positive=['judge', 'throne'], negative=['king'], topn=1))
# print(newmodel.most_similar(
#     positive=['genius', 'dwarf'], negative=['giant'], topn=1))
# print(newmodel.most_similar(
#     positive=['jail', 'dean'], negative=['college'], topn=1))
# print(newmodel.most_similar(positive=['line', 'circle'],
#                             negative=['arc'], topn=1))
# print(newmodel.most_similar(positive=['dutch', 'france'],
#                             negative=['french'], topn=1))
# print(newmodel.most_similar(
#     positive=['king', 'woman'], negative=['man'], topn=1))
# print(newmodel.most_similar(
#     positive=['liquid', 'ice'], negative=['water'], topn=1))
# print(newmodel.most_similar(
#     positive=['sad', 'good'], negative=['bad'], topn=1))
# print(newmodel.most_similar(
#     positive=['hospital', 'teacher'], negative=['nurse'], topn=1))
# print(newmodel.most_similar(
#     positive=['japan', 'pizza'], negative=['usa'], topn=1))
# print(newmodel.most_similar(
#     positive=['dog', 'house'], negative=['human'], topn=1))
# print(newmodel.most_similar(
#     positive=['sky', 'green'], negative=['grass'], topn=1))
# print(newmodel.most_similar(
#     positive=['computer', 'cassette'], negative=['video'], topn=1))
# print(newmodel.most_similar(
#     positive=['house', 'planet'], negative=['universe'], topn=1))
# print(newmodel.most_similar(
#     positive=['sickness', 'wealth'], negative=['poverty'], topn=1))
