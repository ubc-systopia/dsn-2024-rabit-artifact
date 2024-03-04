# The script works, but currently I haven't refactor the code yet. 

from dis import dis
from glob import glob
from ntpath import join
from operator import truediv
import sys
from tkinter.colorchooser import askcolor
from turtle import position, speed
import os
import pickle
import math3d
from hein_robots.robotics import Location, Orientation

file_path = os.path.dirname(os.path.abspath(__file__))

# Path to the cps-security-code (aka project niraapad) git repo
niraapad_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(r"python-urx-master")
import urx

import time


import getopt
import argparse
from datetime import datetime
import time
import logging
import os
import json
import csv
import numpy

isApprixi=0

approxiThr=5


t = time.process_time()
ids_signal = 0

import os
import tkinter as tk
from tkinter import ttk
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=("Verdana", 10))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


class boxes:
    boxesList=[]
#
class last:
    start=2
    lastPosX=0
    lastPosY=0
    lastPosZ=0
    lastSpeed=0
    list0=[]
    #list1=[]
    #list2=[]
    adjustedArmPos=[]

lastInfo=last()
    
loNamesOfObjects=[]
numSec=1
acceLimit=1000
speedLimit=1000
wallInfo=[99999,-99999,99999,-350]#north(x > 0) south(x < 0) east(y > 0) west(y > 0)

# boxList=[[50,50,50,1,2,3],[50,70,00,9,8,1]]
ipAdd="192.168.48.128"
terminateOrNotInCaseOfOverlapping=[]
okCUrrently=1
predictNumSec=1

needPopUp=0
lengtghGrip=20
import math




def getTcpSpeed(tcpPosXYZ):
    dx=tcpPosXYZ[0]-lastInfo.lastPosX
    dy=tcpPosXYZ[1]-lastInfo.lastPosY
    dz=tcpPosXYZ[2]-lastInfo.lastPosZ
    speed=math.sqrt(dx*dx+dy*dy+dz*dz)   
    return speed

def getTcpAcce(tcpSpeed):
    ds=tcpSpeed-lastInfo.lastSpeed
    # print('ds')
    # print(ds)
    return ds

def updatelast(tcpPosXYZ,tcpSpeed):
    lastInfo.lastPosX=tcpPosXYZ[0]
    lastInfo.lastPosY=tcpPosXYZ[1]
    lastInfo.lastPosZ=tcpPosXYZ[2]
    lastInfo.lastSpeed=tcpSpeed

def withInBoundSoeed(tcpSpeed,speedLimit):
    # print('abs(tcpSpeed)')
    # print(abs(tcpSpeed))
    # print('speedLimit')
    # print(speedLimit)
    # print('abs(tcpSpeed))<=speedLimit')
    # print(abs(tcpSpeed)<=speedLimit)

    if( (abs(tcpSpeed))<=speedLimit):
        return True
    return False

def withInBoundAcce(tcpAcce,acceLimit):
    if (abs(tcpAcce))<= acceLimit:
        return True
    return False

import math
import pandas


def transformation2(alpha,beta,gama,transMat,original):
  # unfinished untested


  original=original.add(transMat)#([[xt],[yt],[zt],[0]]))
  transitionfram=pandas.DataFrame([[math.cos(alpha)*math.cos(beta),
  math.cos(alpha)*math.sin(beta)*math.sin(gama)-math.sin(alpha)*math.cos(gama),
  math.cos(alpha)*math.sin(beta)*math.cos(gama)+math.sin(alpha)*math.sin(gama),0],
  [math.sin(alpha)*math.cos(beta),
  math.sin(alpha)*math.sin(beta)*math.sin(gama)+math.cos(alpha)*math.cos(gama),
  math.sin(alpha)*math.sin(beta)*math.cos(gama)-math.cos(alpha)*math.sin(gama),0],
  [-math.sin(beta),math.cos(beta)*math.sin(gama),math.cos(beta)*math.cos(gama),0],[0,0,0,1]])

  #transitionfram=transitionfram.T#need?
  #print(transitionfram)

  

  temp= transitionfram.dot(original)

  return temp

def transform6(l1,a1x,a1y,a1z,l2,a2x,a2y,a2z,l3,a3x,a3y,a3z,l4,a4x,a4y,a4z,l5,a5x,a5y,a5z,l6,a6x,a6y,a6z):
  posList=[]
  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  c=0
  for x in posList:
#    posList[c]=transformation2(a1x,a1y,a1z,l1[0],l1[1],l1[2],posList[c])
    posList[c]=transformation2(a1x,a1y,a1z,l1,posList[c])
    c+=1





  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  l6adjust=pandas.DataFrame([0,-0,0,0])
  c=0
  for x in posList:
    posList[c]=transformation2(0,0,0,l6adjust,posList[c])
    c+=1






  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  c=0
  for x in posList:
    posList[c]=transformation2(a2x,a2y,a2z,l2,posList[c])
    c+=1



  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  l6adjust=pandas.DataFrame([0,-0,0,0])
  c=0
  for x in posList:
    posList[c]=transformation2(0,0,0,l6adjust,posList[c])
    c+=1



  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  c=0
  for x in posList:
    posList[c]=transformation2(a3x,a3y,a3z,l3,posList[c])
    c+=1




  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  #l6adjust=pandas.DataFrame([0,-15,0,0])
  #l6adjust=pandas.DataFrame([0,-80,0,0])
  l6adjust=pandas.DataFrame([0,-83,0,0])
  c=0
  for x in posList:
    posList[c]=transformation2(0,0,0,l6adjust,posList[c])
    c+=1








  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  c=0
  for x in posList:
    posList[c]=transformation2(a4x,a4y,a4z,l4,posList[c])
    c+=1



  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  #l6adjust=pandas.DataFrame([0,15,0,0])
  #l6adjust=pandas.DataFrame([0,80,0,0])
  l6adjust=pandas.DataFrame([0,93,0,0])
  c=0
  for x in posList:
    posList[c]=transformation2(0,0,0,l6adjust,posList[c])
    c+=1







  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  c=0
  for x in posList:
    posList[c]=transformation2(a5x,a5y,a5z,l5,posList[c])
    c+=1

  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  #l6adjust=pandas.DataFrame([0,-20,0,0])
  l6adjust=pandas.DataFrame([0,-120,0,0])
  c=0
  for x in posList:
    posList[c]=transformation2(0,0,0,l6adjust,posList[c])
    c+=1


  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
  c=0
  for x in posList:
    posList[c]=transformation2(a6x,a6y,a6z,l6,posList[c])
    c+=1
  pos=pandas.DataFrame([0,0,0,0])
  posList.append(pos)
