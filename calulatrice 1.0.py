import tkinter as tk


    

## Création d'une fenêtre


window=tk.Tk()
window.minsize(150,50)
frame=tk.Frame(window, width=400, height=350)
frame.pack_propagate(True)
frame.pack()
result=tk.Label(frame,text="")
champ1=tk.Entry(frame)
affichage=tk.Label(frame, text='')
           

def ajouter_texte(texte):
    if champ_actif is not None:
        champ_actif.insert(tk.END, texte)
        
def choisir_champ(champ):
    global champ_actif
    champ_actif=champ

champ_actif= None

champ1.bind("<FocusIn>", lambda event: choisir_champ(champ1))

def effacer_dernier_caractere():
    champ1.delete(len(champ1.get())-1, tk.END)



def rang_signe(a, chaine):## identifie les position des signes recherchés dans l'expression
     liste=[]
     for i in range(len(chaine)):
        if chaine[i] == a:
            liste.append(i)
     return liste

def remplacer_parenthèses(chaine,b):## identifie les parenthèses et rmplace l'expression entre parenthèses par une expression equivalente
    
    copie=""
    L1=rang_signe("(",chaine)
    L2= rang_signe(")", chaine)

    if L1!=[]and L2!=[] :
        copie= chaine[0:L1[0]]+b+chaine[L2[0]+1:]

    return copie
  
        

    
def calculs1(chaine): ## réalise un calcul à partir d'une expression donnée en string
    plus=rang_signe("+",chaine)
    moins=rang_signe("-", chaine)
    div=rang_signe("÷", chaine)
    fois=rang_signe("x", chaine)
    parg= rang_signe("(", chaine)
    pardr= rang_signe(")", chaine)
    liste=plus+moins+div+fois+pardr+parg
    
    if len(liste)==0 :
        return float(chaine)
    else:
        if len(parg)!=0 and len(pardr)!=0: ## en présence de parenthèses on remplace l'expression entre parenthèses par sa valeur
            a= calculs1(chaine[parg[0]+1:pardr[0]])
            nv_chaine=remplacer_parenthèses(chaine,str(a))
            return calculs1(nv_chaine)
    

            
        elif len(plus)>0 or len(moins)>0:  ## on réalise les additions et les différences en dernier
            if len(moins)==0  :
                return calculs1(chaine[0:plus[0]])+calculs1(chaine[plus[0]+1:])
            elif len(plus)==0 :
                return calculs1(chaine[0:moins[0]])-calculs1(chaine[moins[0]+1:])
            elif len(moins)>0 and len(plus)>0:  ## on effectue le calcul dans le sens de lecture en présence d'opérations équivalentes
                if plus[0]>moins[0]:            ##(*)
                    return calculs1(chaine[0:moins[0]])-calculs1(chaine[moins[0]+1:])
                else:
                    return calculs1(chaine[0:plus[0]])+calculs1(chaine[plus[0]+1:])

                    
        
        elif min(liste) in fois: ##(*)
            return calculs1(chaine[0:min(liste)])* calculs1(chaine[min(liste)+1:])
        elif min(liste) in div:
            return calculs1(chaine[0:min(liste)])/ calculs1(chaine[min(liste)+1:])

    

def affichage():
    
    result.config(text=str(calculs1(champ1.get())))
    




## Création de boutons
bouton_plus=tk.Button(frame, text='+',command=lambda: ajouter_texte("+"),width=5, height=2)
bouton_moins= tk.Button(frame,text= '-',command= lambda: ajouter_texte("-"),width=5, height=2)
bouton_fois= tk.Button(frame, text='x',command=lambda: ajouter_texte("x"),width=5, height=2)
bouton_div=tk.Button(frame, text='÷',command=lambda: ajouter_texte("÷"), width=5, height=2)
bouton_eg=tk.Button(frame, text='=',command= affichage,width=5, height=2  )
bouton_1=tk.Button(frame, text='1',command=lambda: ajouter_texte("1"), width=15, height=2)
bouton_2=tk.Button(frame, text='2',command=lambda: ajouter_texte("2"), width=15, height=2)
bouton_3=tk.Button(frame, text='3',command=lambda: ajouter_texte("3"), width=15, height=2)
bouton_4=tk.Button(frame, text='4',command=lambda: ajouter_texte("4"), width=15, height=2)
bouton_5=tk.Button(frame, text='5',command=lambda: ajouter_texte("5"), width=15, height=2)
bouton_6= tk.Button(frame, text='6',command=lambda: ajouter_texte("6"), width=15, height=2)
bouton_7=tk.Button(frame, text='7',command=lambda: ajouter_texte("7"), width=15, height=2)
bouton_8=tk.Button(frame, text='8',command=lambda: ajouter_texte("8"), width=15, height=2,)
bouton_9=tk.Button(frame, text='9',command=lambda: ajouter_texte("9"), width=15, height=2)
bouton_par1= tk.Button(frame, text='(',command=lambda: ajouter_texte("("),width=15, height=2)
bouton_par2= tk.Button(frame, text=')',command=lambda: ajouter_texte(")"),width=15, height=2)
effacer=tk.Button(frame, text='←',width=15, height=2, command=effacer_dernier_caractere)

result.place(x=0,y=60)
champ1.place(x=0, y=0)
bouton_plus.place(x=360,y=300)
bouton_moins.place(x=360,y=250)
bouton_fois.place(x=360,y=200)
bouton_div.place(x=360,y=150)
bouton_eg.place(x=360, y=100)
bouton_1.place(x=0,y=250)
bouton_2.place(x=120,y=250)
bouton_3.place(x=240,y=250)
bouton_4.place(x=0,y=200)
bouton_5.place(x=120,y=200)
bouton_6.place(x=240,y=200)
bouton_7.place(x=0,y=150)
bouton_8.place(x=120,y=150)
bouton_9.place(x=240,y=150)
bouton_par1.place(x=0,y=100)
bouton_par2.place(x=120,y=100)
effacer.place(x=240,y=100)









## Démarrage de la boucle
window.mainloop()





            
        

    
            








