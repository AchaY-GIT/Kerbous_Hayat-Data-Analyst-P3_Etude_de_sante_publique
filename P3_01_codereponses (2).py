#!/usr/bin/env python
# coding: utf-8

# # Réalisez une étude de santé publique

# # Question 1 : donnez le nombre d'humain pour l'année 2013.

# In[ ]:





# In[25]:


import pandas as pd
import numpy as np


# In[26]:


#charger les fichier csv en pyton 
population_df = pd.read_csv('D:\\openclassroom\\projet3\\DonneesFAO_2013_fr/fr_population.csv')



vegetal_df= pd.read_csv('D:\\openclassroom\\projet3\\DonneesFAO_2013_fr/fr_vegetaux.csv')

cereales_df= pd.read_csv('D:\\openclassroom\\projet3\\DonneesFAO_2013_fr/fr_céréales.csv')


animaux_df=pd.read_csv('D:\\openclassroom\\projet3\\DonneesFAO_2013_fr/fr_animaux.csv')

snutrission_df = pd.DataFrame(pd.read_csv('D:\\openclassroom\\projet3\\DonneesFAO_2013_fr/fr_sousalimentation.csv'))


# In[27]:



vegetal=pd.DataFrame(vegetal_pd[['Zone','Produit','Valeur','Unité']])


# In[28]:



population_df.head(3)


# In[29]:


#Verification des données (Zone)
population_df.Zone.unique()
#prendre la chine et suprimer les autres 

#on trouve la chine en entier et ses departements donc on supprime 
# In[30]:


population_df.Année.unique()


# In[31]:


population_df.Valeur.unique()


# In[32]:


population_df.Symbole.unique()


# In[33]:


population_pd=population_df.drop(population_df[(population_df['Zone']=='Chine - RAS de Hong-Kong') | (population_df['Zone']=='Chine, Taiwan Province de') | (population_df['Zone']=='Chine, continentale') | (population_df['Zone']=='Chine - RAS de Macao')].index, inplace=False)


# In[34]:


population_pd.Zone.unique()


# In[35]:


import pandas as pd
pop= pd.DataFrame(population_pd[['Zone','Valeur', 'Unité']])
pop


# In[36]:


hTotal= (pop['Valeur']).sum()*1000
print('le nombre d\'humain sur terre en 2013 est de:',hTotal, 'personnes')


# # Question 2 : Identifiez ces redondances, en donnant votre réponse sous forme de formule mathématique
disponibilité interieure
                         =production+importation+variation de stock-exportation
                         =semance+Nouriture +Aliments pour animeaux+traitement+autre utilisation+perte
# In[37]:


vegetal_df.Zone.unique()


# In[38]:


vegetal_pd=vegetal_df.drop(vegetal_df[(vegetal_df['Zone']=='Chine - RAS de Hong-Kong') | (vegetal_df['Zone']=='Chine, Taiwan Province de') | (vegetal_df['Zone']=='Chine, continentale') | (vegetal_df['Zone']=='Chine - RAS de Macao')].index, inplace=False)


# In[39]:


#verification par l exemple du blé en france 
bléFrance=vegetal_pd[(vegetal_pd['Zone'] == 'France') & (vegetal_pd['Produit'] == 'Blé')]
bléFrance.head(1)


# In[40]:


#Disponibilité intérieure
bléFrance[bléFrance['Élément'] == 'Disponibilité intérieure'].Valeur


# In[41]:


# faire la somme pour verifier l equation de la disponibilite interieur
dispoInter1 =(int(bléFrance[bléFrance['Code Élément'] == 5511].Valeur) 
            + int(bléFrance[bléFrance['Code Élément'] == 5611].Valeur) 
            - int(bléFrance[bléFrance['Code Élément'] == 5911].Valeur) 
            + int(bléFrance[bléFrance['Code Élément'] == 5072].Valeur))
dispoInter1      


# In[42]:


# faire la somme pour verifier l equation de la disponibilite interieur

dispoInter2=(int(bléFrance[bléFrance['Code Élément'] == 5142].Valeur) 
    + int(bléFrance[bléFrance['Code Élément'] == 5521].Valeur) 
    + int(bléFrance[bléFrance['Code Élément'] == 5123].Valeur)
    + int(bléFrance[bléFrance['Code Élément'] == 5527].Valeur)
    + int(bléFrance[bléFrance['Code Élément'] == 5154].Valeur)
    + int(bléFrance[bléFrance['Code Élément'] == 5131].Valeur)
  )