#   print('firstposList ')
#   print(posList[0])
  return pos,posList



def getAllIntermediatePts(xData,yData,zData):
  numPtInBetween=50
  lengthData=len(xData)
  #print(lengthData)
  #print('lengthData')

  res=[]
  c=0
  while c<11:
    c+=1
    newList=[[],[],[],[]]
    
    res.append(newList)
  
  c=1
  while c<lengthData:
    xDiff=xData[c]-xData[c-1]
    yDiff=yData[c]-yData[c-1]
    zDiff=zData[c]-zData[c-1]
    c2=0
    while c2<numPtInBetween:
      res[c-1][0].append(xData[c-1]+c2/numPtInBetween*xDiff)
      res[c-1][1].append(yData[c-1]+c2/numPtInBetween*yDiff)
      res[c-1][2].append(zData[c-1]+c2/numPtInBetween*zDiff)
      res[c-1][3].append(c)
      c2+=1
    c+=1
  lengthData=len(xData)
  #print(lengthData)
  #print('lengthData after')
  return res

def isWithInTwo(num1,num2):
  if(num1 == num2):
    return True
  if(num1 == (num2+1)):
    return True
  if(num1 == (num2-1)):
    return True
  if(num1 == (num2+2)):
    return True
  if(num1 == (num2-2)):
    return True
  return False

def isAllPtFarEnough(newLox,newLoy,newLoz, newLon,safetyDistance):
  length=len(newLox)
  
  c1=0
  while c1<length:
    c2=0
    while c2<length:
      xDiff=newLox[c1]-newLox[c2]
      yDiff=newLoy[c1]-newLoy[c2]
      zDiff=newLoz[c1]-newLoz[c2]
      distancebetweenTwoPt=math.sqrt(xDiff*xDiff+yDiff*yDiff+zDiff*zDiff)
      if ((distancebetweenTwoPt<safetyDistance) & (isWithInTwo(newLon[c1],newLon[c2]) == False)):
        #print('too close')
        #print(distancebetweenTwoPt)
        #print(newLon[c1])
        #print(newLon[c2])
        return False
      c2+=1
    c1+=1
  return True



def extractAsSingleLists(prevRes):
  lox=[]
  loy=[]
  loz=[]
  loArmNum=[]
  c=0
  while c<len(prevRes):#6:
    lox=lox+prevRes[c][0]
    loy=loy+prevRes[c][1]
    loz=loz+prevRes[c][2]
    loArmNum=loArmNum+prevRes[c][3]
    c+=1

  return lox, loy, loz, loArmNum

def lolointToloInt(loloi):
    new=[]
    for i,x in enumerate(loloi):
        new.append(float(x[0]))
    return new    
def extractAsSingleListsForXYZ(prevRes):
    #print('prevRes')
    #print(type(prevRes))
    #print(prevRes)
    #print('prevRes 0')
    #print(type(prevRes[0]))
    #print(prevRes[0])
    lox=[]
    loy=[]
    loz=[]
    for x in prevRes:
        x=x.values.tolist()
        #print('x')
        #print(x)
        x=lolointToloInt(x)
        #print('x')
        #print(x)
        lox.append(x[0])
        loy.append(x[1])
        loz.append(x[2])
    return lox, loy, loz


def notCollideWithItSelf(jointPosCart):


    xdata=[]
    ydata=[]
    zdata=[]

    poslistTolist=[]
    for x in jointPosCart:
        poslistTolist.append(x.values.tolist())

    for x in poslistTolist:
        xdata.append(x[0][0])

    for x in poslistTolist:
        ydata.append(x[1][0])#
    for x in poslistTolist:
        zdata.append(x[2][0])#[



    res=getAllIntermediatePts(xdata,ydata,zdata)
    newLox,newLoy,newLoz, newLon=extractAsSingleLists(res)


    checkFarEnough=isAllPtFarEnough(newLox,newLoy,newLoz, newLon,50)


    return checkFarEnough






def getBoxPts(boxList):
    retList=[]
    for box in boxList:
        for i0 in range(box[0],box[0]+box[3],1):
            for i1 in range(box[1],box[1]+box[4],1):
                for i2 in range(box[2],box[2]+box[5],1):
                    newPos=[i0,i1,i2]
                    retList.append(newPos)
    return retList        


    angle=30/180*3.14
    a=angle
    a2=1.6


def getJointPosCart(jointPos):
    base=jointPos[0]
    shoulder=jointPos[1]
    elbow=jointPos[2]
    wrist1=jointPos[3]
    wrist2=jointPos[4]
    wrist3=jointPos[5]
    #l=pandas.DataFrame([0,0,30,0])
    #l10=pandas.DataFrame([0,0,10,0])
    #l5=pandas.DataFrame([5,0,0,0])

    #l30=pandas.DataFrame([0,0,30,0])
    #l50=pandas.DataFrame([0,0,50,0])
    #l5=pandas.DataFrame([0,0,5,0])
    l=pandas.DataFrame([0,0,30,0])
    l10=pandas.DataFrame([0,0,10,0])
    l5=pandas.DataFrame([5,0,0,0])

    l30=pandas.DataFrame([0,0,30,0])
    l50=pandas.DataFrame([0,0,50,0])
    l5=pandas.DataFrame([0,0,5,0])

    l150=pandas.DataFrame([0,0,150,0])
    l120=pandas.DataFrame([0,0,120,0])
    l250=pandas.DataFrame([0,0,250,0])
    l210=pandas.DataFrame([0,0,210,0])
    l80=pandas.DataFrame([0,0,80,0])
    l60=pandas.DataFrame([0,0,60,0])

    l152=pandas.DataFrame([0,0,152,0])
    l250=pandas.DataFrame([0,0,250,0])
    l244=pandas.DataFrame([0,0,244,0])
    l213=pandas.DataFrame([0,0,213,0])
    l83=pandas.DataFrame([0,0,83,0])
    l82=pandas.DataFrame([0,0,82,0])
    l93=pandas.DataFrame([0,0,93,0])
    l31=pandas.DataFrame([0,0,31,0])

    #base=0
    negForBase=-base

    #shoulder=-60/180*3.14
    neg90negForShoulder=-90/180*3.14-shoulder

    #elbow=-30/180*3.14
    negForElbow=-elbow

    #wrist1=-60/180*3.14
    neg90negForWrist1=-90/180*3.14-wrist1


    angle90=90/180*3.14


    #wrist2=30/180*3.14
    #wrist3=90/180*3.14
    negForWrist3=-wrist3


    #pos,poslist=transform6(l5,negForWrist3,0,-0,l10,wrist2,0,angle90,l10,0,neg90negForWrist1,0,l50,0,negForElbow,0,l50,0,neg90negForShoulder,0,l30,negForBase,0,0)
    #pos,poslist=transform6(l60,negForWrist3,0,-0,l80,wrist2,0,angle90,l80,0,neg90negForWrist1,0,l210,0,negForElbow,0,l250,0,neg90negForShoulder,0,l150,negForBase,0,0)
    pos,poslist=transform6(l31,negForWrist3,0,-0,l83,wrist2,0,angle90,l83,0,neg90negForWrist1,0,l213,0,negForElbow,0,l244,0,neg90negForShoulder,0,l152,negForBase,0,0)

    return poslist

