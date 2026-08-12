---
name: Triage d'hameçonnage
description: Un utilisateur a signalé un e-mail suspect ou un ticket de signalement d'hameçonnage est arrivé sur le tableau sécurité — l'évaluer sans toucher à la charge, mesurer le rayon d'exposition, contenir si malveillant, et répondre au déclarant avec un verdict. (Phishing triage — assess without touching the payload, check blast radius, contain, reply to the reporter — in French.)
category: Localized
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Triage d'hameçonnage

**Quand l'utiliser :** un utilisateur a transféré quelque chose de louche (« est-ce de l'hameçonnage ? »), un ticket de signalement arrive sur le tableau sécurité, ou un technicien veut un second avis avant de libérer ou supprimer un message.

**Exécuter :** sur un seul message signalé.

## Prompt

```
Mène cet e-mail suspect signalé jusqu'à un verdict documenté.

1. Capture les indicateurs depuis le ticket sans interagir avec eux : adresse et nom d'affichage de l'expéditeur, reply-to, sujet, heure d'envoi, chaque cible de lien exactement telle qu'écrite, noms et types des pièces jointes. N'ouvre jamais de lien ni de pièce jointe, et ne récupère jamais une URL du message pour « voir ce que c'est ».
2. Branche simulation : compare l'expéditeur et les domaines des liens aux domaines documentés de la plateforme de simulation d'hameçonnage du client (cherche dans la base de connaissances la fiche du fournisseur de simulation). Correspondance avec un simulateur connu → classe en simulation, clos en interne avec une note en texte brut nommant le domaine apparié, et ne réponds PAS au client (une réponse fausse les métriques de son programme de simulation). Arrête-toi là.
3. Évalue les indicateurs : domaine sosie ou cousin, leviers d'urgence et de paiement, lien de collecte d'identifiants (décalage entre texte affiché et cible réelle), types de pièces jointes inattendus, détournement d'un fil réel antérieur. Si les en-têtes complets ont été collés, confie l'analyse fine au skill email-header-analysis et intègre son verdict.
4. Rayon d'exposition : cherche le même expéditeur ou le même sujet à travers les tableaux du client et les tickets récents. Détermine qui d'autre a reçu le message et — point critique — si quelqu'un a cliqué, répondu, saisi des identifiants ou ouvert une pièce jointe (identifie les destinataires dans la liste des contacts).
5. Si quelqu'un a interagi avec un message que tu juges malveillant → escalade immédiatement et lance le skill compromised-account-containment pour les utilisateurs touchés. Le confinement prime sur la fin de la rédaction : contiens vite, investigue ensuite.
6. Rends le verdict : Malveillant → conseille quarantaine/retrait de toutes les boîtes destinataires, blocage de l'expéditeur/domaine à la passerelle, réinitialisation d'identifiants pour quiconque a cliqué. Suspect mais non confirmé → dis-le exactement ainsi, avec ce qui permettrait de confirmer. Légitime → explique les signaux qui l'innocentent.
7. Réponds au déclarant en brouillon ouvert dans le vocabulaire défensif (un e-mail suspect est un « message signalé », pas une « brèche »). Consigne verdict, preuves et raisonnement en note interne ; classe et positionne le statut du ticket. Remercie le déclarant.

Convention française : vocabulaire défensif — « message signalé », « tentative d'hameçonnage présumée », « activité inhabituelle » ; jamais « piratage » ni « fuite de données » avant confirmation formelle. Réponse au déclarant au vouvoiement, close par « Merci d'avoir signalé ce message — c'est exactement le bon réflexe. » Horodatages en JJ/MM/AAAA et 24 h avec fuseau (« 15/07/2026 09 h 12 CET »). Recopie les indicateurs techniques (en-têtes, URL, noms de fichiers) verbatim en anglais — ne les traduis jamais, ils servent de preuves et de clés de recherche.

Garde-fous : n'ouvre, ne clique, ne récupère ni n'affiche jamais liens ou pièces jointes du message signalé — capture les indicateurs en texte uniquement. Vérifie le statut de simulation dans les deux sens (jamais d'incident réel pour une simulation ; jamais clore un vrai hameçonnage comme simulation sur correspondance partielle — exige un domaine de simulateur documenté et exact). Ne réponds jamais au client sur une simulation confirmée. Un clic ou une réponse = escalade immédiate. N'affirme jamais « personne d'autre ne l'a reçu » à partir d'une recherche plafonnée ; écris « aucun autre signalement trouvé dans les N derniers tickets parcourus ». Documente la décision, pas seulement l'action. En cas de doute, contiens.
```
