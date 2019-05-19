# Use-of-Spacy-for-CV-reading
This repo  aims to provide a single place to help understand training and usage of SpaCy for NER and while doing that making a CV phaser



# Requirments
SpaCy==2.0.18

pdfminer.six

bs4 

urllib

pandas 


# Usage

## Training 

### Training Data

Collect your data in the format given in the sample training and test json

Clean it making sure there are no leading or trailing wite spaces

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

1.Collage Name

2.Degree

3.Location

4.Companies worked at 

5.Email Addrress

6.Skills

7.Graduation Year

8.Designation

9.Email Address

10.Name