def customizeCheck():
    return True


def aboveGround(jointPosCart):
    global lastInfo



    # print('lastInfo.lastPosZ')
    # print(lastInfo.lastPosZ)
    
    #return (lastInfo.lastPosZ>0)
    if(lastInfo.lastPosZ<0):
        return False

    ajArmPos=lastInfo.adjustedArmPos
    if(ajArmPos==[]):
        #print('waiting for adArmPos')
        return True


    for i,pos in enumerate(ajArmPos):
        posX=pos[0]
        posY=pos[1]
        posZ=pos[2]
        if(posZ<0):
            # print('below ground')
            # print(i)
            # print(posZ)
            return False


    return True







    ###
    return
    for pos in jointPosCart:
        #print(pos)
        #print(type(pos))
        pos=pos.values.tolist()
        #print(pos)
        #print(type(pos))
        print('pos[2][0]')
        print(pos[2][0])
        if(pos[2][0]<0):
            return False
        return True

def withinLimitOfWall(jointPosCart,wallInfo,armPosList,tcpPosXYZ):


    adjustedArmPos=corrArmPosByTcp(armPosList,tcpPosXYZ)

    global lastInfo
    lastInfo.adjustedArmPos=armPosList

    for i,pos in enumerate(adjustedArmPos):
        posX=pos[0]
        posY=pos[1]
        posZ=pos[2]
        if(posX>wallInfo[0]):
            print('overlap with north wall')
            print(wallInfo[0])
            return False
        if(posX<wallInfo[1]):
            print('overlap with south wall')
            print(wallInfo[1])
            return False
        if(posY>wallInfo[2]):
            print('overlap with east wall')
            print(wallInfo[2])
            return False
        if(posY<wallInfo[3]):
            print('overlap with west wall')
            print(wallInfo[3])
            return False
        
    return True

    for pos in jointPosCart:
        pos=pos.values.tolist()
        print('pos withinLimitOfWall')
        print(pos)
        if(pos[0][0]>wallInfo[0] ):
            print('overlap with north wall')
            print(wallInfo[0])
            return False
        if(pos[0][0]<wallInfo[1] ):
            print('overlap with south wall')
            print(wallInfo[1])
            return False
        if(pos[1][0]>wallInfo[2] ):
            print('overlap with east wall')
            print(wallInfo[2])
            return False
        if(pos[1][0]<wallInfo[3] ):
            print('overlap with west wall')
            print(wallInfo[3])
            return False    
    return True

def tooClose(boxPos,jointPos,thr):
    #print('tooclose')
    #print(type(boxPos))

    #print(type(jointPos))
    jointPos=jointPos.values.tolist()
    #print(type(jointPos))

    dx=(boxPos[0]-jointPos[0][0])
    dy=(boxPos[1]-jointPos[1][0])
    dz=(boxPos[2]-jointPos[2][0])
    dist=dx*dx+dy*dy+dz*dz
    return (dist<thr)


def isTooCLoseToBox(boxOccupiedPosList,jointPosCart):
    for boxPos in boxOccupiedPosList:
        #boxPos=boxPos.values.tolist()

        for i,jointPos in enumerate( jointPosCart):
            if tooClose(boxPos,jointPos,thr=45):
                # print('box num')
                # print(i)
                # print(boxPos)
                return True
    return False

class c:
    count=0
    List=[]
    resultList=[]

c1=c()

def fetch(entries):
    global c1
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        #print('%s: "%s"' % (field, text)) 
        if(c1.count==0):
            c1.List=[]
        c1.List.append(text)
        c1.count+=1
        if(c1.count==5):
            c1.resultList.append(c1.List)
        #print('in fetch')

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

def virtualizeBoxAndArm(boxList,jointPosCart):
   pass 


def isOutSideBox(box,pos,thr):
    
    if (pos[0]+thr)<box[0]:
        return True
    if (pos[0]-thr)>box[0]+box[3]:
        return True
    if (pos[1]+thr)<box[1]:
        return True
    if (pos[1]-thr)>box[1]+box[4]:
        return True
    if (pos[2]+thr)<box[2]:
        return True
    if (pos[2]-thr)>box[2]+box[5]:
        return True
    return False

def isInSideAnyBox(pos,boxList):
    
    for box in boxList:
        #print('pos box')
        #print(type(box))
        #print((box))
        #print(type(pos))
        #print((pos))
        if isOutSideBox(box,pos,0)==False:
            return True
    return False


def isTooCLoseToBoxWithIntermediaPos(boxList,jl):
    #print('jl')
    #print(jl)
    for i,pos in enumerate( jl):
        if isInSideAnyBox(pos,boxList):
            return True
        return False

def reformatLoxLoyLozLonToRefoamteedLoXYZ(jointPosCartWithIndermediatePos):
    tempList=[]
    #print('jointPosCartWithIndermediatePos')
    #print(jointPosCartWithIndermediatePos)
    lox=jointPosCartWithIndermediatePos[0]
    loy=jointPosCartWithIndermediatePos[1]
    loz=jointPosCartWithIndermediatePos[2]
    #print('lox')
    #print(lox)
    for i,x in enumerate(lox):
        tempList.append([lox[i],loy[i],loz[i]])
    return tempList

def mergeLoxLoyLoz(lox,loy,loz):
    new=[]
    for i,x in enumerate(lox):
        new.append([lox[i],loy[i],loz[i]])
    return new


