#! /usr/bin/env python

import os, sys
import pygame as pg
import random
import hashset as hs
import subprocess
import time
import warnings

if (os.name == 'nt'):    
  c = os.system('title DwarfSector')
else:
  c = os.system('\x1b]2;DwarfSector\x07')
c = os.system('mode con:cols=100 lines=70')

del c


warnings.warn("TEST")



print "Starting"


flags = pg.DOUBLEBUF

#wd = pg.display.set_mode((750, 550), flags)
green = ""
red = ""
yellow = ""
blue = ""

def rocketeer():
  if (os.name == 'nt'):    
    c = os.system('cls')
  else:
    c = os.system('clear')

  print "   "
  print "  x>----------------->"
  print " xx>=/            \===>>"
  print "xxx>=|Dwarf Sector|====>>"
  print " xx>=\            /===>>"
  print "  x>----------------->"
  print "   "
  time.sleep(0.3)
  if (os.name == 'nt'):    
    c = os.system('cls')
  else:
    c = os.system('clear')
  print "   "
  print "  x>----------------->"
  print " xx>=/            \===>>"
  print "xxx>=|Dwarf       |====>>"
  print " xx>=\            /===>>"
  print "  x>----------------->"
  print "   "
  time.sleep(0.3)
  if (os.name == 'nt'):    
    c = os.system('cls')
  else:
    c = os.system('clear')
  print "   "
  print "  x>----------------->"
  print " xx>=/            \===>>"
  print "xxx>=|            |====>>"
  print " xx>=\            /===>>"
  print "  x>----------------->"
  print "   "
  time.sleep(0.3)
  if (os.name == 'nt'):    
    c = os.system('cls')
  else:
    c = os.system('clear')
  print "You have crash landed on a alien"
  print "planet. The Rocketship is very badly"
  print "broken. You have to collect resources"
  print "to survive. This alien is very much"
  print "like Earth. Craft a rocketship and"
  print "fuel to get back. Research/Build/Mine your way"
  print "back to Earth!"
  raw_input("Press enter to continue:")

rocketeer()

class Player():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.health = 10
    self.resources = hs.HashSet()
    self.resources.add(0, 0)
    self.resources.add(1, 0)
    self.resources.add(2, 0)
    self.resources.add(3, 0)
    self.resources.add(4, 0)
    self.resources.add(5, 0)
    self.resources.add(6, 0)
    self.resources.add(7, 0)
    self.resources.add(8, 0)
    self.resources.add(9, 0)
    self.resources.add(10, 0)
    self.resources.add(11, 0)
    self.resources.add(12, 0)
  def addRes(self, type, amount):
    if not type.type == 13:
      if not type.type == 9:
        t = self.resources.get(type.type)
        self.resources.remove(type.type, t)
        self.resources.add(type.type, t + amount)
      else:
        t = self.resources.get(6)
        self.resources.remove(6, t)
        self.resources.add(6, t + amount)
    else:
      t = self.resources.get(12)
      self.resources.remove(12, t)
      self.resources.add(12, t + (amount * 2))
  def setRes(self, type, amount):
    t = self.resources.get(type)
    self.resources.remove(type, t)
    self.resources.add(type, amount)
  def subRes(self, type, amount):
    t = self.resources.get(type)
    self.resources.remove(type, t)
    self.resources.add(type, t - amount)
  def getRes(self, type):
    return self.resources.get(type)

class Map():
  def __init__(self, maxx, maxy, id):
    self.blocks = []
    self.id = id
    for i in xrange(0, maxx):
      for x in xrange(0, maxy):
        self.blocks.append(Block(x, i, 0))
    
  def getBlockAt(self, x, y):
    for block in self.blocks:
      if block.x == x and block.y == y:
        return block
  def setBlockAt(self, x, y, type):
    for block in self.blocks:
      if block.x == x and block.y == y:
        block.type = type
class Block():
  def __init__(self, x, y, type):
    self.x = x
    self.y = y
    self.type = type
    self.data = BlockData()
  def getType(self):
    return int(self.type)
  def setType(self, type):
    self.type = type
class BlockData():
  def __init__(self):
    self.items = []
  def addItem(self, item):
    self.items.append(item)
    
mapt = Map(50, 50, 0)

player = Player(25, 25)

blocktype = {
  "air": 0,
  "stone": 1,
  "player": 2,
  "wood": 3,
  "workbench": 4,
  "furnace": 5,
  "pork": 6,
  "cookedpork": 7,
  "coal": 8,
  "door": 9,
  "goldcoin": 10,
  "compass": 11,
  "cactus": 12,
  "adultcactus": 13
  }

rblocktype = {
  0: "air",
  1: "stone",
  2: "player",
  3: "wood",
  4: "workbench",
  5: "furnace",
  6: "pork",
  7: "cookedpork",
  8: "coal",
  9: "door",
  10: "goldcoin",
  11: "compass",
  12: "cactus",
  13: "adultcactus"
  }

