---
name: Synthèse quotidienne (French)
description: Synthèse quotidienne des tickets ouverts d'un technicien: qui attend réponse, ce qui est urgent, ce qui est planifié aujourd'hui, variante 3 lignes.
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Synthèse quotidienne (French)

**Quand l'utiliser :** un technicien veut la lecture du matin — tout ce qu'il a sur le feu, trié selon ce qui a besoin de lui maintenant, parcourable en moins d'une minute. « Fais-moi un récap de mes tickets ouverts », « synthèse du matin », « version courte ».

**Exécuter :** sur tous les tickets ouverts du membre qui la demande.

## Prompt

```
Produis la synthèse quotidienne des tickets ouverts du membre qui la demande.

1. Récupère tous les tickets ouverts affectés au membre demandeur (résous le membre au besoin). Si un plafond de résultats a pu tronquer la liste, dis-le d'emblée (« 50 affichés — il peut y en avoir davantage ») plutôt que de la présenter comme exhaustive.
2. Classe chaque ticket dans exactement une rubrique, dans cet ordre (un ticket tombe dans la première rubrique à laquelle il correspond) :
   - En attente de votre réponse — le client a répondu en dernier et attend. Trier par durée d'attente.
   - Urgent / à risque — priorité haute, SLA en dépassement ou proche, ou fil à sentiment négatif. Trier par gravité.
   - Planifié aujourd'hui — tickets avec entrée d'agenda ou suivi engagé pour aujourd'hui, ordre horaire.
   - En attente de tiers — client, fournisseur ou escalade a la main. Signaler ceux silencieux depuis 3 jours ou plus, sans laisser cette rubrique envahir le haut.
   - Tout le reste — un total et une caractérisation en une ligne, sans détail par ticket.
3. Chaque ligne de ticket tient sur une seule ligne : numéro, client (abrégé), état en 5 à 8 mots, prochaine action (« #1234 <client> — imprimante HS depuis 2 j, le client a répondu hier → confirmer que le correctif fonctionne »).
4. Ouvre par « Commencez ici : » le ticket le plus important et une phrase expliquant pourquoi (la réponse client qui attend depuis le plus longtemps prime sur une urgence vague ; un dépassement ferme de SLA prime sur tout).
5. Conclus par la physionomie de la journée : totaux par rubrique et une phrase.
6. Si la version courte est demandée (« 3 lignes »), produis exactement trois lignes : (1) Commencez ici + pourquoi, (2) les compteurs — X réponses attendues / Y urgents / Z planifiés, (3) la seule chose qui fera mal si elle est ignorée aujourd'hui. Ni en-têtes, ni préambule.
7. Propose la suite : « Voulez-vous des brouillons de réponse pour les tickets qui vous attendent ? »

Convention française : dates en JJ/MM/AAAA, heures en 24 h (« 10 h 00 »). La synthèse est interne — le tutoiement entre collègues est acceptable si c'est l'usage du desk ; abréviations desk (« HS », « RAS », « càd ») tolérées dans les lignes internes, jamais dans un texte client.

Garde-fous : limite-toi strictement aux tickets du membre demandeur ; n'inclus jamais les files des autres sauf demande explicite. Lecture seule — la synthèse ne modifie rien (pas de statut, note ni rappel) sauf demande de suite. N'invente jamais de numéros de ticket, d'échéances SLA ni de réponses client ; en cas d'ambiguïté, classe dans la rubrique la plus prudente (En attente de votre réponse). Chaque ligne doit être actionnable. En cas de doute, ne fais rien.

Variante non assistée (Flows — via Run Skill sur un événement ticket, jamais planifié) : ta réponse entière est livrée telle quelle comme briefing, sans narration ni questions ; toujours la ligne Commencez ici et les compteurs, sans proposition de suite. File vide → exactement : « Aucun ticket ouvert ne vous est affecté. Profitez de l'ardoise vierge. » Échec de la recherche → une seule ligne indiquant que la synthèse n'a pas pu être générée, jamais une synthèse fabriquée.
```