def getBoxBounds(x):
    # print(" in getBoxBounds")
    # print(x)
    y=[0,0,0,0,0,0]
    y[0]=x[0]
    y[1]=x[1]
    y[2]=x[2]
    y[3]=x[0]+x[3]
    y[4]=x[1]+x[4]
    y[5]=x[2]+x[5]

    return y


def getBoxBoundsForList(boxList):
    # print("boxList in getBoxBoundsForList")
    # print(boxList)
    boxBoundList=boxList.copy()
    for i,x in enumerate(boxList):
        boxBoundList[i]=getBoxBounds(x)
    return boxBoundList

def isInBoundForABox(x,tcpPos):
    # print("x inisInBoundForABox ")
    # print(x)    
    # print("tcpPos inisInBoundForABox ")
    # print(tcpPos)


    t0=tcpPos[0]*1000
    t1=tcpPos[1]*1000
    t2=tcpPos[2]*1000


    if(x[0]>=t0):
        return False
    if(x[3]<=t0):
        return False
    if(x[1]>=t1):
        return False
    if(x[4]<=t1):
        return False
    if(x[2]>=t2):
        return False
    if(x[5]<=t2):
        return False
    # if( ( (x[0]>=())  or (x[3]>=(tcpPos[0]*1000)) ) == True):
    #     print("1 false")
    #     return False
    # if( ( (x[1]>=(tcpPos[1]*1000))  or (x[4]>=(tcpPos[1]*1000)) ) == True):
    #     print("2 false")

    #     return False
    # if( ( (x[2]>=(tcpPos[2]*1000))  or (x[5]>=(tcpPos[2]*1000)) ) == True):        
    #     print("3 false")

    return True


def notCollideWithOtherObjectUsingTcp(boxList,tcpPos):
    boxBoundaries=getBoxBoundsForList(boxList)
    # print("boxBoundaries")
    # print(boxBoundaries)
    for i,x in enumerate(boxBoundaries):
        if (   (isInBoundForABox(x,tcpPos)) and (terminateOrNotInCaseOfOverlapping[i]==1)   ):
            print("collided with box number")

            print(i)
            #popupmsg("Collided with box number "+str(i)+', which is '+str(loNamesOfObjects[i]) + " .")


            return False
        if (   (isInBoundForABox(x,tcpPos)) and (terminateOrNotInCaseOfOverlapping[i]==0)   ):
            popupmsg("(no need to stop) Overlapped with box number "+str(i)+', which is '+str(loNamesOfObjects[i]) + " .")


    return True

def addCurrentOverlappingInformation(theOverlappingHistory,boxList,tcpPos):  
    boxBoundaries=getBoxBoundsForList(boxList)


    listOfOverlapping=[]
    for i,x in enumerate(boxBoundaries):
        if (   isInBoundForABox(x,tcpPos) ):
            listOfOverlapping.append(1)
        listOfOverlapping.append(0)
    theOverlappingHistory.append(listOfOverlapping)
    return theOverlappingHistory



def notCollideWithOtherObject(boxInfo,jointPosCart):




    #boxOccupiedPosList=getBoxPts(boxList)
    #isTooClose=isTooCLoseToBox(boxOccupiedPosList,jointPosCart)
    #print('jointPosCart  notCollideWithOtherObject')
    #print(type(jointPosCart))
    #print(jointPosCart)
    xdata,ydata,zdata=extractAsSingleListsForXYZ(jointPosCart)
    # print('xdata  notCollideWithOtherObject')
    # print(type(xdata))
    # print(xdata)
    jointPosCartWithIndermediatePos=getAllIntermediatePts(xdata,ydata,zdata)
    # print('jointPosCartWithIndermediatePos  notCollideWithOtherObject')
    # print(type(jointPosCartWithIndermediatePos))
    # print(jointPosCartWithIndermediatePos)
    newLox,newLoy,newLoz, newLon=extractAsSingleLists(jointPosCartWithIndermediatePos)
    # print('newLox  notCollideWithOtherObject')
    # print(type(newLox))
    # print(newLox)
    # print('newLoy  notCollideWithOtherObject')
    # print(type(newLoy))
    # print(newLoy)
    #jointPosCartWithIndermediatePosRefoamtatted=reformatLoxLoyLozLonToRefoamteedLoXYZ(jointPosCartWithIndermediatePos)
    mergeedLoxLoyLoz=mergeLoxLoyLoz(newLox,newLoy,newLoz)

    # print('mergeedLoxLoyLoz')
    # print(mergeedLoxLoyLoz)

    lastInfo.list0=mergeedLoxLoyLoz



    isTooClose=isTooCLoseToBoxWithIntermediaPos(boxList,mergeedLoxLoyLoz)
    if(isTooClose == False):
        return True

    virtualizeBoxAndArm(boxList,jointPosCart)
    return False

def isFutureOk(tcpPosXYZ,tcpSpeed,numSec):
    #return True,0
    dx=tcpPosXYZ[0]-lastInfo.lastPosX
    dy=tcpPosXYZ[1]-lastInfo.lastPosY
    dz=tcpPosXYZ[2]-lastInfo.lastPosZ
    #print('lastInfo.lastPosZ')
    #print(lastInfo.lastPosZ)
    waitTime=0.5
    x=dx*numSec/waitTime+tcpPosXYZ[0]
    y=dy*numSec/waitTime+tcpPosXYZ[1]
    z=dz*numSec/waitTime+tcpPosXYZ[2]
    # print('x,y,z')
    # print(x,y,z)
    x*=1000
    y*=1000
    z*=1000

    if z<0:
        return False,1
    if x>wallInfo[0]:
        return False,2
    if x<wallInfo[1]:
        return False,3
    if y>wallInfo[2]:
        return False,4
    if y<wallInfo[3]:
        return False,5

    global isApprixi
    isApprixi=0
    global approxiThr
    if tcpPosXYZ[2]*1000<(0+approxiThr):
        isApprixi=1
        return False,-1
    if (tcpPosXYZ[0]*1000+approxiThr)>wallInfo[0]:
        isApprixi=1
        return False,-1
    if (tcpPosXYZ[0]*1000-approxiThr)<wallInfo[1]:
        isApprixi=1
        return False,-1
    if (tcpPosXYZ[1]*1000+approxiThr)>wallInfo[2]:
        isApprixi=1
        return False,-1
    if (tcpPosXYZ[1]*1000-approxiThr)<wallInfo[3]:
        isApprixi=1
        return False,-1  




    return True,0