labeled = {    0: " ",
    1: u"\u2588",
    2: chr(1),
    3: chr(15),
    4: "@",
    5: "Q",
    6: "^",
    7: "*",
    8: "o",
    9: "H",
    10: chr(169),
    11: chr(11),
    12: "v",
    13: "8"
    }
labelreverse = {
    ' ': 0,
    u"\u2588": 1,
    chr(1): 2,
    chr(15): 3,
    "@": 4,
    "Q": 5,
    "^": 6,
    "*": 7,
    "o": 8,
    "H": 9,
    chr(169): 10,
    chr(11): 11,
    "v": 12,
    "8": 13
    }

if 'idlelib.run' in sys.modules:
  labeled[2] = "$"
  labelreverse["$"] = labelreverse.pop(chr(1))


def load(name):
  if (os.name == 'nt'):    
    c = os.system('cls')
  else:
    c = os.system('clear')
  print "<<LOADING>>"
  mapd = Map(50, 50, 0)
  m = open("saves/" + name + ".dat", "r")
  mapfile = open("saves/" + name + ".map", "r")
  array = mapfile.read(2500 * 2).split(":")
  x = 0
  y = 0
  mapd.setBlockAt(1, 1, array[0])
  try:
    for i in xrange(0, 2500):
      mapblock = array[i]
      if x == 51:
        y += 1
        x = 1
      if mapblock != "":
        mapd.setBlockAt(x, y, int(mapblock))
      else:
        mapd.setBlockAt(x, y, 0)
      x += 1
  except:
    pass
  
  
  contents = ""

  properties = m.readlines()
  playerprops = properties[0].split(":")
  player.x = int(playerprops[1])
  player.y = int(playerprops[2])
  ##############
  tesn = (properties[1]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[2]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[3]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[4]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[5]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[6]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[7]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[8]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[9]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[10]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[11]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[12l]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  tesn = (properties[13l]).split(":")
  player.setRes(blocktype[tesn[0]], int(tesn[1]))
  ##############
  
  mapfile.close()
  m.close()
  if (os.name == 'nt'):    
    c = os.system('cls')
  else:
    c = os.system('clear')
  return mapd

  
def save(map_to_save, name):
  contents = ""
  m = open("saves/" + name + ".dat", "w")


  y = 1
  yold = 1

  for block in map_to_save.blocks:
    contents += str(block.type) + ":"
  md = open("saves/" + name + ".map", "w")

  itemz = ""
  numbd = 1
  for item in player.resources.arrayone:
    itemz +=rblocktype[item] + ":" + str(player.resources.get(item)) + "\n"
    numbd += 1
  
  m.write("playerpos" + ":" +  str(player.x) + ":" + str(player.y) + "\n" + "" + itemz)
  
  md.write(str(contents))
  md.close()  
  m.close()


def ifBlockIsNearPlayer(t):
  if mapt.getBlockAt(player.x - 1, player.y).getType() == t:
    return True
  if mapt.getBlockAt(player.x + 1, player.y).getType() == t:
    return True
  if mapt.getBlockAt(player.x - 1, player.y + 1).getType() == t:
    return True
  if mapt.getBlockAt(player.x + 1, player.y + 1).getType() == t:
    return True
  if mapt.getBlockAt(player.x - 1, player.y - 1).getType() == t:
    return True
  if mapt.getBlockAt(player.x + 1, player.y - 1).getType() == t:
    return True
  if mapt.getBlockAt(player.x, player.y - 1).getType() == t:
    return True
  if mapt.getBlockAt(player.x, player.y + 1).getType() == t:
    return True


global doorpassed

mapt.getBlockAt(25, 25).setType(2)

global input
input = "nothing"

for i in xrange(0, (50 / 2) + ((50 / 5) * 2)):
  mapt.setBlockAt(random.randint(1, 50), random.randint(1, 50), 3)

for i in xrange(0, (50 / 2) + ((50 / 5) * 2)):
  mapt.setBlockAt(random.randint(1, 50), random.randint(1, 50), 1)

for block in mapt.blocks:
  if block.type == 1:
    if random.randint(1, 9) == 2:
      block.setType(8)

for block in mapt.blocks:
  if block.type == 0:
    if random.randint(1, 100) == 1:
      block.setType(1)





doorpassed = False

def update():
  global mapt, doorpassed, input
  print "Health: " + str(player.health)
  for block in mapt.blocks:
    if block.type == 12:
      if random.randint(1, 10) == 2:
        block.setType(13)
  
  if (os.name == 'nt'):    
    c = os.system('cls')
  else:
    c = os.system('clear')
  array = input.split(" ")
  if array[0] == "nothing":
    print green + "You do nothing"
  elif array[0] == "help":
    print green + "help: Displays Commands"
    print green + "nothing: Does nothing and updates"
    print green + "dig: Put down,up,left or right to dig blocks"
    print green + "move: Move down,up,left or right"
    print green + "build: Place stuff down,up,left or right"
    print green + "craft: Craft stuff"
    print green + "cook: Cook stuff around a furnace"
  elif array[0] == "dig":
    if array[1] == "down":
      player.addRes(mapt.getBlockAt(player.x, player.y + 1), random.randint(1, 1))
      mapt.setBlockAt(player.x, player.y + 1, 0)
      print green + "You dug down"
    elif array[1] == "up":
      player.addRes(mapt.getBlockAt(player.x, player.y - 1), random.randint(1, 1))
      mapt.setBlockAt(player.x, player.y - 1, 0)
      print green + "You dug up"
    elif array[1] == "left":
      player.addRes(mapt.getBlockAt(player.x - 1, player.y), random.randint(1, 1))
      mapt.setBlockAt(player.x - 1, player.y, 0)
      print green + "You dug left"
    elif array[1] == "right":
      player.addRes(mapt.getBlockAt(player.x + 1, player.y), random.randint(1, 1))
      mapt.setBlockAt(player.x + 1, player.y, 0)
      print green + "You dug right"
  elif array[0] == "move":
    if array[1] == "down":
      if mapt.getBlockAt(player.x, player.y + 1).getType() == 0 or mapt.getBlockAt(player.x, player.y + 1).getType() == 9:

        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x, player.y + 1).getType() == 9:
          doorpassed = True
        
        player.y += 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved down"
    elif array[1] == "up":
      if mapt.getBlockAt(player.x, player.y - 1).getType() == 0 or mapt.getBlockAt(player.x, player.y - 1).getType() == 9:

        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x, player.y - 1).getType() == 9:
          doorpassed = True
        
        player.y -= 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved up"
    elif array[1] == "left":
      if mapt.getBlockAt(player.x - 1, player.y).getType() == 0 or mapt.getBlockAt(player.x - 1, player.y).getType() == 9:

        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x - 1, player.y).getType() == 9:
          doorpassed = True
        
        player.x -= 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved left"
    elif array[1] == "right":
      if mapt.getBlockAt(player.x + 1, player.y).getType() == 0 or mapt.getBlockAt(player.x + 1, player.y).getType() == 9:
        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x + 1, player.y).getType() == 9:
          doorpassed = True
        
        player.x += 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved right"
    elif array[1] == "dleft":
      if mapt.getBlockAt(player.x - 1, player.y + 1).getType() == 0 or mapt.getBlockAt(player.x - 1, player.y + 1).getType() == 9:

        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x - 1, player.y + 1).getType() == 9:
          doorpassed = True
        
        player.x -= 1
        player.y += 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved down left"
    elif array[1] == "dright":
      if mapt.getBlockAt(player.x + 1, player.y + 1).getType() == 0 or mapt.getBlockAt(player.x + 1, player.y + 1).getType() == 9:
        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x + 1, player.y + 1).getType() == 9:
          doorpassed = True
        
        player.x += 1
        player.y += 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved down right"
    elif array[1] == "uleft":
      if mapt.getBlockAt(player.x - 1, player.y - 1).getType() == 0 or mapt.getBlockAt(player.x - 1, player.y - 1).getType() == 9:

        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x - 1, player.y - 1).getType() == 9:
          doorpassed = True
        
        player.x -= 1
        player.y -= 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved up left"
    elif array[1] == "uright":
      if mapt.getBlockAt(player.x + 1, player.y - 1).getType() == 0 or mapt.getBlockAt(player.x + 1, player.y - 1).getType() == 9:
        mapt.setBlockAt(player.x, player.y, 0)
        if doorpassed:
          doorpassed = False
          mapt.setBlockAt(player.x, player.y, 9)
        if mapt.getBlockAt(player.x + 1, player.y - 1).getType() == 9:
          doorpassed = True
        
        player.x += 1
        player.y -= 1
        mapt.setBlockAt(player.x, player.y, 2)
        print green + "You moved up right"
  elif array[0] == "craft":
    if array[1] == "workbench":
      if player.resources.get(3) >= 2:
        player.addRes(Block(0, 0, 4), 1)
        player.subRes(3, 2)
    if array[1] == "furnace" and ifBlockIsNearPlayer(4):
      if player.resources.get(3) >= 2:
        player.addRes(Block(0, 0, 5), 1)
        player.subRes(1, 5)
    if array[1] == "door" and ifBlockIsNearPlayer(4):
      if player.resources.get(3) >= 4:
        player.setRes(9, player.resources.get(9) + 1)
        player.subRes(3, 4)
    if array[1] == "compass" and ifBlockIsNearPlayer(4):
      if player.resources.get(3) >= 2 and player.resources.get(1) >= 5:
        player.subRes(3, 2)
        player.subRes(1, 5)
  elif array[0] == "cook":
    if array[1] == "pork" and ifBlockIsNearPlayer(5):
      if player.resources.get(6) >= 1 and player.resources.get(8) >= 1:
        player.addRes(Block(0, 0, 7), 1)
        player.subRes(6, 1)
        player.subRes(8, 1)
  elif array[0] == "use":
    if array[1] == "compass":
      print "X: " + str(player.x) + " Y: " + str(player.y)
    if array[1] == "cookedpork":
      print "Nom Nom Nom! 4 health gained! Health: " + player.health
  elif array[0] == "build":
    
      ty = blocktype[array[1]]
      if player.resources.get(ty) > 0:
        if array[2] == "down":
          mapt.setBlockAt(player.x, player.y + 1, ty)
          player.subRes(mapt.getBlockAt(player.x, player.y + 1).getType(), 1)
          
          print green + "You built down"
        elif array[2] == "up":
          mapt.setBlockAt(player.x, player.y - 1, ty)
          player.subRes(mapt.getBlockAt(player.x, player.y - 1).getType(), 1)
          
          print green + "You built up"
        elif array[2] == "left":
          mapt.setBlockAt(player.x - 1, player.y, ty)
          player.subRes(mapt.getBlockAt(player.x - 1, player.y).getType(), 1)
          
          print green + "You built left"
        elif array[2] == "right":
          mapt.setBlockAt(player.x + 1, player.y, ty)
          player.subRes(mapt.getBlockAt(player.x + 1, player.y).getType(), 1)
          
          print green + "You built right"
        if array[2] == "uright":
          mapt.setBlockAt(player.x + 1, player.y - 1, ty)
          player.subRes(mapt.getBlockAt(player.x - 1, player.y - 1).getType(), 1)
              
          print green + "You built up left"
        elif array[2] == "uleft":
          mapt.setBlockAt(player.x - 1, player.y - 1, ty)
          player.subRes(mapt.getBlockAt(player.x - 1, player.y - 1).getType(), 1)
              
          print green + "You built up right"
        elif array[2] == "dleft":
          mapt.setBlockAt(player.x - 1, player.y + 1, ty)
          player.subRes(mapt.getBlockAt(player.x - 1, player.y + 1).getType(), 1)
         
          print green + "You built down left"
        elif array[2] == "dright":
          mapt.setBlockAt(player.x + 1, player.y + 1, ty)
          player.subRes(mapt.getBlockAt(player.x + 1, player.y + 1).getType(), 1)
              
          print green + "You built down right"
        else:
          print green + "Don't have any"
  elif array[0] == "tbm":
    if array[1] == "builder":
      player.addRes(Block(0, 0, 1), 1000)
      player.addRes(Block(0, 0, 3), 1000)
      player.addRes(Block(0, 0, 4), 1000)
      player.addRes(Block(0, 0, 5), 1000)
      player.addRes(Block(0, 0, 6), 1000)
      player.addRes(Block(0, 0, 7), 1000)
      player.addRes(Block(0, 0, 8), 1000)
      player.addRes(Block(0, 0, 9), 1000)
      player.addRes(Block(0, 0, 10), 1000)
      print green + "Got kit builder!"
  elif array[0] == "tbi":
    t = blocktype[array[1]]
    player.addRes(Block(0, 0, t), int(array[2]))
  elif array[0] == "save":
    save(mapt, array[1])
    print green + "Saved"
  elif array[0] == "load":
    mapt = load(array[1])
    print green + "Loaded"
  else:
    print yellow + "Command is not a command, Do help for commands."
  
  
  contents = ""

  y = 1
  yold = 1
  for block in mapt.blocks:
    y = block.y
    if not y == yold:
      yold = y
      contents += "\n"
    contents += labeled[block.type]

  
  
  items = "Resources: "
  numbd = 1
  for item in player.resources.arrayone:
    if player.resources.get(item) > 0 and item != 0:
      items += " \n " + rblocktype[item] + " = " + str(player.resources.get(item))
    numbd += 1
  #print contents + "\n" + "Resources: \n Stone = " + str(player.resources.get(1)) + " \n Wood = " + str(player.resources.get(3)) + " \n Workbenches = " + str(player.resources.get(4)) + " \n Furnaces = " + str(player.resources.get(5)) + " \n Pork = " + str(player.resources.get(6)) + " \n Cooked Pork = " + str(player.resources.get(7)) + " \n Coal = " + str(player.resources.get(8))
  print blue + contents + "\n" + green + items
  input = raw_input("Action:")
  sys.stdout.flush()

for i in xrange(0, 2500):
  update()
