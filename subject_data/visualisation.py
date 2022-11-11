import pandas as pd
import matplotlib.pyplot as plt
import os
import pathlib


directory = pathlib.Path(__file__).parent.resolve()

num_visual_learners = 0
num_audiovisual_learners = 0

visual_learner_example = None
audiovisual_learner_example = None
subject_nr = 0

visual_num_prompts = []
audiovisual_num_prompts = []
visual_num_correct = []
audiovisual_num_correct = []
visual_num_wrong = []
audiovisual_num_wrong = []
visual_learned_visual = []
visual_learned_audiovisual = []
audiovisual_learned_visual = []
audiovisual_learned_audiovisual = []
max_facts_seen_visual = []
max_facts_seen_audiovisual = []
visual_facts_seen_visuallearners = []
audiovisual_facts_seen_visuallearners = []
visual_facts_seen_audiovisuallearners = []
audiovisual_facts_seen_audiovisuallearners = []

audiofact_correct_audiolearner_5min = []
audiofact_correct_visuallearner_5min = []
audiofact_wrong_audiolearner_5min = []
audiofact_wrong_visuallearner_5min = []
visualfact_correct_audiolearner_5min = []
visualfact_correct_visuallearner_5min = []
visualfact_wrong_audiolearner_5min = []
visualfact_wrong_visuallearner_5min = []


names = ['christiaan.csv', 'fanny.csv', 'hilbert.csv', 'joep.csv', 'Matthijs.csv', 'patrick.csv', 'siert_jan.csv', 'wouter.csv']


# data = pd.read_csv(os.path.join(directory, 'christiaan.csv'))
# print(data)

for name in range(len(names)):
    print(names[name])

    data = pd.read_csv(os.path.join(directory, names[name]))
    num_questions = len(data)
    print(data)

    if data["audio_visual_chance"].mean() > 0.5:
        num_audiovisual_learners += 1
        audio_learner = True
        audiovisual_num_prompts.append(num_questions)
    else:
        num_visual_learners += 1
        audio_learner = False
        visual_num_prompts.append(num_questions)



    # Basic info
    # value counts of the correct and wrong answers
    correct = data["correct"].value_counts().tolist()
    correct2 = data["correct"].value_counts()
    #print the number of true answers from corrent
    print(correct2)
    print("Name: " + str(names[name]) +str(correct))


    print("This subject answered " + str(correct[0]) + " out of " + str(num_questions) + " questions correct and therefore made " + str(correct[1]) + " mistakes.")
    if audio_learner:
        audiovisual_num_correct.append(correct[0])
        audiovisual_num_wrong.append(correct[1])
    else:
        visual_num_correct.append(correct[0])
        visual_num_wrong.append(correct[1])

    question_type_Audio = data["audio_or_visual_fact"].value_counts().Audio
    question_type_Visual = data["audio_or_visual_fact"].value_counts().Visual


    print("Out of the " + str(num_questions) + " prompts, " + str(question_type_Visual) + " were visual and " + str(question_type_Audio) + " were audiovisual.")
    if audio_learner:
        visual_facts_seen_audiovisuallearners.append(question_type_Visual)
        audiovisual_facts_seen_audiovisuallearners.append(question_type_Audio)
    else:
        visual_facts_seen_visuallearners.append(question_type_Visual)
        audiovisual_facts_seen_visuallearners.append(question_type_Audio)

    correct_audio_visual = data["correct_audio_visual"].max()
    wrong_audio_visual = data["wrong_audio_visual"].max()
    print("The subject managed to learn " + str(correct_audio_visual) + " Portuguese words from audiovisual stimuli and made " + str(wrong_audio_visual) + " mistakes on words presented as such.")        
    if audio_learner:
        audiovisual_learned_audiovisual.append(correct_audio_visual)
    else:
        visual_learned_audiovisual.append(correct_audio_visual)

    correct_visual = data["correct_visual"].max()
    wrong_visual = data["wrong_visual"].max()
    print("The subject managed to learn " + str(correct_visual) + " Portuguese words from only visual stimuli and made " + str(wrong_visual) + " mistakes on words presented as such.\n")
    if audio_learner:
        audiovisual_learned_visual.append(correct_visual)
        max_facts_seen_audiovisual.append(data["fact_id"].max())
    else:
        visual_learned_visual.append(correct_visual)
        max_facts_seen_visual.append(data["fact_id"].max())


    # Check how many prompts of certain type appeared after 5 minutes and how many the user got correct
    after5min = data[data.start_time > 300000]
    # after5min = (after5min["correct"].ne("False")
    #              .groupby(after5min["audio_or_visual_fact"])
    #              .value_counts()
    #              .unstack(fill_value=0)
    #              .rename(columns={0:"Correct", 1:"Wrong"})
    #              .assign(total=lambda x: x.sum(axis=1))
    #              .reindex(columns=["Total","Correct","Wrong"]))
    # print(after5min)

    s = after5min.groupby("audio_or_visual_fact")["correct"].value_counts()
    # print("S:")
    # print(s)
    # # print("........\n")
    # print(s[0])
    # print(s[1])
    # print(s[2])
    # print(s[3])
    # print("........\n")
    # after5min = after5min.groupby("audio_or_visual_fact")
    # print(after5min.head())
    # correct_audio_5min = after5min["correct_audio_visual"]
    # wrong_audio_5min = after5min["wrong_audio_visual"]
    # correct_visual_5min = after5min["correct_visual"]
    # wrong_visual_5min = after5min["wrong_visual"]
    if audio_learner:
        audiofact_correct_audiolearner_5min.append(s[0])
        visualfact_correct_audiolearner_5min.append(s[2])
        audiofact_wrong_audiolearner_5min.append(s[1])
        visualfact_wrong_audiolearner_5min.append(s[3])
    else:
        audiofact_correct_visuallearner_5min.append(s[0])
        visualfact_correct_visuallearner_5min.append(s[2])
        audiofact_wrong_visuallearner_5min.append(s[1])
        visualfact_wrong_visuallearner_5min.append(s[3])



    # # Plot shit
    # data["start_time"] = data["start_time"] - data["start_time"][0]
    
    # # Choose size of plots:
    # # plt.rcParams["figure.figsize"] = (12,8)
    # plt.rcParams["figure.figsize"] = (8,8)
    # ax = plt.gca()
    # ax.set_ylim([-0.2, 1.2])

    # plt.plot(data["start_time"].div(1000), data["audio_visual_chance"])
    # plt.xlabel("Experiment runtime in seconds")
    # plt.ylabel("Chance prompt being audiovisual")
    # plt.title("Chance of audiovisual prompts over time of subject" + str(subject_nr))
    # subject_nr += 1
    # # plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]
    # plt.show()

    # # Patrick is audiovisual learner
    # if "siert_jan" in subject:
    #     audiovisual_learner_example = data
    # # Christiaan is visual learner
    # if "christiaan" in subject:
    #     visual_learner_example = data

