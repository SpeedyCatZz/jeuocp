import personnage, fight, createMonster
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
from cptr import *


app = Flask(__name__)

import sys
import os

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.form:
        compteurkills = 0 
        listeVaincus =[]
        nomperso=request.form['name']   

        MonPerso = personnage.personnage(nomperso,20,6,3)

        while MonPerso[1] > 0:
            Ennemi = createMonster.createMob()
            fight.fight(MonPerso, Ennemi)

            if MonPerso[1] > 0:
                compteurkills=compteurEnnemisTue(compteurkills)
                listeVaincus.append(Ennemi[0])

        return render_template("home.html", name=nomperso, compteurkills=compteurkills, listeVaincus=listeVaincus)    
    

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)







