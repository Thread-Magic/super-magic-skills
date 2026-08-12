---
name: Réponse client
description: Rédiger une réponse externe au client dans la voix et le format maison — point d'avancement, note de statut, message de clôture ou tout e-mail client sur un ticket. (Draft a client-facing reply in the house voice — status updates, closing messages, any client email on a ticket, in French.)
category: Localized
tools: [search_tickets, view_openDraft, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Réponse client

**Quand l'utiliser :** un technicien doit envoyer un message au client et le veut conforme à la charte, prêt à partir — point d'avancement, note de statut ou message de clôture.

**Exécuter :** sur un seul ticket.

## Prompt

```
Rédige une réponse client prête à envoyer pour ce ticket, dans la voix maison.

1. Lis d'abord l'intégralité du fil du ticket — chaque message, note et changement de statut. Ne rédige jamais à partir du seul dernier message.
2. Commence la réponse par la réponse elle-même ou l'état actuel, puis les détails à l'appui.
3. Applique la voix maison :
   - Salue le client par son prénom uniquement sur le premier message d'un fil ; omets la salutation dans les réponses suivantes du même fil.
   - Aucune formule creuse d'ouverture (« J'espère que vous allez bien », « Je me permets de revenir vers vous »). Entre directement dans le vif.
   - Aucun jargon technique sauf si le client a employé le terme en premier ; si un terme technique est inévitable, ajoute une explication en langage courant.
   - 1 à 2 paragraphes courts. S'il en faut davantage, c'est probablement qu'il faut un appel.
4. Si le membre a une liste de mots préférés/bannis, applique-la : remplace les mots bannis par leurs substituts, privilégie les alternatives listées.
5. Pour un message de clôture, termine le corps par : « Si quelque chose n'est pas résolu, il vous suffit de répondre à cet e-mail — votre réponse rouvrira ce ticket. »
6. Signature : si l'espace de travail applique automatiquement une signature gérée, arrête-toi après la dernière phrase du corps — n'ajoute PAS de formule de politesse qui ferait doublon. N'ajoute une formule de clôture que lorsqu'aucune signature gérée n'existe.
7. Montre-moi la réponse en brouillon ouvert pour relecture par le technicien, étiquetée « BROUILLON — à relire avant envoi ». N'envoie pas.

Convention française : vouvoiement systématique ; ne passe au tutoiement que si le client l'a explicitement instauré. Ouverture « Bonjour <Prénom>, » (relation établie) ou « Bonjour Madame/Monsieur <Nom>, » (registre formel) — suis le registre déjà installé dans le fil. Clôture sobre sans signature gérée : « Cordialement, ». Dates en JJ/MM/AAAA, heures en 24 h (« 14 h 30 »), espace insécable avant « : », « ? », « ! », « ; ».

Garde-fous : n'invente jamais de détails — pas d'horodatages, d'étapes réalisées, de numéros de ticket, de liens ni de promesses fabriqués ; si le fil n'établit pas un fait, omets-le ou marque-le <à confirmer avec le technicien>. Le brouillon reste un brouillon tant qu'un humain ne l'a pas approuvé — n'envoie jamais de façon autonome. N'expose jamais de notes internes, d'identifiants, de tarifs ni de données d'autres clients. Aligne-toi sur la langue du client. En cas de doute, ne fais rien. Propose une note interne en texte brut si le membre souhaite en garder une trace.
```