from tkinter import simpledialog

def getConfigFromGui():
    data=dict()
    import tkinter as tk

    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    speedLimit = simpledialog.askstring(title="Set Speed Limit",
                                    prompt="What is the speed limit for this run?")

    # check it out
    # print("sppeed limit", speedLimit)
    import tkinter as tk
    ip = simpledialog.askstring(title="Set ip",
                                    prompt="What is the ip add for simulator for this run?") 
                        
    # print("ip", ip)
    accLimit = simpledialog.askstring(title="Set Accelerate Limit",
                                    prompt="What is the Accelerate limit for this run?")
    # print("Accelerate limit", speedLimit)

    south = simpledialog.askstring(title="Wall in South",
                                    prompt="Position of Wall in South? (Leave empty if there is no wall at south)")
    print( south)


    north = simpledialog.askstring(title="Wall in North",
                                    prompt="Position of Wall in North? (Leave empty if there is no wall at North)")
    print( north)


    east = simpledialog.askstring(title="Wall in East",
                                    prompt="Position of Wall in East? (Leave empty if there is no wall at East)")
    print( east)


    west = simpledialog.askstring(title="Wall in West",
                                    prompt="Position of Wall in West? (Leave empty if there is no wall at West)")
    print( west)
    pre = simpledialog.askstring(title="predictTime",
                                    prompt="For how long do you wants to predict?(seconds) (Leave empty if you do not want to see warming of potential invalid position for future)")
    # print( pre)
    data['ipAdd']=ip
    data['predictTime']=pre
    data['speedLimit']=speedLimit
    data['accelerationLimit']=accLimit
    data['northWall']=north
    data['southWall']=south
    data['eastWall']=east
    data['westWall']=west
    data['boxInfo']=getBoxInfoFromGui()
    # print('data from gui')
    # print(data)
    return data



def convertToList(l):
    # print('l')
    # print(l)
    if(l == [] or l == [[]]):
        return []
    temp=l[0]
    print('temp')
    print(temp)
    for i,x in enumerate( temp):
        
        try:
            temp[i]=int(x)
        except:
            temp[i]=0
    boxList=[]
    tempBoxList=[]
    c=0
    for i,x in enumerate(temp):
        #print('tempBoxList')
        #print(tempBoxList)        
        #print('x')
        #print(x)
        tempBoxList.append(x)
        #print('tempBoxList')
        #print(tempBoxList) 
        c+=1
        if(c%6==0 and c!=0):
            boxList.append(tempBoxList)
            tempBoxList=[]
    # print('boxList')
    # print(boxList)

    return boxList


def getBoxInfoFromGui():
    fields = 'X position', 'Y position', 'Z position', 'Length', 'Width', 'Height'

    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Enter Next',
                    command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='No Other Data Needs Entering', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
    # print(c1.resultList)

    toReturn=convertToList(c1.resultList)
    # print('toReturn')
    # print(toReturn)
    return toReturn



import json

def getConfig():
        
    try:
        # Opening JSON file
        #print(file_path)
        f = open(file_path + '\\jsonFileForRules.json')
        #print('found file')
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        # list
        #for i in data['option']:
        # print(i)
       # print(data)
        # Closing file
        f.close()


        #print(data["speedLimit"])
        #popupmsg('imported')
        return data
        
    except:
        exit()
        # popupmsg('No configuration file found, no data has been imported, please enter limit information in the input boxes.')

        # print('fail to load get from GUI')

        # return getConfigFromGui()


def addZeroIfNeededAndStringfy(i):
    if i == '':
        i=0
    return float(i)

def addInfIfNeededAndStringfy(i):
    if i == '':
        i=999999999999999999990000000
    return float(i)

def addNegInfIfNeededAndStringfy(i):
    if i == '':
        i=-99999999999999999999000000
    return float(i)

def handleInvalidInput(configDict):
    configDict['northWall']=addInfIfNeededAndStringfy(configDict['northWall'])
    configDict['southWall']=addNegInfIfNeededAndStringfy(configDict['southWall'])
    configDict['eastWall']=addInfIfNeededAndStringfy(configDict['eastWall'])
    configDict['westWall']=addNegInfIfNeededAndStringfy(configDict['westWall'])
    configDict['speedLimit']=addInfIfNeededAndStringfy(configDict['speedLimit'])
    configDict['accelerationLimit']=addInfIfNeededAndStringfy(configDict['accelerationLimit'])
    configDict['predictTime']=addZeroIfNeededAndStringfy(configDict['predictTime'])
    return configDict

def setConfig():
    configDict=getConfig()
    global boxList
    global wallInfo
    global acceLimit
    global speedLimit
    global numSec
    global ipAdd
    global loNamesOfObjects
    global terminateOrNotInCaseOfOverlapping
    configDict=handleInvalidInput(configDict)
    ipAdd=configDict['ipAdd']
    boxList=configDict['boxInfo']
    
    wallInfo[0]=float(configDict['northWall'])
    wallInfo[1]=float(configDict['southWall'])
    wallInfo[2]=float(configDict['eastWall'])
    wallInfo[3]=float(configDict['westWall'])
    speedLimit=float(configDict['speedLimit'])
    acceLimit=float(configDict['accelerationLimit'])
    numSec=float(configDict['predictTime'])
    loNamesOfObjects=configDict['namesOfObjects']
    terminateOrNotInCaseOfOverlapping=configDict['terminateOrNotInCaseOfOverlapping']
    #wallInfo[0]=float(wallInfo[0])
    #wallInfo[1]=float(wallInfo[1])
    #wallInfo[2]=float(wallInfo[2])
    #wallInfo[3]=float(wallInfo[3])
    #speedLimit=float(speedLimit)
    #acceLimit=float(acceLimit)
    #numSec=float(numSec)
    # print("boxList in setConfig")
    # print(boxList)

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt



def seprateXYZ(armPos):
    #print(type(armPos))
    x=[]
    y=[]
    z=[]
    for i,e in enumerate(armPos):
        x.append(e[0])
        y.append(e[1])
        z.append(e[2])
    return x,y,z