dispoInter2


# In[43]:


dispoInter1==dispoInter2

l'équation est verifié pour le Blé en France
# # Question 3 : Calculez (pour chaque pays et chaque produit) la disponibilité alimentaire en kcal puis en kg de protéines.

# In[44]:



animaux_df.Zone.unique()


# In[45]:


animaux_pd=animaux_df.drop(animaux_df[(animaux_df['Zone']=='Chine - RAS de Hong-Kong') | (animaux_df['Zone']=='Chine, Taiwan Province de') | (animaux_df['Zone']=='Chine, continentale') | (animaux_df['Zone']=='Chine - RAS de Macao')].index, inplace=False)


# In[46]:




vegetal_pd.head(1)


# In[47]:


#on rajoute un collonne Type
animaux_pd['Type'] = 'Ani'
vegetal_pd['Type'] = 'Veg'


# In[48]:


#ON RAJOUTE LA TABLE animal a la tabl evegetal pour avoir tout les produitsdans une meme table et cela grace a apend 

vegetal=pd.DataFrame(animaux_pd.append(vegetal_pd))

vegetal.head(1)


# In[49]:


population=pop.rename(columns={"Valeur":"NombreDePopulation","Unité":"UniteDePopulation"})


# In[50]:


#jointure des deux tables vegetaux et population
dispo=pd.merge(population,vegetal,on = 'Zone')


# In[51]:


#multiplication de collonne valeur de la disponibilite allimentaire *nombre de population par ans 
multipli=dispo.assign(mult=dispo.NombreDePopulation*1000*dispo.Valeur*365)
multipli.head(1)


# In[52]:


#selectioner les lignes element =disponibilité alimentaire (Kcal/personne/jour)
dis=pd.DataFrame(multipli[(multipli['Élément'] == 'Disponibilité alimentaire (Kcal/personne/jour)')])
dis.head(1)


# In[53]:


#grouper par produit et zone et valeurs d la disponibilite alimentaire pour chaque pay de chaque produit en kcal
dispoAlimentaire= dis.groupby(["Produit", "Zone"])['mult'].agg('sum')
print('la disponibilité alimentaire en kcal pour chaque pays et chaque produit:')
dispoAlimentaire


# In[54]:


#disponibilité Alimentaire Totale en kcal
disponibilitéAlimentaireCal=dis['mult'].sum()
print('la disponibilité Alimentaire Totale en kcal est de:',disponibilitéAlimentaireCal,'kcal')


# In[55]:


#selectioner les lignes eyant l element dispo en proteines et valeurs
disPro=pd.DataFrame(multipli[(multipli['Élément']== 'Disponibilité de protéines en quantité (g/personne/jour)')])
disPro.head(1)


# In[56]:


#grouper par produit et zone 
#la disponibilite en proteine des produits il faut le convertir en KG

dispoProtein= disPro.groupby(["Zone","Produit"])['mult'].agg('sum')/1000
print('la disponibilité en protein pour chaque pay et chaque produit:')
dispoProtein


# In[57]:


disponibiliteProteinPro=disPro['mult'].sum()/1000
print('la disponibilité alimentaire en kg de proteine est:',disponibiliteProteinPro,'kg')


# # Question 4 : A partir de ces dernières informations, et à partir du poids de la disponibilité alimentaire (pour chaque pays et chaque produit), calculez pour chaque produit le ratio "énergie/poids", que vous donnerez en kcal/kg. Vous pouvez vérifier la cohérence de votre calcul en comparant ce ratio aux données disponibles sur internet, par exemple en cherchant la valeur calorique d'un oeuf.

# In[58]:


#selectioner les lignes eyant l element dispo en proteine
qAlim=pd.DataFrame(multipli[(multipli['Élément']== 'Disponibilité alimentaire en quantité (kg/personne/an)')])
qAlim.head(1)


# In[ ]:





# In[59]:


qValAlim=pd.DataFrame(qAlim.rename(columns={'Valeur':'ValeurQantité'}))
qValAlim.head(1)


# In[60]:


qValAlim=pd.DataFrame(qValAlim[['Zone','ValeurQantité']])


# In[61]:


unionRatio=pd.merge(disPro,qValAlim)
unionRatio.head(2)


# In[62]:



pivo = vegetal.pivot_table(index=['Zone','Code zone', 'Code Produit','Produit','Type'], columns='Élément', values='Valeur',
           aggfunc = sum).reset_index()
pivo.head(3)


# In[63]:


pivot=pd.DataFrame(pivo.assign(Ratio=pivo['Disponibilité alimentaire (Kcal/personne/jour)']  
                                                        / (pivo['Disponibilité alimentaire en quantité (kg/personne/an)']/365)))
Test=pd.DataFrame(pivot['Disponibilité alimentaire (Kcal/personne/jour)']>0)
Test


# In[64]:


ratProduit= pivot.groupby(["Zone","Produit"])['Ratio'].agg('sum')
ratProduit


# In[65]:


#comparer la valuer calorique d un oeuf
pivot[pivot['Produit'] == 'Oeufs'].head()


# # calculez également le pourcentage de protéines de chaque produit (pour chaque pays).

# In[66]:


pivotrat=pd.DataFrame(pivot.assign(TeneurPro=pivot['Disponibilité de protéines en quantité (g/personne/jour)']*365
                                                        / (pivot['Disponibilité alimentaire en quantité (kg/personne/an)'] *1000)*100))
pivotrat.head(3)
                      


# In[67]:


#comparer la valuer calorique d avoin
pivotrat[pivotrat['Produit'] == 'Avoine']


# # Question 5 : Citez 5 aliments parmi les 20 aliments les plus caloriques, en utilisant le ratio énergie/poids.

# In[68]:


pivotrat=pivotrat.replace([np.inf, -np.inf], np.nan).dropna(subset=['Ratio'], how="all")


# In[69]:



drop_dfRatio=pd.DataFrame(pivotrat[(pivotrat['Ratio'] != 0)]) 
drop_dfRatio


# In[ ]:





# In[70]:


gb_Rat=drop_dfRatio.groupby('Produit')['Ratio'].agg('mean')
gb_Rat


# In[71]:


print('les 5 aliments les plus caloriques :')

gb_Rat.nlargest(5)


# # Citez 5 aliments parmi les 20 aliments les plus riches en protéines.

# In[ ]:





# In[72]:


#enlever les valeurs nulls pour la teneur en protéine
drop_dfTeneurPro=pd.DataFrame(pivotrat[(pivotrat['TeneurPro'] != 0)]) 


# In[73]:


gb_Teneur=drop_dfTeneurPro.groupby('Produit')['TeneurPro'].agg('mean')
gb_Teneur


# In[74]:


print('les 5aliments les pls riches en protéine')
gb_Teneur.nlargest(5)


# # Question6:disponibilité intérieure mondiale exprimée en kcal
# 

# In[75]:


disInter=pivotrat
disInter.head(1)


# In[76]:


#ajouter une colone 'Disponibilité intérieure (Kcal)'] = ((disInterVeg['Disponibilité intérieure']*1000000)
disInter['Disponibilité intérieure (Kcal)']=((disInter['Disponibilité intérieure']*1000000)
                                                                  * disInter['Ratio'])


# In[77]:


#ce n est pas demande ici mais on aura besoin pour la question9 on calcul la dispo interieure en proteine en multipliant l disponibilte interieur de proteine par le pourcentage de proteines pour chaque produit
disInter['la Disponibilité interieure en kg de protéines']=disInter['Disponibilité intérieure']*1000000* disInter['TeneurPro']/100
disInter.head(1)


# In[78]:



disInterVeg = pd.DataFrame(disInter[(disInter['Type']== 'Veg')])
disInterVeg.head(1)


# In[ ]:





# In[79]:


gbDispoMondial= disInterVeg.groupby(["Produit"])['Disponibilité intérieure (Kcal)'].agg('sum')
gbDispoMondial


# In[ ]:





# In[ ]:





# In[80]:


DispoMondial= disInterVeg['Disponibilité intérieure (Kcal)'].sum()
print('la disponibilité intérieure en kcal et de:', DispoMondial)


# # Question7: Combien d'humains pourraient être nourris si toute la disponibilité intérieure mondiale de produits végétaux était utilisée pour de la nourriture ? 

