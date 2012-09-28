#Moorpark Poker Parlor Random Table Seating
#Written By Bryan Alcorn
#Version: 1.1

import random;

def Main():
    Tables = numimp("Enter the number of tables: ");
    perTable = numimp("Enter the number of players per table: ");
    numOfMale = numimp("Enter the Number of Male Players: ");
    numOfFemale = numimp("Enter the Number of Female Players: ");
    while((perTable * Tables) != (numOfMale + numOfFemale)):
        print "Your numbers don't add up, try again!";
        Tables = numimp("Enter the number of tables: ");
        perTable = numimp("Enter the number of players per table: ");
        numOfMale = numimp("Enter the Number of Male Players: ");
        numOfFemale = numimp("Enter the Number of Female Players: ");
    MaleNames = []
    FemaleNames = []
    MasterList = range(3);
    
    for x in range(numOfMale):
        name = raw_input("Enter a Male name: ");
        MaleNames.append(name);
    for x in range(numOfFemale):
        name = raw_input("Enter a Female name: ");
        FemaleNames.append(name);
        
    setUp = Round1(MaleNames,FemaleNames,Tables,perTable);
    setUp2d = SetTables(Tables,perTable,setUp);
    print "ROUND 1"
    Format(setUp2d);
    MasterList[0] = setUp2d;
    setUp = Round2(setUp,Tables,perTable);
    setUp = Round2(setUp,Tables,perTable);
    setUp2d = SetTables(Tables,perTable,setUp);
    print "ROUND 2"
    Format(setUp2d);
    MasterList[1] = setUp2d;
    setUp = Round2(setUp,Tables,perTable);
    setUp2d = SetTables(Tables,perTable,setUp);
    print "ROUND 3"
    Format(setUp2d);
    MasterList[2] = setUp2d;
    write(MasterList,"Tables.csv",Tables,perTable);


def Round1(Array1,Array2,Tables,perTable):
    setUp = []; usedNumx = []; usedNumy = [];
    M = len(Array1);F = len(Array2);
    if(M > F):
        while(M > F):
            x = random.randint(0,len(Array1)-1);
            if(x  in usedNumx):
                x = random.randint(0,len(Array1)-1);
            else:
                setUp.append(Array1[x]);
                usedNumx.append(x);
                M-=1;
    elif(F > M):
        while(F>M):
            y = random.randint(0,len(Array2)-1);
            if(y in usedNumy):
                y = random.randint(0,len(Array1)-1);
            else:
                usedNumy.append(y);
                setUp.append(Array2[y]);
                F-=1;
    else:
        pass;
    while(True):
        x = random.randint(0,len(Array1)-1);
        y = random.randint(0,len(Array2)-1);
        if((x  in usedNumx) or (y in usedNumy)):
            x = random.randint(0,len(Array1)-1);
            y = random.randint(0,len(Array2)-1);
        else:
            usedNumx.append(x);
            usedNumy.append(y);
            setUp.append(Array1[x]);
            setUp.append(Array2[y]);
            if(len(setUp) == (len(Array1) + len(Array2))):
                return setUp;

def Round2(Array,Tables,perTable):
     usedNums = []; a = len(Array)-1;count = 0; b = 0;
     setUp = range(len(Array));
     
     if(a%2 == 0):
         while(True):
             setUp[count] = Array[b];
             b +=1;
             count +=1;
             setUp[count] = Array[a];
             a -= 1;
             count +=1;
             if(b == len(Array)/2):
                 setUp[count] = Array[b];
                 break;
     else:
         while(True):
             if(count >= len(setUp)-1):
                 break;
             setUp[count] = Array[b];
             b +=1;
             count +=1;
             setUp[count] = Array[a];
             a -= 1;
             count +=1;
     return setUp;

def SetTables(Tables,perTable,Array):
    setUp = range(Tables); count = 0;
    for a in range(Tables):
        setUp[a] = range(perTable);

    for x in range(Tables):
        for y in range(perTable):
            setUp[x][y] = Array[count];
            count +=1;
    return setUp;

def numimp(prompt):
    x = raw_input(prompt);
    if(x.isdigit()):
        return int(x);
    else:
        while(x.isdigit() == False):
            print "Enter a number!"
            x = raw_input(prompt);
        return int(x);

def Format(Array2d):
    for a in range(len(Array2d)):
        print "Table " + str(a+1) + ": ",Array2d[a]

def write(List, fileName,Tables,perTable):
    outFile = open(fileName, 'w');
    for a in range(len(List)):
        for b in range(Tables):
           for c in range(perTable):
                List[a][b][c] = str(List[a][b][c]);
    for a in range(len(List)):
        print >> outFile, "Round ",a+1;
        for Person in List[a]:
            string = ','.join(Person);
            print >> outFile, string;
    outFile.close();

Main();
input("Press Enter to quit");