def seprateBoxXYZ(boxPos):
   # print(boxPos)

    listXYZ=[]
    for i,e in enumerate(boxPos):
        listXYZ.append([e[0],e[1],e[2]])
        listXYZ.append([e[0]+e[3],e[1],e[2]])
        listXYZ.append([e[0],e[1]+e[4],e[2]])
        listXYZ.append([e[0],e[1],e[2]+e[5]])
        listXYZ.append([e[0]+e[3],e[1]+e[4],e[2]])
        listXYZ.append([e[0]+e[3],e[1],e[2]+e[5]])
        listXYZ.append([e[0],e[1]+e[4],e[2]+e[5]])
        listXYZ.append([e[0]+e[3],e[1]+e[4],e[2]+e[5]])




    return seprateXYZ(listXYZ)

def askIfGoodWithConfig():
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 320, height = 200)

    canvas1.create_text(150, 100, text="Received information for rules", font=('Times New Roman', '12', 'bold'))

    canvas1.pack()

    answer=tk.messagebox.askquestion ('Confirm','Are you sure you entered the information correctly and would like to start?',icon = 'warning')
    #print(answer)
    root.destroy()
    if answer =='yes':
        return True
    return False



def getRatio2(armPos,tcpPosXYZ):
    armPosX=armPos[0][0]
    armPosY=armPos[0][1]
    armPosZ=armPos[0][2]
    tcpPosX=tcpPosXYZ[0]
    tcpPosY=tcpPosXYZ[1]
    tcpPosZ=tcpPosXYZ[2]
    jX=1
    jY=1
    #jZ=1
    if(armPosX!=0):
        jX=(tcpPosX*1.0*1000)/(armPosX*1.0)
    if(armPosY!=0):
        jY=(tcpPosY*1.0*1000)/(armPosY*1.0)
    #if(armPosZ!=0):
    #    jZ=(tcpPosZ*1.0*1000)/(armPosZ*1.0)
    # print("jX,jY")
    # print(jX,jY)
    
    return jX,jY


def getRatio(armPos,tcpPosXYZ):
    armPosX=armPos[0][0]
    armPosY=armPos[0][1]
    armPosZ=armPos[0][2]
    tcpPosX=tcpPosXYZ[0]
    tcpPosY=tcpPosXYZ[1]
    tcpPosZ=tcpPosXYZ[2]
    #jX=1
    #jY=1
    jZ=1
    #if(armPosX!=0):
    #    jX=(tcpPosX*1.0*1000)/(armPosX*1.0)
    #if(armPosY!=0):
    #    jY=(tcpPosY*1.0*1000)/(armPosY*1.0)
    if(armPosZ!=0):
        jZ=(tcpPosZ*1.0*1000)/(armPosZ*1.0)
    #print("jX,jY,jZ")
    #print(jX,jY,jZ)
    
    rotateXY=0

    angleTcp=math.atan2(tcpPosY*1.0,tcpPosX)
    angleArmPos=math.atan2(armPosY*1.0,armPosX)
    angleDiff=angleTcp-angleArmPos

    # print('in calculating angle diff')
    # print(tcpPosX)
    # print(tcpPosY)
    # print(armPosX)
    # print(armPosY)
    # print(angleTcp)
    # print(angleArmPos)




    distTcp=math.sqrt(tcpPosX*tcpPosX+tcpPosY*tcpPosY)
    distArmPos=math.sqrt(armPosX*armPosX+armPosY*armPosY)

    distRatio=distTcp*1.0*1000/distArmPos    

    return angleDiff,jZ,distRatio


def rotateMat(ang,twoNum):

    theta = ang# np.radians(30)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c)))
    #print(R) 

    p=twoNum#[10,0]

    np.array(p)

    p=np.dot(R,p)
    p=p.tolist()
    return p



def corrArmPosByTcp (armPos,tcpPosXYZ):
    # print("corr start")
    # print("armPos[0]")
    # print(armPos[0])
    # print("tcpPosXYZ")
    # print(tcpPosXYZ)
    # print("corr start2")
    #return armPos

    angleDiff,jZ,distRatio=getRatio(armPos,tcpPosXYZ)

    lenArmPos=len(armPos)


    # print("angleDiff,jZ,distRatio")

    # print(angleDiff,jZ,distRatio)


    for i,x in enumerate(armPos):
        #armPos[i][0]*=jX
        #armPos[i][1]*=jY
        #armPos[i][2]*=((jZ-1)*  (int( ((i+1)/lenArmPos)*6+0.5) )/6)   +1 
        armPos[i][2]*=((jZ-1)* (((i+1)/lenArmPos))**2   +1) 


    for i,x in enumerate(armPos):
        twoNum=[x[0],x[1]]
        # if(i==0):
            # print('before rotate')
            # print(armPos[i])
        newTwoNum=rotateMat(angleDiff,twoNum)

        armPos[i][0]=newTwoNum[0]
        armPos[i][1]=newTwoNum[1]
        #if(i==0):
            # print('after rotate')
            # print(armPos[i])
        #armPos[i][0]*=((distRatio-1)*  (int( ((i+1)/lenArmPos)*6+0.5) /6))   +1 
        #armPos[i][1]*=((distRatio-1)*  (int( ((i+1)/lenArmPos)*6+0.5) /6))   +1 
        armPos[i][0]*=((distRatio-1)*   (((i+1)/lenArmPos))**16   +1) 
        armPos[i][1]*=((distRatio-1)*   (((i+1)/lenArmPos))**16   +1) 

        #armPos[i][0]*=-1
        #armPos[i][1]*=-1
        # if(i==0):
        #     print('after ajust for length')
        #     print(armPos[i])

    jx,jy=getRatio2(armPos,tcpPosXYZ)

    # print("jx,jy")
    # print(jx,jy)
    #for i,x in enumerate(armPos):
    #    #armPos[i][0]*=((jx-1)*  (int( ((i+1)/lenArmPos)*6+0.5) /6))   +1 
    #    #armPos[i][1]*=((jy-1)*  (int( ((i+1)/lenArmPos)*6+0.5) /6))   +1 
     #   armPos[i][0]*=((jx-1)*   (((i+1)/lenArmPos))**16   +1) 
     #   armPos[i][1]*=((jy-1)*  (((i+1)/lenArmPos))**16   +1) 
    
    return armPos

