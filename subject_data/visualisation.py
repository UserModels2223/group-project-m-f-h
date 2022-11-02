import pandas as pd
import matplotlib.pyplot as plt
import os
import pathlib


directory = pathlib.Path(__file__).parent.resolve()

for subject in os.listdir(directory):
    path = os.path.join(directory, subject)
    if os.path.isfile(path):
        if ".py" in subject:
            continue
        print(subject)

        data = pd.read_csv(subject, index_col=0)
        num_questions = len(data)

        # Basic info
        correct = data["correct"].value_counts()
        print("This subject answered " + str(correct[1]) + " out of " + str(num_questions) + " questions correct and therefore made " + str(correct[0]) + " mistakes.")

        question_type = data["audio_or_visual_fact"].value_counts()
        print("Out of the " + str(num_questions) + " prompts, " + str(question_type[0]) + " were visual and " + str(question_type[1]) + " were audiovisual.")

        correct_audio_visual = data["correct_audio_visual"].max()
        wrong_audio_visual = data["wrong_audio_visual"].max()
        print("The subject managed to learn " + str(correct_audio_visual) + " Portuguese words from audiovisual stimuli and failed to learn " + str(wrong_audio_visual) + " words presented as such.")        

        correct_visual = data["correct_visual"].max()
        wrong_visual = data["wrong_visual"].max()
        print("The subject managed to learn " + str(correct_visual) + " Portuguese words from only visual stimuli and failed to learn " + str(wrong_visual) + " words presented as such.\n")


        # Plot shit
        plt.plot(data["trial"], data["audio_visual_chance"])
        plt.show()