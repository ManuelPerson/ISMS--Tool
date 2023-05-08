import sys

# Schritt 1
print("Initiierung des Sicherheitsprozesses. Die Verantwortung verbleibt vollständig bei der obersten Leitungsebene.")
print("Initiierung des Sicherheitsprozesses. Die Leitungsebene muss den Sicherheitsprozess initiieren, steuern und kontrollieren. "
      "\nHierfür sind einerseits strategische Leitaussagen zur Informationssicherheit und andererseits organisatorische Rahmenbedingungen erforderlich.")
print("Hinweis: Die Verantwortung für Informationssicherheit verbleibt in jedem Fall bei der obersten Managementebene, "
      "\ndie Aufgabe „Informationssicherheit“ wird allerdings typischerweise an einen Beauftragten für Informationssicherheit bzw. ein ISMS- Team delegiert.")
print("Bitte bestätigen Sie, dass das ISMS durch die Leitungsebene initiiert und die Verantwortung durch diese vollständig übernommen wurde. "
      "\nFalls die Leitungsebene sich gegen die Einführung geeigneter Sicherheitsmaßnahmen entscheidet, "
      "\nsind Sie in Ihrer Funktion als ISB / ISO verpflichtet, dies durch eine Unterschrift der Geschäftsleitung bestätigen zu lassen.")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 1 abgeschlossen.")
