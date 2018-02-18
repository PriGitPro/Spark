import os

import sys


 

# Configure the environment. 

# Set this up to the directory where Spark is installed



 

# Create a variable for our root path

def createConfig():

    SPARK_HOME = os.environ['SPARK_HOME']
    sys.path.insert(0,os.path.join(SPARK_HOME,"python"))

    sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib"))

    sys.path.insert(0,os.path \

     .join(SPARK_HOME,"python","lib","pyspark.zip"))

    sys.path.insert(0,os.path \

     .join(SPARK_HOME,"python","lib","py4j-0.10.4-src.zip"))
    print("spark config ",SPARK_HOME)
    
# Initiate Spark context.
print(createConfig())
  


 