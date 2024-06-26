# Pi calculation using MapReduce
# Description

<img width="500" alt="image" src="https://user-images.githubusercontent.com/93315926/194803849-7c4c723f-81a1-48ef-b068-12dd25496823.png">

# Design

* Step 1: Generate an input file to the Pi MapReduce program
    * Step 1.1: Create a regular Java program which accepts two command line arguments.
    * R: The radius
    * N: The number of (x, y) pairs to create
    The Java program then randomly generates N pairs of (x, y) and displays them on the standard output.
  Step 1.2: Run the program created in Step 1.1 and save the result in a file. The file is the input to Step 2's Pi MapReduce program.

* Step 2: Create a MapReduce program to calculate the numbers of inside darts and outside darts.
* Step 3: Use the file generated in Step 1.2 as the input to execute the MapReduce program created in Step 2
* Step 4: Calculate Pi in the driver program based on the numbers of inside darts and outside darts.

# Implement

## Requirment

* GCP Environment


* Hadoop environment


* Java environment

## Prepare input data
```
  $ mkdir PiCalculation
  $ cd PiCalculation
  $ vi GenerateRandomNumbers.java
  $ javac GenerateRandomNumbers.java
  $ java -cp . GenerateRandomNumbers
```

Input data will store in PiCalculationInput

## Setup passphraseless ssh
Now check that you can ssh to the localhost without a passphrase:
```
  $ cd hadoop-3.4.0/
  $ ssh localhost
```
If you cannot ssh to localhost without a passphrase, execute the following commands:
```
  $ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
  $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
  $ chmod 0600 ~/.ssh/authorized_keys
```

## Make the HDFS directories required to execute MapReduce jobs(Copy input data to HDFS)
```
  $ cd ..
  $ cd hadoop-3.4.0/
  $ bin/hdfs namenode -format
  $ sbin/start-dfs.sh
  $ wget http://localhost:9870/
  $ bin/hdfs dfs -mkdir /user
  $ bin/hdfs dfs -mkdir /user/nseghid8444
  $ bin/hdfs dfs -mkdir /user/username/picalculate
  $ bin/hdfs dfs -mkdir /user/username/picalculate/input
  $ bin/hdfs dfs -put ../PiCalculation/PiCalculationInput /user/username/picalculate/input
```
> If you can not copy input into hadoop dictionary, please restart the virtual machine.

## Prepare code

* Build PiCalculation java file
```
  $ cd /hadoop-3.4.0
  $ vi PiCalculation.java      
```

* Compile PiCalculation.java and create a jar
```
  $ bin/hadoop com.sun.tools.javac.Main PiCalculation.java
  $ jar cf wc.jar PiCalculation*class  
```

## Run

* Execute
```
  $ bin/hadoop jar wc.jar PiCalculation /user/username/picalculate/input /user/username/picalculate/output5
```

* Output
```
  $ bin/hdfs dfs -ls /user/username/picalculate/output5
  $ bin/hdfs dfs -cat /user/username/picalculate/output5/part-r-00000 
```

* Stop
```
  $ sbin/stop-dfs.sh
```

## Test Result

Test Case:

How many random numbers to generate: 1000000
Radius = 200

<img width="700" alt="image" src="https://user-images.githubusercontent.com/93315926/194802159-668eb99d-39c7-4feb-b0ee-1921e827bf41.png">

## Detail Design Presentation
[Pi calculation using MapReduce](https://docs.google.com/presentation/d/1thjbG_JBTAl9nfgU4DVH6SQ13RW8-FIMdpJiCKz0ttQ/edit?usp=sharing)

# Appendix
