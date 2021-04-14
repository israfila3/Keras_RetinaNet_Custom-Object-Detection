import glob, os


current_dir = "Annotations"

# Percentage of images to be used for the validation set
percentage_val = 10;

# Create and/or truncate train.txt and Val.txt
file_train = open('ImageSets/Main/train.txt', 'w')
file_test = open('ImageSets/Main/val.txt', 'w')

counter = 1
index_test = round(100 / percentage_val)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.xml")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(title + "\n")
    else:
        file_train.write(title + "\n")
        counter = counter + 1
file_train.close()
file_test.close()
