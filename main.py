def salaire_mensuel(salaire_annuel):
  salaire_mensuel = salaire_annuel / 12
  return salaire_mensuel


def salaire_hebdomadaire(salaire_mensuel):
  salaire_hebdomadaire = salaire_mensuel / 4
  return salaire_hebdomadaire


def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
  salaire_horaire = salaire_hebdomadaire / heures_travaillees
  return salaire_horaire

  #def main():
  salaire_annuel = int(input("Entrez votre salaire annuel: "))
  heures_travaillees = int(input("Entrez le nombre d'heures travaillées: "))
  calcul_salaire_mensuel = salaire_mensuel(salaire_annuel)
  calcul_salaire_hebdomadaire = salaire_hebdomadaire(calcul_salaire_mensuel)
  calcul_salaire_horaire = salaire_horaire(calcul_salaire_hebdomadaire,
                                           heures_travaillees)
  print("Votre salaire horaire est de ", calcul_salaire_horaire, " euros")