L’EFSA a établi les besoins moyens (BM) en apports énergétiques pour les adultes
Femmes/hommes

50-59

2000-2500
source:https://www.efsa.europa.eu/fr/press/news/130110
# In[81]:



besoinE=2500


# In[82]:


#apport energetique /an
besoinEAn=2500*365
besoinEAn


# In[83]:


#perssonnes qui peuvent etre nouris par la dispo interieur monndiale  
PersoNouri=DispoMondial/besoinEAn


# In[1]:


#chifre en pourcentage
PopulationNouriEnCal=PersoNouri*100/hTotal
print('perssonnes qui peuvrent étre nourrits  par la disponibilité interieur mondial en énergie des produits vegetaux  est de:', PopulationNouriEnCal,%)


# In[ ]:





# In[86]:


#calculer la somme de la disponibilite alimentaire en kg de de proteine 

disInterproteines=disInterVeg['la Disponibilité interieure en kg de protéines'].sum()
print('la somme de la disponibilite alimentaire en kg de de protéine est de:', disInterproteines)


# # calcule de nombre d humain pouvant se nourire de la disponibilité en proteines 

# In[87]:


#le besoin journalier en proteines en kg
#58,5,42
besoinProAn=(58.5/1000)*365

besoinProAn


# In[88]:


#nombre de population pouvant se nourire de la disponibilité en proteines
PopulationNouriEnPro=disInterproteines/besoinProAn
PopulationNouriEnPro


# In[89]:


#le pourcentage de la population pouvant se nourir de la disponibilité en protéine 
pourcPopNouriEnPro=PopulationNouriEnPro*100/hTotal
print('le pourcentage de la population pouvant se nourir de la disponibilité en protéine', pourcPopNouriEnPro)


# In[90]:


animaux_pd= pd.read_csv('D:\\openclassroom\\projet3\\DonneesFAO_2013_fr/fr_animaux.csv')
animaux_pd.head(1)


# # question08: d'humains pourraient être nourris si toute la disponibilité alimentaire en produits végétaux la nourriture végétale destinée aux animaux et les pertes de produits végétaux étaient utilisés pour de la nourriture ? Donnez les résultats en termes de calories, puis de protéines, et exprimez ensuite ces 2 résultats en pourcentage de la population mondiale.

# In[91]:


disInterVeg.head(1)


# In[92]:


#Trouver la disponiilite alimentaire des vegetaux en kcal 5(choisir la nouriture)
lignDispoAlimVegCal=dis.loc[dis['Type']== 'Veg']
lignDispoAlimVegCal.head(1)


# In[93]:


#Trouver la disponiilite alimentaire des vegetaux en proteine
lignDispoAlimVegPro=disPro.loc[disPro['Type']== 'Veg']
lignDispoAlimVegPro.head(1)


# In[94]:



#disponibilité alimentaire vegetale en kcal 

dispoAlimVegCal=lignDispoAlimVegCal['mult'].sum()
dispoAlimVegCal


# In[95]:


#disponibilité alimentaire vegetale en proteines et convertir en kg de proteines 

dispoAlimVegPro=(lignDispoAlimVegPro['mult']/1000).sum()
dispoAlimVegPro


# In[96]:


#trouver les pertes en kcal
pertCal=((disInterVeg['Pertes']*1000000)*(disInterVeg.Ratio)).sum()
pertCal


# In[97]:


pertPro=((disInterVeg['Pertes']*1000000)*(disInterVeg.TeneurPro)/100).sum()
pertPro


# In[98]:


AliAnimCal=((disInterVeg['Aliments pour animaux'])*1000000*(disInterVeg.Ratio)).sum()
AliAnimCal


# In[99]:


AliAnimPro=((disInterVeg['Aliments pour animaux'])*1000000*(disInterVeg.TeneurPro)/100).sum()
AliAnimPro


# In[100]:


#la somme dela disponibilite en kcal
dispoAlimentVeAnPert=pertCal+AliAnimCal+dispoAlimVegCal
dispoAlimentVeAnPert


# In[ ]:





# In[101]:



dispoProAlimentVeAnPert=AliAnimPro+pertPro+dispoAlimVegPro
dispoProAlimentVeAnPert


# In[102]:



PerNouriPerAliAnimalCal=dispoAlimentVeAnPert/besoinEAn
PerNouriPerAliAnimalCal


# In[103]:



pourPerNouriPerAliAnimalCal=PerNouriPerAliAnimalCal*100/hTotal
print('le pourcentage de personne pouvant se nourrir de la disponibilité en calories de la nourriture pour animaux et pertes est de:', pourPerNouriPerAliAnimalCal)


# In[104]:



PerNouriPerAliAnimalPro=dispoProAlimentVeAnPert/besoinProAn
PerNouriPerAliAnimalPro


# In[105]:


#pourcentage de personne nourris en proteines de produits végétaux  alimants pour animaux, pértes,disponibilité
pourPerNouriPerAliAnimalPro=PerNouriPerAliAnimalPro*100/hTotal
print('pourcentage de personne nourris en proteines de produits végétaux  alimants pour animaux, pértes', pourPerNouriPerAliAnimalPro)


# # Question9: combien de perssonnes qui peuvent etre nouris avec la disponibilité en nouriture mondiale 
# 

# In[106]:


dispoInterTCal=(disInter['Disponibilité intérieure (Kcal)']).sum()
dispoInterTCal


# In[107]:


# personne nourris personnes en calories de disponibilite alimentaire
popNouriDispoCal=dispoInterTCal/besoinEAn
popNouriDispoCal


# In[ ]:





# In[108]:


# personne nouris personnes en calories de disponibilite alimentaire
pourpopNouriDispoCal=popNouriDispoCal*100/hTotal
print('personne nouris personnes en calories de disponibilite alimentaire', pourpopNouriDispoCal)


# In[109]:


#disponibilite alimentaire en kg de  proteine


# In[110]:


#calculer la somme de la disponibilite alimentaire en kgd de proteine 

disInterTpro=disInter['la Disponibilité interieure en kg de protéines'].sum()
disInterTpro


# In[111]:


# personne nouris personnes en proteines de disponibilite alimentaire
PerNourdisPro=disInterTpro/besoinProAn
PerNourdisPro


# In[112]:


# pourcentage de perssonnes qui peuvent etre nouris avec la disponibilité en nouriture mondiale
pourpopNouriDispoPro=PerNourdisPro*100/hTotal
print('pourcentage de perssonnes qui peuvent étre nourris avec la disponibilité en nouriture mondiale', pourpopNouriDispoPro)


# # Question10: Quelle proportion de la population mondiale est considérée comme étant en sous-nutrition ?

# In[ ]:





# In[113]:



snutrission_df.head(1)


# In[114]:


snutrission_df.Zone.unique()


# In[ ]:





# In[115]:


#la chine se trouve en tant que pays en entier mais egalement en tant que provinces separées


# In[116]:


snutrission=snutrission_df.drop(snutrission_df[(snutrission_df['Zone']=='Chine - RAS de Hong-Kong') | (snutrission_df['Zone']=='Chine, Taiwan Province de') | (snutrission_df['Zone']=='Chine, continentale') | (snutrission_df['Zone']=='Chine - RAS de Macao')].index, inplace=False)


# In[117]:


snutrission.Année.unique()


# snutrission.Valeur.unique()

# In[118]:


snutrission.Valeur.unique()


# In[119]:


snutrission.Produit.unique()


# In[ ]:





# In[120]:


s=snutrission[(snutrission.Produit==0) & (snutrission.Valeur!=0)]
s


# In[121]:


#ici on remarque la presence d un charactere qu on doit transformer en un nombre  0
snutrission.loc[snutrission['Valeur'] == '<0.1'] = 0
snutrission.head(2)


# In[122]:


#On transforme le contenue de la colonne valeur en valeurs numerique pour pouvoir les additionner 
snutrission['Valeur']=pd.to_numeric(snutrission['Valeur'])


# In[123]:


#Snouri=snutrission[(snutrission[]]


# In[124]:


#il faut expliquer pour les autres années
gb_Snouri=pd.DataFrame(snutrission.groupby(["Année"])['Valeur'].agg('sum')*1000000)
gb_Snouri


# In[125]:


gb_an1=gb_Snouri.iloc[1]
gb_an1                    


# In[126]:


#on a trouver la valeur des humains en sous nutrission en periode entre 2012et 2014( donc 2013 compris )
humEnSNutrission=(gb_an1.Valeur)
humEnSNutrission