def virtualizeArmAndObjects(armPos,boxPos,wallPos,plotWall,tcpPosXYZ):
    fig = plt.figure()
    ax = fig.gca(projection='3d')


    armPosCorr=corrArmPosByTcp(armPos,tcpPosXYZ)

    armX,armY,armZ=seprateXYZ(armPosCorr)
    #armXY,armYY,armZY=seprateXYZ(armPos)
    boxX,boxY,boxZ=seprateBoxXYZ(boxPos)
    ax.plot(armX, armY, armZ,  label='arm')
    #ax.plot(armXY, armYY, armZY,  label='arm uncorr',c='r')
    ax.scatter(boxX, boxY, boxZ, c='green', label='box')
    # Define the indices for the lines
    indices = [(0, 1), (0, 2), (0,3), (1,4), (1,5), (2,4), (2,6), (3,6), (3,5), (4,7), (5,7), (6,7)]

    # Draw lines for the sides of the box
    for length in range(0, len(boxX),8):
        for i, j in indices:
            ax.plot([boxX[i+length], boxX[j+length]], [boxY[i+length], boxY[j+length]], [boxZ[i+length], boxZ[j+length]], c='green')

    if(plotWall):
        if(wallInfo[0]<99999):
                
            #X = np.arange(-5, 5, 0.25)
            #Y = np.arange(-5, 5, 0.25)
            #X, Y = np.meshgrid(X, Y)
            #R = np.sqrt(X**0 + Y**0)
            #Z = np.sin(R)

            # Plot the surface.
            #surf = ax.plot_wireframe(X, Y, Z, rstride=50, cstride=50)
            Z = np.arange(-0, 400, 300)
            Y = np.arange(wallInfo[3]-200, wallInfo[2]+200,  wallInfo[3]+350-wallInfo[3])
            Y,Z = np.meshgrid(Y,Z)
            R = np.sqrt(Z**0 + Y**0)
            X = wallInfo[0]

            # Plot the surface.
            surf = ax.plot_wireframe(X, Y, Z, rstride=50, cstride=50)
        
        if(wallInfo[1]>-99999):

            Z = np.arange(-0, 400, 300)
            Y = np.arange(wallInfo[3]-200, wallInfo[2]+200,  wallInfo[3]+350-wallInfo[3])
            Y,Z = np.meshgrid(Y,Z)
            R = np.sqrt(Z**0 + Y**0)
            X = wallInfo[1]

            # Plot the surface.
            surf = ax.plot_wireframe(X, Y, Z, rstride=50, cstride=50)

        if(wallInfo[2]<99999):
        
            Z = np.arange(-0, 400, 300)
            X = np.arange(wallInfo[1]-200, wallInfo[0]+200, wallInfo[0]+350-wallInfo[1])
            X,Z = np.meshgrid(X,Z)
            Y = wallInfo[2]

            # Plot the surface.
            surf = ax.plot_wireframe(X, Y, Z, rstride=50, cstride=50)


        if(wallInfo[3]>-99999):
        
            Z = np.arange(-0, 400, 300)
            X = np.arange(wallInfo[1]-200, wallInfo[0]+200,  wallInfo[0]+350-wallInfo[1])
            X,Z = np.meshgrid(X,Z)
            Y = wallInfo[3]

            # Plot the surface.
            surf = ax.plot_wireframe(X, Y, Z, rstride=50, cstride=50)

        Y = np.arange(-300, 300, 25)
        X = np.arange(-300, 300, 25)

        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X**0 - Y**0)
        Z = np.sin(R)
        # Plot the surface.
        #surf = ax.plot_wireframe(X, Y, Z, rstride=50, cstride=50)



    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)
    #ax.set_zlim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# def tcpOffset(tcpPos,l,a1,a2,a3):
    



def tcpOffset(tcpAngle,tcpPosXYZ,lengtghGrip):
    alpha=tcpAngle[0]
    beta=tcpAngle[1]
    gama=tcpAngle[2]

    return tcpOffset_h(tcpPosXYZ,lengtghGrip,alpha,beta ,gama)





def tcpOffset_h(tcpPos,l,alpha,beta ,gama):


    ldf=pandas.DataFrame([0,0,l,0])


    transitionfram=pandas.DataFrame([[math.cos(alpha)*math.cos(beta),
    math.cos(alpha)*math.sin(beta)*math.sin(gama)-math.sin(alpha)*math.cos(gama),
    math.cos(alpha)*math.sin(beta)*math.cos(gama)+math.sin(alpha)*math.sin(gama),0],
    [math.sin(alpha)*math.cos(beta),
    math.sin(alpha)*math.sin(beta)*math.sin(gama)+math.cos(alpha)*math.cos(gama),
    math.sin(alpha)*math.sin(beta)*math.cos(gama)-math.cos(alpha)*math.sin(gama),0],
    [-math.sin(beta),math.cos(beta)*math.sin(gama),math.cos(beta)*math.cos(gama),0],[0,0,0,1]])


    tcpOffset= transitionfram.dot(ldf)
    # print(("tcpOffset"))
    # print((tcpOffset))

    tcpOffset=tcpOffset.values.tolist()
    for i,x in enumerate(tcpOffset):
        tcpOffset[i]=tcpOffset[i][0]
    # print(("tcpOffset"))
    # print((tcpOffset))

    # print((tcpPos))
    # print((tcpOffset))
    tcpPos[0]+=tcpOffset[0]/1000.0
    tcpPos[1]-=tcpOffset[1]/1000.0
    tcpPos[2]+=tcpOffset[2]/1000.0
    return tcpPos



setConfig()
print(ipAdd)
# r = urx.Robot(ipAdd, use_rt=True, urFirm=5.1)
r = urx.Robot(ipAdd, use_rt=True, urFirm=5.1)
# pose = []
# location = Location(x=pose[0], y=pose[1], z=pose[2], rx=pose[3], ry=pose[4], rz=pose[5])
# relative_position = (Location()) * location
# transform = r.csys * math3d.Transform(relative_position.convert_mm_to_m().matrix)
# vel = 250
# acc = 250 * 2
# r.movel(transform.pose_vector, acc=acc / 1000, vel=vel / 1000, relative=False, wait=False)

needVirtualize=1

# print("boxList after setConfig")
# print(boxList)

theBoxes=boxes()
theBoxes.boxesList=boxList
# print("theBoxes.boxesList after setConfig")
# print(theBoxes.boxesList)

