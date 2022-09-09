from genMob import *
import random

def createMob():
   listemob = ["KhaZix", "BelVeth", "ReqSai", "ChoGath"]
   nommob = random.choice (listemob)
   return genMob(nommob)