# In[127]:


#proportion d humain en sous nutrission on dvise la valeur des humains en sous nutrission en periode entre 2012et 2014 par la population total
porhumEnSNutrission=humEnSNutrission*100/hTotal
print('la proportion de la population mondiale est considérée comme étant sous-nutrition:',porhumEnSNutrission)


# # Question11:En ne prenant en compte que les céréales destinées à l'alimentation (humaine et animale), quelle proportion (en termes de poids) est destinée à l'alimentation animale ?

# In[128]:



cereales_df.Zone.unique()


# In[129]:


#on supprime les provinces de la chine et on garde la chine  
cereales_pd=cereales_df.drop(cereales_df[(cereales_df['Zone']=='Chine - RAS de Hong-Kong') | (cereales_df['Zone']=='Chine, Taiwan Province de') | (cereales_df['Zone']=='Chine, continentale') | (cereales_df['Zone']=='Chine - RAS de Macao')].index, inplace=False)


# In[130]:


#on rajoute une collone Qualité aux ceriales 
cereales_cer=cereales_pd.assign(Famille='cer')
cereales_cer.head(3)


# In[131]:


cereales_df=pd.DataFrame(cereales_cer[['Code zone','Zone','Produit','Année','Valeur','Famille']])
cereales_df


# In[132]:


#on renome la collonne valeur pour pas confondre avec la valeur de l'autre table  
cereales_re=cereales_df.rename(columns={'Valeur':'Quantité totale de Céréales'})
cereales_re.head(10)


# In[133]:


#on reunit les deux table
cermerg=pd.merge(cereales_re,disInterVeg)
cermerg.head(3)


# In[134]:


#on filtre on ne gardant que la famille des cereales 
cerAnimHum=cermerg.loc[cermerg['Famille']== 'cer']
cerAnimHum.head(1)


# In[135]:


#on remplace les nan par 0 pour pouvoir faire des calcules 
cerAnimHum=cerAnimHum.replace(np.nan,0)
cerAnimHum.head(3)


# In[136]:


#on rajoute une colonne ou on fait la somme nourriture et aloment pour animeaux
cerAnimHums=pd.DataFrame(cerAnimHum.assign(sommeAnimaletHumains =cerAnimHum['Nourriture']+(cerAnimHum['Aliments pour animaux']) ))
cerAnimHums.head(3)


# In[137]:


#on fait la somme des données de la colonne sommeAnimaletHumains
sCereale=cerAnimHums['sommeAnimaletHumains'].sum()
sCereale


# In[138]:


#on fait la somme des données de la colonne Aliments pour animaux
sCerAnim=cerAnimHums['Aliments pour animaux'].sum()
sCerAnim


# In[139]:


#proportion  de cereale destine aux animeaux par raport a la nouriture est 
propAnimeauNouriture=sCerAnim*100/sCereale
print('proportion  de cereale destine aux animeaux par raport a la nouriture est de:', propAnimeauNouriture,'%')

# recencer les pays en sous nutrission

# In[2]:


#on choisi l'année 2013 qui se situe entre '2012-2014' et fixe la condition valeur>0
paySsNouri=snutrission.loc[(snutrission['Année'] == '2012-2014') & (snutrission['Valeur'] > 0)]
paySsNouri.head(3)


# In[3]:


#isi on choisi les pays qui sont concidéré comme etant sous nourris present dans la table paySsNouri

paySsNourisp=pivot[pivot['Zone'].isin(paySsNouri['Zone'])]
paySsNourisp.head(3)


# In[4]:


#on renomme la valeur 
paySsNouri=paySsNouri.rename(columns={"Valeur":"Valeur_Sous_Nouris"})


# In[144]:


#on Repére les 15 produits les plus exportés par les pays sous nourris on les classant du plus haut au plus faible exportation .
gb_Snouri=pd.DataFrame(paySsNourisp.groupby("Produit").agg('sum').reset_index().sort_values(by='Exportations - Quantité', ascending=False)[:15])
gb_Snouri.head(3)


# In[145]:


prod_Snouri=gb_Snouri[['Produit','Exportations - Quantité']]
print('les 15 produit exportés par les pays sous nouris sont:')
prod_Snouri


# In[146]:


grand_import = pivot[pivot['Produit'].isin(gb_Snouri['Produit'])]
grand_import.head(3)


# In[ ]:





# In[147]:


prodAsc=grand_import.sort_values(by='Importations - Quantité', ascending=False)[:200]
prodAsc.head(3)


# In[148]:


#Groupez ces importations par produit, afin d'avoir une table contenant 1 ligne pour chacun des 15 produits
gb_Snouri=pd.DataFrame(prodAsc.groupby('Produit').agg('sum').reset_index())
gb_Snouri.head(3)


# In[149]:


#le ratio entre la quantité destinés aux "Autres utilisations" (Other uses) et la disponibilité intérieure.
RatioAutreUs=gb_Snouri.assign(Ratio_Other_uses=(gb_Snouri['Autres utilisations (non alimentaire)'])/(gb_Snouri['Disponibilité intérieure'])
)
RatioAutreUs.head(3)


# In[150]:


somAlim=RatioAutreUs['Aliments pour animaux']+RatioAutreUs.Nourriture


# In[151]:


#le ratio entre la quantité destinée à la nourriture animale et la quantité destinée à la nourriture (animale + humaine)
RatioAlim=RatioAutreUs.assign(Ratio_aliments=(RatioAutreUs['Aliments pour animaux'])/somAlim)
RatioAlim


# In[184]:


Ratio_Alim_animaux=(RatioAlim.Ratio_aliments).sum()
print('la proportion (en termes de poids) destinée à l\'alimentation animale',Ratio_Alim_animaux,'%')


# # Question 12 :  les 3 produits qui ont la plus grande valeur pour chacun des 2 ratios 

# In[153]:


RatioautreOrd=RatioAlim[['Produit','Ratio_Other_uses']]


# In[154]:


RatioAlimOrd=RatioAlim[['Produit','Ratio_aliments']]


# In[155]:


#les 3 premier produit pour le ratio autre usage/disponibilité allimentaire
RatioautreOrd.sort_values(by='Ratio_Other_uses', ascending=False)[:3].reset_index()


# In[156]:


#le ratio entre la quantité destinée à la nourriture animale et la quantité destinée à la nourriture (animale + humaine)
RatioAlimOrd.sort_values(by='Ratio_aliments', ascending=False)[:3].reset_index()


# # Question 13 : la quantité de céréales qui pourraient être libérées si les USA diminuaient leur production de produits animaux de 10% 

# In[ ]:





# In[157]:


cerUsa=cerAnimHums.loc[cerAnimHums['Zone'] == "États-Unis d\'Amérique"]
cerUsa


# In[158]:


#quantité de ceréale libéré = la quantité de ceréale consommée par les animeaux
qCerLibére=(cerUsa['Aliments pour animaux'].sum())*10/100
print('la quantité de céréales qui pourraient être libérées si les USA diminuent leur production de produits animaux de 10% est de:', qCerLibére,'tonne')


# # Question 14 : En Thaïlande, quelle proportion de manioc est exportée ? Quelle est la proportion de personnes en sous-nutrition?

# In[159]:



thailandeInfo=pd.DataFrame(pivot.loc[(pivot['Zone'] == 'Thaïlande')&(pivot['Produit'] == 'Manioc')])
thailandeInfo


# In[160]:


#la proportion du manioc exporté est:'
proManiocExpTailande1=thailandeInfo['Exportations - Quantité']


# In[161]:


proManiocExpTailande2=thailandeInfo['Production']


# In[162]:


#la proportion du manioc exporté est:
proManiocExpTailande=(thailandeInfo['Exportations - Quantité']/thailandeInfo['Production'])*100
print('la proportion du manioc exporté en thailande est de:', proManiocExpTailande)


# In[163]:


#la proportion de personnes en sous-nutrition


# In[164]:


#Valeur de population sous nouris
thailandeInfoPopSsN=snutrission.loc[(snutrission['Zone'] == 'Thaïlande')&(snutrission['Année'] == '2012-2014')]
thailandeInfoPopSsN


# In[165]:


#Valeur de population sous nouris
thailandeInfoPopSsNouris=int(thailandeInfoPopSsN['Valeur'])*1000000
thailandeInfoPopSsNouris


# In[166]:


#Valeur de la population totale
thailandeInfoPop=pop.loc[(pop['Zone'] == 'Thaïlande')]
thailandeInfoPop


# In[167]:


#Valeur de la population totale
thailandeInfoPopST=int(thailandeInfoPop.Valeur)*1000
thailandeInfoPopST


# In[168]:


#la portion de la population sous nouris en thailand:
sPopTailand=int(thailandeInfoPopSsNouris/(thailandeInfoPopST)*100)
print('la portion de la population sous nourris en thailand est de:',sPopTailand,'%')


# # Base de données MySQL

# In[169]:


populationRename=population_pd.rename(columns={'Valeur':'population','Année':'annee','Zone':'pays','Code zone':'code_pays'})


# In[170]:


#table population
populationSQL=populationRename[['pays', 'code_pays', 'annee', 'population']]


# In[171]:


populationSQL.to_csv("population_SQL.csv", index = False)


# In[ ]:





# In[172]:


import mysql.connector


# # Question 15 : Proposez une clé primaire pertinente pour cette table.Population2013

# In[173]:


table_pivoté= pd.DataFrame(vegetal.pivot_table(index=['Zone','Code zone','Code Produit','Produit','Type','Année'], columns='Élément', values='Valeur',
           aggfunc = sum).reset_index())
table_pivoté


# # Question 16 :  

# In[174]:


rename_colomn=table_pivoté.rename(columns={'Code zone':'code_pays','Zone':'pays','Année':'année','Code Produit':'code_produit','Produit':'poduit','Type':'origine','Disponibilité alimentaire (Kcal/personne/jour)':'dispo_alim_kcal_p_j','Nourriture':'dispo_alim_tonnes','Disponibilité intérieure':'dispo_int','Disponibilité de matière grasse en quantité (g/personne/jour)':'dispo_mat_gr','Disponibilité de protéines en quantité (g/personne/jour)':'dispo_prot','Disponibilité intérieure':'dispo_int','Aliments pour animaux':'alim_ani','Semences':'semences','Pertes':'pertes', 'Traitement':'transfo', 'Nouriture':'nourriture','Autres utilisations (non alimentaire)':'autres_utilisations'})


# In[175]:


dispo_alim=rename_colomn[['code_pays','pays','année','code_produit','poduit','origine','dispo_alim_kcal_p_j','dispo_alim_tonnes','dispo_mat_gr','dispo_prot']]
dispo_alim


# In[176]:


dispo_alim.to_csv("dispo_alim_SQL.csv", index = False)


# #une clé primaire pertinente pour cette table:code produit

# # Question 17 :

# In[177]:


rename_colomn2=table_pivoté.rename(columns={'Code zone':'code_pays','Zone':'pays','Année':'année','Code Produit':'code_produit','Produit':'poduit','Type':'origine','Disponibilité alimentaire (Kcal/personne/jour)':'dispo_alim_kcal_p_j','Nourriture':'nourriture','Disponibilité intérieure':'dispo_int','Disponibilité de matière grasse en quantité (g/personne/jour)':'dispo_mat_gr','Disponibilité de protéines en quantité (g/personne/jour)':'dispo_prot','Disponibilité intérieure':'dispo_int','Aliments pour animaux':'alim_ani','Semences':'semences','Pertes':'pertes', 'Traitement':'transfo', 'Nouriture':'nourriture','Autres utilisations (non alimentaire)':'autres_utilisations'})


# In[178]:


equilibre_prod=rename_colomn2[['code_pays','pays','année','code_produit','poduit','dispo_int','dispo_mat_gr','dispo_prot','alim_ani','semences','pertes','transfo','nourriture','autres_utilisations']]
equilibre_prod


# In[179]:


equilibre_prod.to_csv("equilibre_prod_SQL.csv", index = False)


# In[180]:


rename_snutrission=snutrission.rename(columns={'Zone':'pays','Code zone':'code_pays', 'Année':'année', 'Valeur':'nb_personnes'})
rename_snutrission


# In[181]:


sous_nutrition=rename_snutrission[['pays', 'code_pays', 'année','nb_personnes']]
sous_nutrition


# In[182]:


sous_nutrition=sous_nutrition.loc[sous_nutrition.année== '2012-2014']
sous_nutrition


# In[183]:


sous_nutrition.to_csv("sous_nutrition_SQL.csv", index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