def theLoop(needPopUp,boxList,needVirtualize,theBoxes):
    with open('signal.pkl', 'wb') as file:
            pickle.dump(0, file)
    #askcolorkPop
    while (needPopUp==0):
        try:
            get_all_data = r.get_all_rt_data()
            print("retrieving info..")

        except:
            print("disconnected")
        # print("theBoxes.boxesList in mainloop")
        # print(theBoxes.boxesList)

        boxList=theBoxes.boxesList
        # print("boxList in mainloop")
        # print(boxList)
        # print(get_all_data)
        #print(get_all_data['tcp'])
        qActual=get_all_data['qActual']
        
        tcp=get_all_data['tcp']
        #print(qActual)
        #print(qActual[0])
        #print(qActual[2])

        #otherObjectInformationNotNoTableWithHole
        #otherObjectInformationOnTableWithHole
        #wallInformation
        #objectState

        JointPos=get_all_data['qActual']
        tcpPos=get_all_data['tcp']
        tcpPosXYZ=tcpPos[0:3]
        tcpAngle=tcpPos[3:7]
        # print('tcpAngle')
        # print(tcpAngle)
        # print("tcpPos 1 ")
        # print(tcpPos)
        #tcpPosXYZ=tcpOffset(tcpAngle,tcpPosXYZ,lengtghGrip)
        # print('tcpPosXYZ')
        # print(tcpPosXYZ)
        tcpSpeed=getTcpSpeed(tcpPosXYZ)
        tcpAcce=getTcpAcce(tcpSpeed)
        speedWithinLimit=withInBoundSoeed(tcpSpeed,speedLimit)
        acceWithinLimit=withInBoundAcce(tcpAcce,acceLimit)
        
        #objectPos=getObjectPos(tcpPos,objectState)
        #isFitIntoHole(objectPos,otherObjectInformationOnTableWithHole)

        jointPosCart=getJointPosCart(JointPos)
        #print('jointPosCart')
        #print(jointPosCart)

        # print("boxList in mainloop")
        # print(boxList)

        # print("jointPosCart")
        # print(jointPosCart)

        okWithGround=aboveGround(jointPosCart)
        #okWithWalls=withinLimitOfWall(jointPosCart,wallInfo,lastInfo.list0,tcpPosXYZ)
        okWithItSelf=notCollideWithItSelf(jointPosCart)
        okWithOtherObj=notCollideWithOtherObject(boxList,jointPosCart)
        okWithOtherObj=notCollideWithOtherObjectUsingTcp(boxList,tcpPos)
        okWithWalls=withinLimitOfWall(jointPosCart,wallInfo,lastInfo.list0,tcpPosXYZ)

        global theOverlappingHistory
        # theOverlappingHistory=addCurrentOverlappingInformation(theOverlappingHistory,boxList,tcpPos)
        okWithCustomizeCheck=customizeCheck()
        okWithFutre,futureCode=isFutureOk(tcpPosXYZ,tcpSpeed,numSec)
        updatelast(tcpPosXYZ,tcpSpeed)

        if(needVirtualize):
            needVirtualize=0
            virtualizeArmAndObjects(lastInfo.list0,boxList,wallInfo,False,tcpPosXYZ)
            virtualizeArmAndObjects(lastInfo.list0,boxList,wallInfo,True,tcpPosXYZ)
            while(askIfGoodWithConfig()==False):
                setConfig()
                virtualizeArmAndObjects(lastInfo.list0,boxList,wallInfo,False,tcpPosXYZ)
                virtualizeArmAndObjects(lastInfo.list0,boxList,wallInfo,True,tcpPosXYZ)





        if((okWithGround and speedWithinLimit and acceWithinLimit and okWithItSelf and okWithOtherObj and okWithWalls) or lastInfo.start>=1 ):#and okWithFutre):
            okCUrrently=1
            # if(okWithFutre==False and lastInfo.start==0 ):
            #     global isApprixi
            #     if isApprixi==0:
            #         if futureCode==1:
            #             #popupmsg('might be colliding after '+str(predictNumSec)+ ' second(s) '+ str(futureCode))
            #             popupmsg('Might be colliding after '+str(predictNumSec)+ ' second(s) with ground.')
            #         elif futureCode ==2:
            #             popupmsg('Might be colliding after '+str(predictNumSec)+ ' second(s) with North wall.')
            #         elif futureCode ==3:
            #             popupmsg('Might be colliding after '+str(predictNumSec)+ ' second(s) with South wall.')
            #         elif futureCode ==4:
            #             popupmsg('Might be colliding after '+str(predictNumSec)+ ' second(s) with East wall.')
            #         elif futureCode ==5:
            #             popupmsg('Might be colliding after '+str(predictNumSec)+ ' second(s) with West wall.')
            #         else:
            #             #should not be excuted
            #             popupmsg('Might be hitting something, error in detecting what that is.')

            #     else:
            #         popupmsg("Too close to walls or the ground.")
        else:
            okCUrrently=0
            ids_signal = 1
            coords = [point*1000 for point in get_all_data['tcp'][0:3]]
            with open('signal.pkl', 'wb') as file:
                pickle.dump(ids_signal, file)
            # with open('coordinates.pkl', 'wb') as file:
            #     pickle.dump(coords, file)
            #break
            # print('invalid move')
            # print("speedLimit")
            # print(speedLimit)
            # print("acceWithinLimit")
            # print(acceWithinLimit)
            # print("okWithItSelf")
            # print(okWithItSelf)
            # print("okWithOtherObj")
            # print(okWithOtherObj)
            # print("okWithWalls")
            # print(okWithWalls)
            #print("okWithFutre")
            #print(okWithFutre)
            needPopUp=1
            text=''
            if(speedWithinLimit==False):
                text+=': Looks like over speed.'
            if(acceWithinLimit==False):
                text+=': Looks like over accelerated.'
            if(okWithItSelf==False):
                text+=': Looks like collision with robot itself.'
            if(okWithOtherObj==False):
                text+=': looks like collision with other objects.'
            if(okWithWalls==False):
                text+=': Looks like collision with a wall.'
            if(okWithGround==False):
                text+=': Looks like collision with ground.'
            popupmsg('Invalid move '+text)
            #virtualizeArmAndObjects(lastInfo.list0,boxList,wallInfo,False)
            #virtualizeArmAndObjects(lastInfo.list0,boxList,wallInfo,True)
        if(lastInfo.start>0):
            lastInfo.start-=1

        #print('tcp pos')
        #print(tcp)
        # print('speed')
        # print(lastInfo.lastSpeed)

        # print('abs(tcpAcce)')
        # print(abs(tcpAcce))
        time.sleep(0.1)

    # print('invalid move, stopped')
    ids_signal = 1
    #printErr(e)

    r.close()

theLoop(needPopUp,boxList,needVirtualize,theBoxes)