else:
    print("Bitte achten Sie auf die korrekte Initiierung des Sicherheitsprozesses und die Übernahme der Verantwortung durch die Geschäftsleitung.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. Bitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 2
print("Konzeption und Planung des Sicherheitsprozesses und Bereitstellung von finanziellen, personellen und zeitlichen Ressourcen.")
print("Bitte bestätigen Sie, dass die Konzeption und Planung des Sicherheitsprozesses abgeschlossen ist und ausreichende finanzielle, "
      "\npersonelle und zeitliche Ressourcen bereitgestellt wurden.")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 2 abgeschlossen.")
else:
    print("Die Geschäftsleitung konzipiert und plant den Sicherheitsprozess und stellt ausreichende Ressourcen bereit. "
          "\nIst dies nicht der Fall, darf kein ISMS implementiert werden.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 3
print("Die Entscheidung bezüglich der Vorgehensweise (z.B. Basis-, Kern-, Standard-Absicherung) lieget im Verantwortungsbereich der Geschäftsleitung.")
print("Bitte bestätigen Sie, dass eine Vorgehensweise ausgewählt wurde.")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 3 abgeschlossen.")
else:
    print("Alleine die Leitungsebene darf eine geeignete Vorgehensweise bezüglich der Absicherungsarten wählen/ festlegen.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt X
print("Die Erstellung der Leitlinie zur Informationssicherheit, liegt im Verantwortungsbereich der Geschäftsleitung.")
print("Hinweis: Die Leitlinie beschreibt, welche Sicherheitsziele und welches Sicherheitsniveau die Institution anstrebt, "
      "\nwas die Motivation hierfür ist und mit welchen Maßnahmen und mit welchen Strukturen dies erreicht werden soll. "
      "\nAlle Mitarbeiter sollten daher die Inhalte der Sicherheitsleitlinie kennen")
print("Bitte bestätigen Sie, dass eine Leitlinie zur Informationssicherheit erstellt wurde, und die Leitline allen Mitarbeitern bekannt gegeben wurde .")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt X abgeschlossen.")
else:
    print("Allein die Leitungsebene darf eine geeignete Vorgehensweise bezüglich der Absicherungsarten wählen "
          "\nund eine Leitlinie zur Informationssicherheit erstellen. Ebenso müssen durch die Geschäftsleitung Rollen und Aufgaben benannt und verteilt werden.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 4
print("Aufbau einer geeigneten Organisationsstruktur für das Informationssicherheitsmanagement.")
print("Hinweis: Für das Informationssicherheitsmanagement muss eine, für Größe und Art der Institution geeignete Organisationsstruktur aufgebaut werden.")
print("Bitte bestätigen Sie, dass eine geeignete Organisationsstruktur (ggf. ISMS-Team) für das Informationssicherheitsmanagement durch die, "
      "\nvon der Geschäftsleitung benannten Personen aufgebaut wurde.")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 4 abgeschlossen.")
else:
    print("Bitte bauen Sie gemeinsam mit der Leitungsebene eine geeignete Organisationsstruktur für das Informationssicherheitsmanagement auf.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 5
print("Erstellung einer Sicherheitskonzeption. Die Umsetzung der Sicherheitskonzeption wird durch die Geschäftleitung beauftragt.")
print("Hinweis: Nachdem ein Informationssicherheitsprozess initiiert wurde und die Sicherheitsleitlinie "
      "\nund Informationssicherheitsorganisation definiert wurden, wird die Sicherheitskonzeption für die Institution erstellt. "
      "\nAls Grundlage hierfür finden sich in den Bausteinen des IT-Grundschutz-Kompendiums für typische Komponenten von Geschäftsprozessen, "
      "\nAnwendungen, IT-Systeme und weitere Objekte entsprechende Sicherheitsanforderungen nach dem Stand der Technik.")
print("Bitte bestätigen Sie, dass eine Sicherheitskonzeption erstellt und die Umgesetzung von der Geschäftsleitung in Auftrag gegeben wurde.")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 5 abgeschlossen.")
else:
    print("Bitte achten Sie darauf, das eine durch die Geschäftsleitung abgenommene und unterschiebene Sicherheitskonzeption vorliegt "
          "\nund setzen Sie diese Ihrem Auftrag entsprechend um. Starten Sie nun mit der implementierung des ISMS.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 6
print("Definition des Informationsverbunds im Geltungsbereich.")
print("Wurde der Geltungsbereich der IT-Grundschutzmaßnahmen definiert und festgelegt?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 6 abgeschlossen.")
else:
    print("Bitte achten Sie zunächst darauf, dass Geltungsbereich der IT-Grundschutzmaßnahmen klar definiert wurde.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 7
print("Durchführung einer Strukturanalyse und Erstellung des Netzwerkplans.")
print("Haben Sie eine übersichtliche Struktur des Informationsverbunds erstellt?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 7 abgeschlossen.")
else:
    print("Bitte führen Sie die Strukturanalyse und die Erstellung eines Netzwerkplans durch.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 8
print("Durchführung einer Schutzbedarfsfeststellung.")
print("Haben Sie den Schutzbedarf für die einzelnen Komponenten innerhalb des Informationsverbunds ermittelt?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 8 abgeschlossen.")
else:
    print("Bitte führen Sie eine Schutzbedarfsfeststellung durch.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 9
print("Modellierung des Informationsverbunds.")
print("Haben Sie ein Modell des Informationsverbunds erstellt?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 9 abgeschlossen.")
else:
    print("Bitte erstellen Sie zunächst ein Modell des Informationsverbunds. "
          "\nZur Modellierung nach IT-Grundschutz: "
          "\nUm einen im Allgemeinen komplexen Informationsverbund nach IT-Grundschutz zu modellieren,"
          "\nmüssen die passenden Bausteine des IT-Grundschutz-Kompendiums ausgewählt und umgesetzt werden. "
          "\nUm die Auswahl zu erleichtern, sind die Bausteine im IT-Grundschutz-Kompendium zunächst in prozess- und systemorientierte Bausteine aufgeteilt.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 10
print("Durchführung des IT-Grundschutz-Checks (Soll-Ist-Vergleich).")
print("Hinweis: Die Ergebnisse des IT-Grundschutz-Checks sollten so dokumentiert werden, "
      "\ndass sie für alle Beteiligten nachvollziehbar sind und als Grundlage für die Umsetzungsplanung der defizitären Anforderungen und Maßnahmen genutzt werden können.")
print("Haben Sie den IT-Grundschutz-Check durchgeführt?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 10 abgeschlossen.")
else:
    print("Bitte führen Sie zunächst den IT-Grundschutz-Check durch (Durchführung des Soll-Ist-Vergleichs). "
          "\nBei der Erhebung des erreichten Sicherheitsstatus werden die Sicherheitsanforderungen des jeweiligen Bausteins der Reihe nach durchgearbeitet")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 11
print("Die Risikoanalyse.")
print("Haben Sie eine Risikoanalyse durchgeführt?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 11 abgeschlossen.")
else:
    print("Bitte führen Sie zunächst eine Risikoanalyse durch.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut.'
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 12
print("Konsolidierung der Maßnahmen.")
print("Haben Sie nach der Risikoanalyse eine Liste aller erforderlichen Schutzmaßnahmen erstellt?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 12 abgeschlossen.")
else:
    print("Bitte erstellen Sie zunächst eine Liste aller erforderlichen Maßnahmen.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 13
print("Umsetzung aller Maßnahmen der in Schritt 12 aufgelisteten Maßnahmen.")
print("Haben Sie alle Maßnahmen Ihrer Liste umgesetzt? (begründen Sie ggf. die Nichtumsetzung in Ihrer Dokumentation.)")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 13 abgeschlossen.")
else:
    print("Bitte setzen Sie zunächst alle zutreffenden Maßnahmen um, oder begründen ggf. sie die Nichtumsetzung.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 14
print("Aufrechterhaltung und kontinuierliche Verbesserung der Informationssicherheit.")
print("Haben Sie sichergestellt, dass die Informationssicherheit kontinuierlich aufrechterhalten und verbessert wird?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 14 abgeschlossen.")
else:
    print("Bitte stellen Sie zunächst sicher, dass die Informationssicherheit kontinuierlich aufrechterhalten und verbessert wird.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 15
print("Fortentwicklung des ISMS.")
print("Entwickeln Sie das ISMS kontinuierlich weiter?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 15 abgeschlossen.")
else:
    print("Bitte entwickeln Sie das ISMS kontinuierlich weiter.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()
print("")
# Schritt 16
print("Erweiterung der gewählten Vorgehensweise.")
print("Erweitern Sie die gewählte Vorgehensweise (im Bezug auf Kern- und Standard-Absicherung) bei Bedarf?")
confirmation = input("Ja/Nein: ")
if confirmation.lower() == "ja":
    print("Schritt 16 abgeschlossen.")
    print("")
    print("Herzlichen Glückwunsch! Ihr ISMS ist nun implementiert. Ihr ISMS bedarf auch weiterhin kontinuierliche Verbesserung und Pflege.")
    print("Bleiben Sie also am Ball! Informationssicherheit ist kein einmalig herzustellender Zustand.")
    print("")
    print('Zum beenden des Programms drücken Sie bitte "Enter"')
    input("")
else:
    print("Bitte erweitern Sie die gewählte Vorgehensweise (Kern- und Standard-Absicherung) bei Bedarf. "
          "\nStarten Sie den Prozess zur Implementierung eines ISMS entsprechend der Anforderungen zur Absicherung erneut.")
    print('Bitte führen Sie zunächst die fehlenden Schritte aus und starten Sie das Programm erneut. '
          '\nBitte drücken Sie "Enter" um das Programm zu verlassen.')
    input("")
    sys.exit()