learn_types = ["Visual", "Audiovisual"]
data = [num_visual_learners, num_audiovisual_learners]
plt.bar(learn_types, data)
plt.title("Number of particpants per category")
plt.xlabel("Learn type")
plt.ylabel("Number of participants")
plt.show()

# ax = plt.gca()
# ax.set_ylim([-0.2, 1.2])
# plt.plot(audiovisual_learner_example["start_time"].div(1000), audiovisual_learner_example["audio_visual_chance"], label="audiovisual learner")
# plt.plot(visual_learner_example["start_time"].div(1000), visual_learner_example["audio_visual_chance"], label="visual learner")
# plt.xlabel("Experiment runtime in seconds")
# plt.ylabel("Chance prompt being audiovisual")
# plt.title("Chance of audiovisual prompts over time")
# plt.legend(loc="upper left")

def average(lst):
    return sum(lst) / len(lst)

print("Avg prompts visual learners: " + str(average(visual_num_prompts)))
print("Avg prompts audiovisual learners: " + str(average(audiovisual_num_prompts)))
print("Avg correct visual learners: " + str(average(visual_num_correct)))
print("Avg correct audiovisual learners: " + str(average(audiovisual_num_correct)))
print("Avg wrong visual learners: " + str(average(visual_num_wrong)))
print("Avg wrong audiovisual learners: " + str(average(audiovisual_num_wrong)))
print("Avg visual facts learned visual learners: " + str(average(visual_learned_visual)))
print("Avg audiovisual facts learned visual learners: " + str(average(visual_learned_audiovisual)))
print("Avg visual facts learned audiovisual learners: " + str(average(audiovisual_learned_visual)))
print("Avg audiovisual facts learned audiovisual learners: " + str(average(audiovisual_learned_audiovisual)))
print("Avg unique facts seen by visual learners: " + str(average(max_facts_seen_visual)))
print("Avg unique facts seen by audiovisual learners: " + str(average(max_facts_seen_audiovisual)))
print("Avg facts presented as visual to visual learners: " + str(average(visual_facts_seen_visuallearners)))
print("Avg facts presented as audiovisual to visual learners: " + str(average(audiovisual_facts_seen_visuallearners)))
print("Avg facts presented as visual to audiovisual learners: " + str(average(visual_facts_seen_audiovisuallearners)))
print("Avg facts presented as audiovisual to audiovisual learners: " + str(average(audiovisual_facts_seen_audiovisuallearners)))

print("\nFinal data:\n")

# audio learners
print("After 5 minutes, audio learners had on average " + str(average(audiofact_correct_audiolearner_5min)) + " audio prompts correct and " + str(average(audiofact_wrong_audiolearner_5min)) + " wrong.")
print("After 5 minutes, audio learners had " + str(average(visualfact_correct_audiolearner_5min)) + " visual prompts correct and " + str(average(visualfact_wrong_audiolearner_5min)) + " wrong.")

# visual learners
print("After 5 minutes, visual learners had on average " + str(average(audiofact_correct_visuallearner_5min)) + " audio prompts correct and " + str(average(audiofact_wrong_visuallearner_5min)) + " wrong.")
print("After 5 minutes, visual learners had " + str(average(visualfact_correct_visuallearner_5min)) + " visual prompts correct and " + str(average(visualfact_wrong_visuallearner_5min)) + " wrong.")

plt.show()