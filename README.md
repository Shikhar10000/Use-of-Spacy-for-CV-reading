# Use-of-Spacy-for-CV-reading
<<<<<<< HEAD
This repo  aims to provide a single place to help understand the usage of SpaCy for training and testing Custom Named Entity Recognizer, for identifying different entities in a resume.
=======
This repo  aims to provide a single place to help understand training and usage of SpaCy for NER and while doing that making a CV phaser

>>>>>>> 9a913297d6b31dd7e83f8515776406452b1469af


# Requirments
SpaCy==2.0.18

pdfminer.six

bs4

urllib

pandas


# Usage

Some of the features provided by spaCy are- Tokenization, Parts-of-Speech (PoS) Tagging, Text Classification and Named Entity Recognition.

SpaCy provides an exceptionally efficient statistical system for NER in python, which can assign labels to groups of tokens which are contiguous. It provides a default model which can recognize a wide range of named or numerical entities, which include person, organization, language, event etc. Apart from these default entities, spaCy also gives us the liberty to add arbitrary classes to the NER model, by training the model to update it with newer trained examples.

## Training
For different purposes, different classes are required in order to label the entities in the dataset.
So, for the very same purpose NER model needs to be trained to identify the custom entities required by the user for information gain.

SpaCy requires minimum of 200 examples to train the model

Steps:
1. Load the model
2. Add new entity labels
3. Loop over
4. Save the trained model
5. Test it


### Training Data

Collect your data in the format given in the sample training and test dataset i.e. json
Make sure that training data has enough examples along with their annotations

Clean it making sure there are no leading or trailing white spaces

Now use train.py to train your custom model

  it will train the model on the given data and save all the files required in a "my_model" directory


## Using Trained Model

Move the "my_model to" usage of trained model directory

and run resumeparser.py
  it will run use the model to identify name skills and phone number email id etc..
  you can modify this function to modify what the model is used to recognise

  '''


    def extract_name(string):

     r1 = string

     nlp = spacy.load('my_model')

      doc = nlp(r1)

      for ent in doc.ents:

         if(ent.label_ == 'Name'):

             print(ent.text)

              break

  '''

Pre trained model entity list:-

1.College Name

2.Degree

3.Location

4.Companies worked at

5.Skills

6.Graduation Year

7.Designation

8.Email Address

9.Name
