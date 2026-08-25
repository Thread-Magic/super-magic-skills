---
name: Triage d'hameçonnage (French)
description: Triage d'hameçonnage d'un e-mail suspect: évaluer sans toucher la charge, mesurer le rayon d'exposition, contenir si malveillant, répondre au déclarant.
category: Localized
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Triage d'hameçonnage (French)

**Quand l'utiliser :** un utilisateur a transféré quelque chose de louche (« est-ce de l'hameçonnage ? »), un ticket de signalement arrive sur le tableau sécurité, ou un technicien veut un second avis avant de libérer ou supprimer un message.

**Exécuter :** sur un seul message signalé.

## Prompt

```
Mène un e-mail suspect signalé à un verdict documenté.

1. Capture les indicateurs du ticket en texte seul : adresse et nom affiché de l'expéditeur, reply-to, sujet, heure d'envoi, chaque cible de lien telle qu'écrite, noms et types des pièces jointes. N'ouvre, ne clique, ne télécharge ni n'affiche jamais un lien ou une pièce jointe du message, pas même « pour voir ».
2. Branche simulation : compare l'expéditeur et les domaines de liens aux domaines de simulation documentés du client dans la base de connaissances. Uniquement sur correspondance exacte avec un domaine de simulateur documenté → classe en simulation, clos en interne par une note en texte brut nommant le domaine, et ne réponds PAS au client (cela fausse les métriques de son programme). Arrête-toi là. Une correspondance partielle n'en est pas une : jamais de vrai hameçonnage clos en simulation, jamais d'incident réel déclenché pour une simulation.
3. Évalue les indicateurs : domaine sosie ou cousin, leviers d'urgence ou paiement, lien de collecte d'identifiants (texte affiché différent de la cible réelle), pièces jointes inattendues, détournement d'un fil antérieur. En-têtes complets collés : confie l'analyse fine à email-header-analysis.
4. Rayon d'exposition : cherche le même expéditeur ou sujet dans les tableaux et tickets récents du client. Détermine qui d'autre l'a reçu et — point critique — si quelqu'un a cliqué, répondu, saisi des identifiants ou ouvert une pièce jointe. N'affirme jamais « personne d'autre ne l'a reçu » sur une recherche plafonnée ; écris « aucun autre signalement dans les N derniers tickets parcourus » (skill de base Sweep Honesty).
5. Si quelqu'un a interagi avec un message jugé malveillant, escalade immédiatement et lance compromised-account-containment pour les utilisateurs touchés. Le confinement prime sur la rédaction.
6. Rends le verdict. Malveillant → quarantaine/retrait de toutes les boîtes destinataires, blocage expéditeur et domaine à la passerelle, réinitialisation des identifiants de quiconque a cliqué. Suspect mais non confirmé → dis-le ainsi, avec ce qui le confirmerait. Légitime → explique les signaux qui l'innocentent.
7. Réponds au déclarant en brouillon ouvert et remercie-le ; consigne verdict, preuves et raisonnement en note interne en texte brut, sans markdown ni émojis (skill de base PSA Note Discipline), puis classe le ticket et fixe son statut. Documente la décision, pas seulement l'action.

Convention française : vocabulaire défensif — « message signalé », « tentative présumée » ; jamais « piratage » ni « fuite de données » avant confirmation formelle. Réponse au déclarant au vouvoiement, avec remerciement explicite. Horodatages JJ/MM/AAAA et 24 h avec fuseau (« 15/07/2026 09 h 12 CET »). Recopie les indicateurs techniques (en-têtes, URL, noms de fichiers) verbatim en anglais : preuves et clés de recherche. En cas de doute, contiens.
```
